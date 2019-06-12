import pygame
from src.colors import blue
from src.resources import gfx


class Controller:
    def __init__(self):
        self.area = None
        self.position = (0, 0)
        self.radius = 10

        self.debug = True

        img = gfx('pointer-shield.png', convert=True)
        self.img = pygame.transform.scale(img, (self.radius*2, self.radius*2))

    def update_position(self):
        pass

    def render(self, screen):
        last_area = self.area

        if self.debug is True:
            pygame.draw.circle(screen, blue, self.position, self.radius)
        blit_x_pos = self.position[0] - self.radius
        blit_y_pos = self.position[1] - self.radius
        self.area = screen.blit(self.img, (blit_x_pos, blit_y_pos))

        return last_area, self.area

    def clean_up(self):
        pass
