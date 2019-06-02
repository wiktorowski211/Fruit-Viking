from .target import Target
import src.resources as res


class Pear(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        pear = res.gfx('pear.png', convert=True)
        Target.__init__(self, pear, pos, screen, debug)

        w, _h = pear.get_size()
        self.radius = int(w / 2.3)
        self.offset = (7, 20)
    @staticmethod
    def get_image():
        return res.gfx('pear.png', convert=True)
