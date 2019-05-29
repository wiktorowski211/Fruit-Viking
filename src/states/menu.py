from .state import State

import pygame
from pygame.sprite import DirtySprite

import src.resources as res

from src.util import text_format, blit_rotate
from src.colors import yellow, white, black, gray

from src.state_types import States

# Menu Fonts
main_font = "Splatch.ttf"


class Banana(DirtySprite):
    def __init__(self, pos):
        DirtySprite.__init__(self)
        self.pos = pos

        banana = res.gfx('Banana_happy.png', convert_alpha=True)
        banana = pygame.transform.scale(banana, (256, 256))

        self.img = pygame.transform.scale(banana, (256, 256))
        self.angle = 0

    def update(self, dt):
        self.dirty = 1

        self.angle += 180 * dt

        if self.angle > 360:
            self.angle -= 360

    def render(self, screen):
        w, h = self.img.get_size()
        return blit_rotate(screen, self.img, self.pos, (w / 2, h / 2), self.angle)


class MenuState(State):
    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)

        # Menu should be always active
        self.active = True

        # The text
        self.title = text_format("<FRUIT VIKING>", main_font, 90, yellow)
        self.text_start = text_format("START", main_font, 75, white)
        self.text_quit = text_format("QUIT", main_font, 75, black)
        self.selected = "start"

        # The elusive banana
        banana_pos = (250, 450)

        self.banana = Banana(banana_pos)

    def render(self):

        rects = []

        title_rect = self.title.get_rect()
        start_rect = self.text_start.get_rect()
        quit_rect = self.text_quit.get_rect()

        self.screen.fill(gray)

        # Main Menu Text
        self.screen.blit(self.title, (self._game.WIDTH / 2 - (title_rect[2] / 2), 80))
        draw_start = self.screen.blit(self.text_start, (self._game.WIDTH / 2 - (start_rect[2] / 2), 300))
        draw_quit = self.screen.blit(self.text_quit, (self._game.WIDTH / 2 - (quit_rect[2] / 2), 480))

        # Banana
        draw_banana = self.banana.render(self.screen)
        rects.append(draw_banana)
        rects.append(draw_start)
        rects.append(draw_quit)

        return rects

    def tick(self, dt):
        if self.selected == "start":
            self.text_start = text_format("START", main_font, 75, white)
        else:
            self.text_start = text_format("START", main_font, 75, black)
        if self.selected == "quit":
            self.text_quit = text_format("QUIT", main_font, 75, white)
        else:
            self.text_quit = text_format("QUIT", main_font, 75, black)

        # Banana
        self.banana.update(dt)

    def start_game(self):
        print("Start")
        self._game.push_state(States.LEVEL_SELECTION)

    def event(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                res.sfx("menumove.ogg", True)
                self.selected = "start"
            elif event.key == pygame.K_DOWN:
                res.sfx("menumove.ogg", True)
                self.selected = "quit"
            if event.key == pygame.K_RETURN:
                if self.selected == "start":
                    self.start_game()
                    res.sfx("cut.ogg", True)
                if self.selected == "quit":
                    self._game.running = False
