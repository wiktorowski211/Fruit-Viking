import cv2
import numpy as np
import colorsys


def top_point(c):
    return tuple(c[c[:, :, 1].argmin()][0])


# python
# bgr = [59, 30, 132]
# bgr = [195, 255, 15]
# thresh = 60

# convert 1D array to 3D, then convert it to HSV and take the first element
# this will be same as shown in the above figure [65, 229, 158]
# hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]

# lower_bound = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
# upper_bound = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])

# hsv_low = colorsys.hsv_to_rgb(33, 80, 40)
# hsv_high = colorsys.hsv_to_rgb(102, 255, 255)
#
# print(hsv_low)
# print(hsv_high)
#
# rgb_low = colorsys.rgb_to_hsv(194, 119, 255)
# rgb_high = colorsys.rgb_to_hsv(71, 0, 130)

lower_bound = np.array([33, 80, 40])
upper_bound = np.array([102, 255, 255])

cam = cv2.VideoCapture(0)
kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cam.read()

    # convert BGR to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # create the Mask
    mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
    # morphology
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    conts, h = cv2.findContours(maskClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(conts) > 0:
        # draw in blue the contours that were founded
        cv2.drawContours(img, conts, -1, 255, 3)
        # print(len(conts))
        # find the biggest area
        c = max(conts, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(c)
        # draw the book contour (in green)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        top = top_point(c)
        cv2.circle(img, top, 8, (0, 0, 255), -1)

    cv2.imshow("cam", img)
    cv2.waitKey(10)