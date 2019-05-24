from .state import State
from src.targets import Strawberry
from src.colors import gray
import pygame


class LevelState1(State):

    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)
        self.active = True

        target1 = Strawberry((200, 200), self.screen, True)

        target2 = Strawberry((300, 300), self.screen, True)

        self.targets = [target2]
        self.targets.append(target1)

        # For rect cleanup
        self.deleteds_area = []

        self.score = 0

    def render(self):
        rects = [] + self.deleteds_area

        self.deleteds_area.clear()

        self.screen.fill(gray)
        for target in self.targets:
            rect_a, rect_b = target.render()
            rects.append(rect_a)
            rects.append(rect_b)

        return rects

    def tick(self, dt):
        marked_for_delete = []
        for i, target in enumerate(self.targets):
            target.update(dt, (300, 300), 10)
            if target.defeated is True:
                marked_for_delete.append(i)
                self.deleteds_area.append(target.last_area)
        for index in marked_for_delete[::-1]:
            del self.targets[index]




    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Go back to level selection")
                self._game.remove_top_state()
