import pygame
from src.colors import blue


class Controller:
    def __init__(self):
        self.area = None
        self.position = (0, 0)
        self.radius = 10

    def update_position(self):
        pass

    def render(self, screen):
        last_area = self.area

        self.area = pygame.draw.circle(screen, blue, self.position, self.radius)

        return last_area, self.area

    def clean_up(self):
        pass
