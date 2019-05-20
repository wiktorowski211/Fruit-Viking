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
        blit_rotate(screen, self.img, self.pos, (w / 2, h / 2), self.angle)


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

        title_rect = self.title.get_rect()
        start_rect = self.text_start.get_rect()
        quit_rect = self.text_quit.get_rect()

        self.screen.fill(gray)

        # Main Menu Text
        self.screen.blit(self.title, (self._game.WIDTH / 2 - (title_rect[2] / 2), 80))
        self.screen.blit(self.text_start, (self._game.WIDTH / 2 - (start_rect[2] / 2), 300))
        self.screen.blit(self.text_quit, (self._game.WIDTH / 2 - (quit_rect[2] / 2), 480))

        # Banana
        self.banana.render(self.screen)

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
        self._game.push_state(States.CONTROLLER_TEST)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = "start"
            elif event.key == pygame.K_DOWN:
                self.selected = "quit"
            if event.key == pygame.K_RETURN:
                if self.selected == "start":
                    self.start_game()
                if self.selected == "quit":
                    self._game.running = False
