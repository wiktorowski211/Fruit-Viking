from .target import Target
import src.resources as res


class Strawberry(Target):

    def __init__(self, pos, screen, debug: bool = False):
        strawberry = res.gfx('strawberry.png', convert=True)
        Target.__init__(self, strawberry, pos, screen, debug)

        w, _h =strawberry.get_size()
        self.radius = int(w / 2.6)
        self.offset = (20, 30)

    @staticmethod
    def get_image():
        return res.gfx('strawberry.png', convert=True)
