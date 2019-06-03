from .target import Target
import src.resources as res


class Banana(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        banana = res.gfx('banana.png', convert=True)
        Target.__init__(self, banana, pos, screen, debug)

        w, _h =banana.get_size()
        self.radius = int(w / 2.6)
        self.offset = (13, 23)
    @staticmethod
    def get_image():
        return res.gfx('banana.png', convert=True)
