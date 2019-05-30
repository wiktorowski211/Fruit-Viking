from .target import Target
import src.resources as res


class Kiwi(Target):

    def __init__(self, pos, screen, debug: bool = False):
        kiwi = res.gfx('kiwi.png', convert=True)
        Target.__init__(self, kiwi, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('kiwi.png', convert=True)
