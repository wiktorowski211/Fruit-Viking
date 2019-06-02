from .target import Target
import src.resources as res


class Pineapple(Target):

    def __init__(self, pos, screen, debug: bool = False):
        pineapple = res.gfx('pineapple.png', convert=True)
        Target.__init__(self, pineapple, pos, screen, debug)

        w, _h = pineapple.get_size()
        self.radius = int(w / 3.5)
        self.offset = (50, 65)

    @staticmethod
    def get_image():
        return res.gfx('pineapple.png', convert=True)
