from .target import Target
import src.resources as res


class Grapes(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        grapes = res.gfx('grapes.png', convert=True)
        Target.__init__(self, grapes, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('grapes.png', convert=True)
