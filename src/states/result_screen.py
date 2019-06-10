from .state import State

import pygame
import src.resources as res

from src.util import text_format
from src.colors import red, yellow, green, white, gray


# Used fonts
main_font = "Splatch.ttf"

#percentage_font = "MIB.ttf"
percentage_font = "Noise Machine.ttf"


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
        percentage = (hits / total) * 100
        percentage = int(percentage)

        self.init_render(percentage, score)

    def render(self):
        rects = []

        return rects

    def tick(self, dt):
        pass

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or pygame.K_ESCAPE:
                # res.music("cut.ogg")
                self._game.remove_top_state()

    def init_render(self, percentage, score):
        self.screen.fill(gray)

        top_offset = 100

        headline = text_format("HIT RATE", percentage_font, 75, white)
        headline_rect = headline.get_rect()
        self.screen.blit(headline, (self._game.WIDTH / 2 - (headline_rect[2] / 2), top_offset + 5))

        if percentage >= 100.0:
            percentage_color = green
            comment = "Peach perfect!"
        elif percentage > 75.0:
            percentage_color = green
            comment = "Berry good!"
            comment_font_size = 200
        elif percentage > 50.0:
            percentage_color = yellow
            comment = "Almost bananas, try again!"
            comment_font_size = 100
        else:
            percentage_color = red
            comment = "Don't kiwi up!"
            comment_font_size = 200

        percentage_text = text_format(str(percentage) + "%", percentage_font, 200, percentage_color)
        percentage_text_rect = percentage_text.get_rect()
        self.screen.blit(percentage_text, (self._game.WIDTH / 2 - (percentage_text_rect[2] / 2), top_offset + 45))

        comment_text = text_format(comment, percentage_font, comment_font_size, percentage_color)
        comment_text_rect = comment_text.get_rect()
        self.screen.blit(comment_text, (self._game.WIDTH / 2 - (comment_text_rect[2] / 2), top_offset + 250))


