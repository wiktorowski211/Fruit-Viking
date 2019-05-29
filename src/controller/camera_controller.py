from image_processing.camera import Camera
from image_processing.tracker import Tracker
from .controller import Controller


class CameraController(Controller):
    def __init__(self):
        Controller.__init__(self)

        self.camera = Camera(1280, 720)

        self.tracker = Tracker()

    def update_position(self):
        img = self.camera.image()

        self.position = self.tracker.get_position(img)
        return self.position
