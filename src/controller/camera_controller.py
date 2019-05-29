from image_processing.camera import Camera
from image_processing.tracker import Tracker
from .controller import Controller


class CameraController(Controller):
    def __init__(self):
        Controller.__init__(self)

        camera = Camera(1280, 720)
        self.tracker = Tracker(camera)
        self.tracker.start()

    def update_position(self):
        self.position = self.tracker.position
        return self.position
