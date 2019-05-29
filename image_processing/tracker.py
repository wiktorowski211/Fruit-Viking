import cv2
import numpy as np
import time
from threading import Thread
from image_processing.camera import Camera
from image_processing.color_picker import ColorPicker
from image_processing.prediction import Prediction


class Tracker:
    def __init__(self, camera, prediction):
        self.prediction = prediction
        self.camera = camera

        # loop
        self.frequency = 30
        self.running = False
        self.position = 0, 0
        self.im_full = 5

        # image processing

        self.kernel_open = np.ones((5, 5))
        self.kernel_close = np.ones((20, 20))

        # should be None but since we don't have
        # color picking we set it to torch color
        self.lower_color = (-10, -10, 245)
        self.upper_color = (10, 10, 265)

    def start(self):
        self.running = True
        thread = Thread(target=self.loop)
        thread.start()

    def stop(self):
        self.running = False

    def loop(self):
        im_hungry = self.im_full
        while self.running:
            start = time.time()

            # Heavy load

            img = self.camera.image()
            position = self.get_position(img)

            if self.prediction.is_point_valid(position, 25) or im_hungry == 0:
                im_hungry = self.im_full
                self.position = position
            else:
                im_hungry -= 1
                self.position = self.prediction.predicted_point

            self.prediction.predict_next_point(position)

            # End of heavy load

            sleep_time = 1. / self.frequency - (time.time() - start)

            if sleep_time > 0:
                time.sleep(sleep_time)

    def get_position(self, img):
        if self.is_color_set():
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(img_hsv, self.lower_color, self.upper_color)

            mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel_open)
            mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, self.kernel_close)

            contours, h = cv2.findContours(mask_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) > 0:
                largest_contour = max(contours, key=cv2.contourArea)

                return self.highpoint(largest_contour)
            else:
                return 0, 0
        else:
            return 0, 0

    def highpoint(self, contour):
        return tuple(contour[contour[:, :, 1].argmin()][0])

    def set_color(self, color):
        self.lower_color = color[0]
        self.upper_color = color[1]

    def is_color_set(self):
        return self.lower_color is not None and self.upper_color is not None


if __name__ == '__main__':

    camera = Camera(1280, 720)
    prediction = Prediction()

    tracker = Tracker(camera, prediction)
    tracker.start()

    color_picker = ColorPicker()

    while True:
        img = camera.image()

        center = color_picker.center_point(img)

        camera.draw_circle(img, center, 2)
        camera.write_message(img, 'Press q to choose color from the center')

        key = cv2.waitKey(125)

        if key == ord('q'):
            color = color_picker.from_area(img, 10)
            tracker.set_color(color)

        tracked_position = tracker.position

        camera.draw_circle(img, tracked_position, -1)

        camera.show(img)
