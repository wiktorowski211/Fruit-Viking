from .target import Target
import src.resources as res


class Melon(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        melon = res.gfx('melon.png', convert=True)
        Target.__init__(self, melon, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('melon.png', convert=True)
