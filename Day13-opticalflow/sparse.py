import numpy as np 
import time 
import cv2 

# Lucas-Kanade optical flow parameters
lk_params = dict(winSize = (15, 15),
                 maxLevel = 2,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Parameters for corner detection
feature_params = dict(maxCorners = 20,
                      qualityLevel = 0.3,
                      minDistance = 10,
                      blockSize = 7)

# Initialize trajectory parameters
trajectory_len = 20 
detect_interval = 1
trajectories = []
frame_idx = 0

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Start time for calculating FPS
    start = time.time()
    suc, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = frame.copy()

    # Initialize new_trajectories as an empty list
    new_trajectories = []

    # Calculate optical flow for a sparse feature set
    if len(trajectories) > 0:
        img0, img1 = prev_gray, frame_gray 
        p0 = np.float32([trajectory[-1] for trajectory in trajectories]).reshape(-1,1,2)
        p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)

        p0r, str, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)
        d = abs(p0 - p0r).reshape(-1, 2).max(-1)
        good = d < 1

        # Get all trajectories
        for trajectory, (x, y), good_flag in zip(trajectories, p1.reshape(-1, 2), good):
            if not good_flag:
                continue
            trajectory.append((x, y))
            if len(trajectory) > trajectory_len:
                del trajectory[0]
            new_trajectories.append(trajectory)

            # Draw the newest detected point
            cv2.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)

    trajectories = new_trajectories

    # Draw all trajectories
    cv2.polylines(img, [np.int32(trajectory) for trajectory in trajectories], False, (0, 255, 0))

    cv2.putText(img, 'track count: %d' % len(trajectories), (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0))

    # Update the interval to detect new features
    if frame_idx % detect_interval == 0:
        mask = np.zeros_like(frame_gray)
        mask[:] = 255

        # Avoid detecting features in the latest points of trajectories
        for x, y in [np.int32(trajectory[-1]) for trajectory in trajectories]:
            cv2.circle(mask, (x, y), 5, 0, -1)

        # Detect good features to track
        p = cv2.goodFeaturesToTrack(frame_gray, mask=mask, **feature_params)
        if p is not None:
            # If good features are detected, add them to the trajectories
            for x, y in np.int32(p).reshape(-1, 2):
                trajectories.append([(x, y)])

    frame_idx += 1
    prev_gray = frame_gray

    # End time for calculating FPS
    end = time.time()
    fps = 1 / (end - start)
    print(f"FPS: {fps:.2f}")

    # Show the results
    cv2.putText(img, f"{fps:.2f} FPS", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    cv2.imshow('Optical Flow', img)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
