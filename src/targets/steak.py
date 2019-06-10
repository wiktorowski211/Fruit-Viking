from .target import Target
import src.resources as res


class Steak(Target):

    def __init__(self, pos, screen, debug: bool = False):
        steak = res.gfx('steak.png', convert=True)
        Target.__init__(self, steak, pos, screen, debug)

        #w, _h = apple.get_size()
        #self.radius = int(w / 2.5)
        #self.offset = (22, 25)

    def on_defeat(self, targets: list):
        for target in targets:
            target.velocity = target.velocity[0] * 2.0, target.velocity[1]

    @staticmethod
    def get_image():
        return res.gfx('steak.png', convert=True)

    # If the target is supposed to be sliced
    @staticmethod
    def is_fruit():
        return False
