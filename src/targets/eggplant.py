from .target import Target
import src.resources as res


class Eggplant(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        eggplant = res.gfx('eggplant.png', convert=True)
        Target.__init__(self, eggplant, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('eggplant.png', convert=True)
