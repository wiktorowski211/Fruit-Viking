import cv2
import numpy as np


class Tracker:
    def __init__(self, width, height):
        self.window_size = (width, height)

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.enabled = False

        self.kernel_open = np.ones((5, 5))
        self.kernel_close = np.ones((20, 20))

    def run(self):
        self.enabled = True

        camera = cv2.VideoCapture(0)

        lower_bound = None
        upper_bound = None

        while self.enabled:

            ret, img = camera.read()

            img = cv2.resize(img, self.window_size)
            img = cv2.flip(img, 1)

            center = self.center_point(img)
            cv2.circle(img, center, 10, (0, 0, 255), 2)

            self.write_message(img, 'Press q to choose color from the center')

            key = cv2.waitKey(125)

            if key == ord('q'):
                center_point_color = self.color_from_area(img, center, 10)
                print(center_point_color)
                lower_bound = center_point_color[0]
                upper_bound = center_point_color[1]

            if lower_bound is not None and upper_bound is not None:
                tracked_position = self.position(img, lower_bound, upper_bound)

                cv2.circle(img, tracked_position, 8, (0, 0, 255), -1)

            cv2.imshow("cam", img)
            cv2.waitKey(10)

        cv2.destroyAllWindows()

    def position(self, img, lower_bound, upper_bound):
        # convert BGR to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # create the Mask
        mask = cv2.inRange(img_hsv, lower_bound, upper_bound)

        # morphology
        mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel_open)
        mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, self.kernel_close)

        contours, h = cv2.findContours(mask_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            # draw in blue the contours that were founded
            cv2.drawContours(img, contours, -1, 255, 3)

            # find the largest contour
            largest_contour = max(contours, key=cv2.contourArea)

            self.draw_contour_rect(img, largest_contour)

            return self.top_point(largest_contour)

    def finish(self):
        self.enabled = False
        cv2.destroyAllWindows()

    def top_point(self, contour):
        return tuple(contour[contour[:, :, 1].argmin()][0])

    def center_point(self, img):
        dimensions = img.shape
        x_center = int(dimensions[1] / 2)
        y_center = int(dimensions[0] / 2)
        return x_center, y_center

    def color_from_area(self, img, center, size):
        hsv_roi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        crop_img = hsv_roi[center[1] - 1:center[1] + 1, center[0] - 1:center[0] + 1]
        lower = np.array([crop_img[:, :, 0].min(), crop_img[:, :, 1].min(), crop_img[:, :, 2].min()])
        lower_threshold = np.array([lower[0] - size, lower[1] - size, lower[2] - size])
        upper = np.array([crop_img[:, :, 0].max(), crop_img[:, :, 1].max(), crop_img[:, :, 2].max()])
        upper_threshold = np.array([upper[0] + size, upper[1] + size, upper[2] + size])
        return lower_threshold, upper_threshold

    def write_message(self, img, text):
        cv2.putText(img, text, (10, 25), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    def draw_contour_rect(self, img, contour):
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


tracker = Tracker(1280, 820)
tracker.run()
