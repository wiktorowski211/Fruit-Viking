class Prediction:
    def __init__(self, q):
        self.min_accuracy = 1
        self.q = q
        self.last_timestamp = 0
        self.position = 0, 0
        self.variance = -1.0

    def set_state(self, position, accuracy, timestamp):
        self.position = position
        self.variance = accuracy ** 2
        self.last_timestamp = timestamp

    def process(self, position, accuracy, timestamp):
        if accuracy < self.min_accuracy:
            accuracy = self.min_accuracy
        if self.variance < 0:
            self.set_state(position, accuracy, timestamp)
        else:
            delta_time = timestamp - self.last_timestamp
            if delta_time > 0:
                self.variance += delta_time * self.q ** 2 / 1000
                self.last_timestamp = timestamp

            x0, y0 = self.position
            x1, y1 = position

            k = self.variance / (self.variance + accuracy ** 2)
            x0 += int(round(k * (x1 - x0)))
            y0 += int(round(k * (y1 - y0)))
            self.variance = (1 - k) * self.variance

            self.position = x0, y0

        return self.position
