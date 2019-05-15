import cv2
import numpy as np
from image_processing.camera import Camera
from image_processing.color_picker import ColorPicker


class Tracker:
    def __init__(self):
        self.kernel_open = np.ones((5, 5))
        self.kernel_close = np.ones((20, 20))

        self.lower_bound = None
        self.upper_bound = None

    def set_color(self, color):
        self.lower_bound = color[0]
        self.upper_bound = color[1]

    def color_set(self):
        return self.lower_bound is not None and self.upper_bound is not None

    def get_position(self, img):
        if self.color_set():
            # convert BGR to HSV
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # create the Mask
            mask = cv2.inRange(img_hsv, self.lower_bound, self.upper_bound)

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
        else:
            return None

    def top_point(self, contour):
        return tuple(contour[contour[:, :, 1].argmin()][0])

    # only for test, will be deleted
    def draw_contour_rect(self, img, contour):
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


if __name__ == '__main__':

    camera = Camera(1280, 820)
    color_picker = ColorPicker()
    tracker = Tracker()

    while True:
        img = camera.image()

        center = color_picker.center_point(img)

        camera.draw_circle(img, center, 2)
        camera.write_message(img, 'Press q to choose color from the center')

        key = cv2.waitKey(125)

        if key == ord('q'):
            color = color_picker.from_area(img, 10)
            tracker.set_color(color)

        if tracker.color_set():
            tracked_position = tracker.get_position(img)

            if tracked_position is not None:
                camera.draw_circle(img, tracked_position, -1)

        camera.show(img)