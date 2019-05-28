import pygame
from src.colors import blue


class Controller:
    def __init__(self):
        self.area = None
        self.position = (0, 0)

    def update_position(self):
        pass

    def render(self, screen):
        last_area = self.area

        self.area = pygame.draw.circle(screen, blue, self.position, 10)

        return last_area, self.area
