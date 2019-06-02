from .target import Target
import src.resources as res


class Avocado(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        avocado = res.gfx('avocado.png', convert=True)
        Target.__init__(self, avocado, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('avocado.png', convert=True)
