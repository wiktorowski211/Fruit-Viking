from math import sqrt


class Prediction:
    def __init__(self, q_metres_per_second):
        self.min_accuracy = 1
        self.q_metres_per_second = q_metres_per_second
        self.timestamp_milliseconds = 0
        self.lat = 0
        self.lng = 0
        # P matrix. Negative means object uninitialised.  NB: units irrelevant, as long as same units used throughout
        self.variance = -1.0

    def get_accuraccy(self):
        return sqrt(self.variance)

    def set_state(self, lat, lng, accuracy, timestamp_milliseconds):
        self.lat = lat
        self.lng = lng
        self.variance = accuracy ** 2
        self.timestamp_milliseconds = timestamp_milliseconds

    def process(self, lat, lng, accuracy, timestamp_milliseconds):
        if accuracy < self.min_accuracy:
            accuracy = self.min_accuracy
        if self.variance < 0:
            # object is unitialised, so initialise with current values
            self.set_state(lat, lng, accuracy, timestamp_milliseconds)
        else:
            # apply Kalman filter methodology
            timeinc_milliseconds = timestamp_milliseconds - self.timestamp_milliseconds
            if timeinc_milliseconds > 0:
                # time has moved on, so the uncertainty in the current position increases
                self.variance += timeinc_milliseconds * self.q_metres_per_second ** 2 / 1000
                self.timestamp_milliseconds = timestamp_milliseconds
                # TO DO: USE VELOCITY INFORMATION HERE TO GET A BETTER ESTIMATE OF CURRENT POSITION

            # Kalman gain matrix K = Covarariance * Inverse(Covariance + MeasurementVariance)
            # NB: because K is dimensionless, it doesn't matter that variance has different units to lat and lng
            K = self.variance / (self.variance + accuracy ** 2)
            self.lat += int(round(K * (lat - self.lat)))
            self.lng += int(round(K * (lng - self.lng)))
            # new Covarariance  matrix is (IdentityMatrix - K) * Covarariance
            self.variance = (1 - K) * self.variance

            return self.lat, self.lng
