from .target import Target
import src.resources as res


class Tangerine(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        tangerine = res.gfx('tangerine.png', convert=True)
        Target.__init__(self, tangerine, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('tangerine.png', convert=True)
