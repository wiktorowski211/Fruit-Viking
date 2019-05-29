from image_processing.camera import Camera
import time


class Prediction:
    def __init__(self):
        # loop
        self.frequency = 30
        self.last_point = 0, 0
        self.last_time = time.time()
        self.last_velocity = 0

        self.vector_x = 0
        self.vector_y = 0

    def predict(self, point):
        # new_time = time.time()

        x1, y1 = point
        x0, y0 = self.last_point

        self.vector_x = x1 - x0
        self.vector_y = y1 - y0

        self.last_point = point


if __name__ == '__main__':
    camera = Camera(1280, 720)

    pr = Prediction()
    pr.predict((5, 5))
    pr.predict((10, 10))
    pr.predict((15, 15))
    pr.predict((20, 22))
    pr.predict((25, 29))
