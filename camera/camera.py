# import cv2
#
# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)
#
# rval, frame = vc.read()
#
# while True:
#
#   if frame is not None:
#      cv2.imshow("preview", frame)
#   rval, frame = vc.read()
#
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#      break

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_blue = np.array([333, 39, 50])   #244, 66, 69
    upper_blue = np.array([359, 100, 100])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
