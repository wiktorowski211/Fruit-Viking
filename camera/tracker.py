import cv2
import numpy as np
import colorsys
import time

def top_point(c):
    return tuple(c[c[:, :, 1].argmin()][0])

def get_center_x_y(img):
    dimensions = img.shape
    x_center = int(dimensions[1]/2)
    y_center = int(dimensions[0]/2)
    return (x_center, y_center)

def get_center_point_boundries(img, center):
    hsvRoi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    crop_img = hsvRoi[center[1]-1:center[1]+1, center[0]-1:center[0]+1]
    lower = np.array([crop_img[:, :, 0].min(), crop_img[:, :, 1].min(), crop_img[:, :, 2].min()])
    lower_treshold = np.array([lower[0]-10, lower[1]-10, lower[2]-10])
    upper = np.array([crop_img[:, :, 0].max(), crop_img[:, :, 1].max(), crop_img[:, :, 2].max()])
    upper_treshold = np.array([upper[0]+10, upper[1]+10, upper[2]+10])
    return (lower_treshold, upper_treshold)

def write_g_needed_text(cv2):
    cv2.putText(img, 'Press q to choose color from the center', (10, 25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

lower_bound = np.array([33, 80, 40])
upper_bound = np.array([102, 255, 255])

cam = cv2.VideoCapture(0)
kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))

font = cv2.FONT_HERSHEY_SIMPLEX

center_point_color = ([0, 0, 0],[0, 0, 0])

while True:
    k = cv2.waitKey(125)

    ret, img = cam.read()
    center = get_center_x_y(img)

    # convert BGR to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # create the Mask
    mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
    # morphology
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    conts, h = cv2.findContours(maskClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.circle(img, center, 10, (0,0,255), 2)
    write_g_needed_text(cv2)
    if k == ord('q'):
        center_point_color = get_center_point_boundries(img, center)
        print(center_point_color)
        lower_bound = center_point_color[0]
        upper_bound = center_point_color[1]

    else:
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

cv2.release()
cv2.destroyAllWindows()