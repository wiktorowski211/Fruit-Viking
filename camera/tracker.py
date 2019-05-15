import cv2
import numpy as np


class Camera:
    def __init__(self, width, height):
        self.window_size = (width, height)

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.camera = cv2.VideoCapture(0)

    def image(self):
        ret, img = self.camera.read()
        img = cv2.resize(img, self.window_size)
        img = cv2.flip(img, 1)
        return img

    def show(self, img):
        cv2.imshow("cam", img)
        cv2.waitKey(10)

    def kill(self):
        cv2.destroyAllWindows()

    def write_message(self, img, text):
        cv2.putText(img, text, (10, 25), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    def draw_rect(self, img, contour):
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    def draw_circle(self, img, position, thickness):
        cv2.circle(img, position, 10, (0, 0, 255), thickness)


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
