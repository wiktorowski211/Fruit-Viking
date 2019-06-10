import src.resources as res
from random import choice, uniform


class Remains:
    def __init__(self, life_time, pos, is_fruit: bool = True):
        self.life_time = uniform(life_time - 0.5, life_time + 0.5)
        if is_fruit:
            img = choice(['exp1', 'exp2', 'exp3', 'exp4', 'exp5'])
        else:
            img = 'blood1'
        self.img = res.gfx(img + '.png', convert=True)
        self.pos = pos

    def update(self, dt):
        self.life_time -= dt
        if self.life_time <= 0.0:
            return False
        return True

    def render(self, screen):
        return screen.blit(self.img, self.pos)

    def area(self):
        w, h = self.img.get_size()
        left, top = self.pos
        return left, top, w, h
