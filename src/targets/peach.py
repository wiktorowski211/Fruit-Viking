from .target import Target
import src.resources as res


class Peach(Target):
    #    def __init__(self, image, pos, screen, debug: bool = True):

    def __init__(self, pos, screen, debug: bool = False):
        peach = res.gfx('peach.png', convert=True)
        Target.__init__(self, peach, pos, screen, debug)

        w, _h = peach.get_size()
        self.radius = int(w / 2.3)
        self.offset = (17, 23)

    @staticmethod
    def get_image():
        return res.gfx('peach.png', convert=True)
