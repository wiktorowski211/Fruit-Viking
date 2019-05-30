from .target import Target
import src.resources as res


class Watermelon(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        watermelon = res.gfx('watermelon.png', convert=True)
        Target.__init__(self, watermelon, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('watermelon.png', convert=True)
