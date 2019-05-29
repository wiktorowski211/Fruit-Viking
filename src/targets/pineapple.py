from .target import Target
import src.resources as res


class Pineapple(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        pineapple = res.gfx('pineapple.png', convert=True)
        Target.__init__(self, pineapple, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('pineapple.png', convert=True)
