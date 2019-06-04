from .state import State

import pygame
import src.resources as res

from src.util import text_format
from src.colors import yellow, white, black, gray


# Menu Fonts
main_font = "Splatch.ttf"


class ResultScreenState(State):
    def __init__(self, *args, score, **kwargs):
        State.__init__(self, *args, **kwargs)

        # Menu should be always active
        self.active = True

        print("In result state:")
        print(score)

        total = 0
        hits = 0

        for key, value in score.items():
            if value['is_fruit'] is True:
                total_gain = value['hits'] + value['misses']

                total += total_gain
                hits += value['hits']
        percentage = hits / total
        print(round(percentage, 4) * 100, '%')

    def render(self):
        rects = []
        self.screen.fill(gray)

        return rects

    def tick(self, dt):
        pass

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or pygame.K_ESCAPE:
                # res.music("cut.ogg")
                self._game.remove_top_state()
