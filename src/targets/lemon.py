from .target import Target
import src.resources as res


class Lemon(Target):

    def __init__(self, pos, screen, debug: bool = False):
        lemon = res.gfx('lemon.png', convert=True)
        Target.__init__(self, lemon, pos, screen, debug)

        w, _h = lemon.get_size()
        self.radius = int(w / 2.5)
        self.offset = (25, 25)

    @staticmethod
    def get_image():
        return res.gfx('lemon.png', convert=True)
