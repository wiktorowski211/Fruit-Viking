from .target import Target
import src.resources as res


class Grapes(Target):

    def __init__(self, pos, screen, debug: bool = False):
        grapes = res.gfx('grapes.png', convert=True)
        Target.__init__(self, grapes, pos, screen, debug)

        w, _h = grapes.get_size()
        self.radius = int(w / 2.1)
        self.offset = (10, 10)

    @staticmethod
    def get_image():
        return res.gfx('grapes.png', convert=True)
