import cv2
import numpy as np
import time
from threading import Thread
from image_processing.camera import Camera
from image_processing.prediction import Prediction


class Tracker:
    def __init__(self, camera, prediction):
        self.prediction = prediction
        self.camera = camera

        self.previous_position = 0, 0

        # loop
        self.frequency = 30
        self.running = False
        self.position = 0, 0

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
        while self.running:
            start = time.time()

            # Heavy load

            img = self.camera.image()
            position = self.get_position(img)

            timestamp = time.time() * 1000

            predicted = self.prediction.process(position, 50, timestamp)

            self.position = predicted

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
                self.previous_position = self.highpoint(largest_contour)
                return self.previous_position
            else:
                return self.previous_position
        else:
            return self.previous_position

    def highpoint(self, contour):
        return tuple(contour[contour[:, :, 1].argmin()][0])

    def set_color(self, color):
        self.lower_color, self.upper_color = color

    def is_color_set(self):
        return self.lower_color is not None and self.upper_color is not None


if __name__ == '__main__':

    camera = Camera(1280, 720)
    prediction = Prediction(200)

    tracker = Tracker(camera, prediction)
    while True:
        start = time.time()

        # Heavy load

        img = camera.image()

        position = tracker.get_position(img)

        timestamp = time.time() * 1000

        predicted = prediction.process(position, 50, timestamp)

        camera.draw_circle(img, position, -1, (0, 0, 255))

        camera.draw_circle(img, predicted, 10, (255, 0, 0))

        camera.show(img)

        # End of heavy load

        sleep_time = 1. / 30 - (time.time() - start)

        if sleep_time > 0:
            time.sleep(sleep_time)
