from .target import Target
import src.resources as res


class Cherry(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        cherry = res.gfx('cherry.png', convert=True)
        Target.__init__(self, cherry, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('cherry.png', convert=True)
