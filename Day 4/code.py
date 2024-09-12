import HSV_filter as hsv 
import shape_recognition as shape 
import triangulation as tri 
import cv2
import numpy as np

cap_right = cv2.VideoCapture('http://192.168.0.102:8080/video')
cap_left = cv2.VideoCapture(0)

target_width, target_height = 400, 400

frame_rate = 120 

B=9
f=6 
alpha=56.6

count = -1

while (True):
    count+=1

    ret_right, frame_right = cap_right.read()
    ret_left, frame_left = cap_left.read()

    frame_right = cv2.resize(frame_right, (target_width, target_height))
    frame_left = cv2.resize(frame_left, (target_width, target_height))

    # else:
    mask_right = hsv.add_HSV_filter(frame_right,1)
    mask_left = hsv.add_HSV_filter(frame_left,0)

    res_right = cv2.bitwise_and(frame_right, frame_right, mask = mask_right)
    res_left = cv2.bitwise_and(frame_left, frame_left, mask = mask_left)

    circles_right = shape.find_circles(frame_right, mask_right)
    circles_left = shape.find_circles(frame_left, mask_left)
    

    if np.all(circles_right) == None or np.all(circles_left) == None:
        cv2.putText(frame_right, "TRACKING LOST",(75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        cv2.putText(frame_left, "TRACKING LOST",(75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    else:
        depth = tri.find_depth(circles_right, circles_left, frame_right, frame_left, B, f, alpha)

        cv2.putText(frame_right, "TRACKING", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
        cv2.putText(frame_left, "TRACKING", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
        

        cv2.putText(frame_right, "Distance : " + str(round(depth,3)), (200,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
        cv2.putText(frame_left, "Distance : " + str(round(depth,3)), (200,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)

        print("depth :  ", depth)

    cv2.imshow("frame right", frame_right)
    cv2.imshow("frame left", frame_left)
    cv2.imshow("mask right", mask_right)
    cv2.imshow("mask left", mask_left)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_right.release()
cap_left.release()

cv2.destroyAllWindows()
