from .target import Target
import src.resources as res


class Steak(Target):

    def __init__(self, pos, screen, debug: bool = False):
        steak = res.gfx('steak.png', convert=True)
        Target.__init__(self, steak, pos, screen, debug)

        w, _h = steak.get_size()
        self.radius = int(w / 2.25)
        self.offset = (6, 6)

    def on_defeat(self, targets: list):
        for target in targets[1::3]:
            target.velocity = target.velocity[0] * 2.0, target.velocity[1]

    @staticmethod
    def get_image():
        return res.gfx('steak.png', convert=True)

    @staticmethod
    def is_fruit():
        return False
