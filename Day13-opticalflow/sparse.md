# Optical Flow with Corner Detection and Trajectories - Notes

## Overview

This project focuses on detecting good features in an image frame using **optical flow** and **corner detection** to track trajectories over time. Below are the key steps and concepts:

---

## Key Steps:

### 1. Mask for Tracking Points
- We take the latest point in the trajectory and display it on a mask.
- This mask helps detect corners, which will then be used to track points of interest.
- The mask is used to highlight the areas that contain important points or corners in the image frame.
  
### 2. Loop Through Coordinates
- A loop is run through the x and y values of the latest trajectory.
- Each point is plotted on the mask to visualize the features being tracked.

---

## Detecting Good Features

### 3. Using `goodFeaturesToTrack`
- We use OpenCV's `goodFeaturesToTrack` to detect corners and track them as key points in the image.
- The mask created earlier is passed in to identify points of interest within the trajectory.
- Parameters like `maxCorners`, `qualityLevel`, and `minDistance` control how many and which features to track.

#### Feature Parameters:
- **maxCorners**: 20
- **qualityLevel**: 0.3
- **minDistance**: 10
- **blockSize**: 7

Play around with these parameters to adjust how features are detected and tracked.

---

## Trajectory Updates

### 4. Appending Good Features to Trajectories
- If good features are detected, their x and y coordinates are appended to the trajectories list.
- This allows the program to maintain a running list of the tracked points over time.

### 5. Frame Index
- The frame index is updated, and each frame helps generate the next trajectory.
- The current frame is set as the new reference for the next set of tracking points.

---

## Viewing Optical Flow

### 6. Frames per Second (FPS)
- The program calculates and prints the FPS.
- The mask and the points being tracked are displayed to visualize the corners and trajectories.

### 7. Green Lines and Red Dots
- **Red Dots**: Nearest points in consecutive frames.
- **Green Lines**: Represent the trajectory of a point across frames. Each green line stores a history of up to 20 points.

---

## Adjusting Parameters

### 8. Changing Trajectory Length and Detection Interval
- By adjusting the **trajectory length** and **detection interval**, the speed and number of points tracked can be modified.
- Increasing the trajectory length will result in longer green lines as more points are stored.

---

## Real-world Applications

- Optical flow can be used to track moving objects like cars on a highway, following their motion trajectory over time.
- The system efficiently tracks points at high FPS (70-80 FPS) on a CPU, making it suitable for real-time applications.

