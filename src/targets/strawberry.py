from .target import Target
import src.resources as res


class Strawberry(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        strawberry = res.gfx('strawberry.png', convert=True)
        Target.__init__(self, strawberry, pos, screen, debug)

    @staticmethod
    def get_image():
        return res.gfx('strawberry.png', convert=True)
