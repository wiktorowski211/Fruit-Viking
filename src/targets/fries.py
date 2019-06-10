from .target import Target
import src.resources as res


class Fries(Target):

    def __init__(self, pos, screen, debug: bool = False):
        fries = res.gfx('fries.png', convert=True)
        Target.__init__(self, fries, pos, screen, debug)

        # w, _h = apple.get_size()
        # self.radius = int(w / 2.5)
        # self.offset = (22, 25)

    def on_defeat(self, targets: list):
        for target in targets[1::2]:
            target.velocity = target.velocity[0], target.velocity[1] + 125.0

    @staticmethod
    def get_image():
        return res.gfx('fries.png', convert=True)

    @staticmethod
    def is_fruit():
        return False
