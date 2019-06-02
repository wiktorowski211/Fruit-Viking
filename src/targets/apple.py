from .target import Target
import src.resources as res


class Apple(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        apple = res.gfx('apple.png', convert=True)
        Target.__init__(self, apple, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('apple.png', convert=True)