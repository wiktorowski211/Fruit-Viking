import pygame
from .controller import Controller


class MouseController(Controller):
    def __init__(self):
        Controller.__init__(self)

        pygame.mouse.set_visible(False)

    def update_position(self):
        self.position = pygame.mouse.get_pos()
        return self.position
