from .state import State
from src.targets import Strawberry
from src.colors import gray
import pygame


class LevelState1(State):

    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)
        self.active = True

        self.target1 = Strawberry((200, 200), self.screen, False)

    def render(self):
        rects = []

        self.screen.fill(gray)
        rect_a, rect_b = self.target1.render()
        rects.append(rect_a)
        rects.append(rect_b)

        return rects

    def tick(self, dt):
        self.target1.update(dt, (300, 300), 10)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Go back to level selection")
                self._game.remove_top_state()
