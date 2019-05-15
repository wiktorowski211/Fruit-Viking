import cv2
import numpy as np


class ColorPicker:
    def from_area(self, img, size):
        center = self.center_point(img)

        hsv_roi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        crop_img = hsv_roi[center[1] - 1:center[1] + 1, center[0] - 1:center[0] + 1]
        lower = np.array([crop_img[:, :, 0].min(), crop_img[:, :, 1].min(), crop_img[:, :, 2].min()])
        lower_threshold = np.array([lower[0] - size, lower[1] - size, lower[2] - size])
        upper = np.array([crop_img[:, :, 0].max(), crop_img[:, :, 1].max(), crop_img[:, :, 2].max()])
        upper_threshold = np.array([upper[0] + size, upper[1] + size, upper[2] + size])
        return lower_threshold, upper_threshold

    def center_point(self, img):
        dimensions = img.shape
        x_center = int(dimensions[1] / 2)
        y_center = int(dimensions[0] / 2)
        return x_center, y_center
