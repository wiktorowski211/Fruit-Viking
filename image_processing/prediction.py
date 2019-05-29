from image_processing.camera import Camera
from math import sqrt


class Prediction:
    def __init__(self):
        self.last_point = 0, 0
        self.predicted_point = 0, 0
        self.last_distance = 0

    def is_point_valid(self, point, distance_toleration):
        distance = self.get_distance(point, self.predicted_point)
        if distance < self.last_distance + distance_toleration:
            return True
        else:
            return False

    def get_distance(self, point1, point2):
        x1, y1 = point1
        x0, y0 = point2
        return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    def predict_next_point(self, point):
        x1, y1 = point
        x0, y0 = self.last_point

        self.last_distance = self.get_distance(point, self.last_point)

        x1 += x1 - x0
        y1 += y1 - y0

        self.last_point = point
        self.predicted_point = x1, y1


if __name__ == '__main__':
    camera = Camera(1280, 720)

    pr = Prediction()
    pr.predict_next_point((10, 20))
    pr.predict_next_point((8, 18))
    pr.predict_next_point((6, 16))
    pr.predict_next_point((20, 22))
    pr.predict_next_point((25, 29))
