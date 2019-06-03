from .target import Target
import src.resources as res


class Tangerine(Target):

    def __init__(self, pos, screen, debug: bool = False):
        tangerine = res.gfx('tangerine.png', convert=True)
        Target.__init__(self, tangerine, pos, screen, debug)

        w, _h = tangerine.get_size()
        self.radius = int(w / 2.5)
        self.offset = (14, 25)

    @staticmethod
    def get_image():
        return res.gfx('tangerine.png', convert=True)
