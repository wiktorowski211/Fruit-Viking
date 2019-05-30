from .state import State

import pygame
import src.resources as res

from src.util import text_format
from src.colors import yellow, white, black, gray

from src.state_types import States
from enum import Enum

# Visual idea: make fruits appear on the left of menu and hover downwards, reverse on right

# Menu Fonts
main_font = "Splatch.ttf"


class MenuMovement(Enum):
    NONE = 0
    UP = 1
    DOWN = 2


class MenuOption:
    def __init__(self, text, size, screen_width, text_height, transition):
        # Required for text redrawing
        self.text = text
        self.size = size
        self.surface = text_format(text, main_font, size, black)
        surface_rect = self.surface.get_rect()
        self.position = (screen_width / 2 - (surface_rect[2] / 2), text_height)

        # Required to determine where the button leads
        self.transition = transition

    def render(self, screen):
        return screen.blit(self.surface, self.position)

    def activate(self):
        self.surface = text_format(self.text, main_font, self.size, white)

    def deactivate(self):
        self.surface = text_format(self.text, main_font, self.size, black)

    def press(self):
        # On press give the information where pressing enter should lead
        return self.transition


class LevelSelectionState(State):
    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)

        # Menu should be always active
        self.active = True

        # Which way the menu will move
        self.menu_movement = MenuMovement.NONE

        # Create a menu, could be it's own class
        self.menu = []
        self.menu_pos = 0

        self.menu.append(MenuOption("LEVEL 1", 60, self._game.WIDTH, 180, States.LEVEL1))
        self.menu.append(MenuOption("LEVEL 2", 60, self._game.WIDTH, 280, States.LEVEL2))
        self.menu.append(MenuOption("CAMERA TEST", 60, self._game.WIDTH, 600, States.CONTROLLER_TEST))
        # Activate a menu item
        self.menu[0].activate()

    def render(self):
        rects = []
        self.screen.fill(gray)

        for option in self.menu:
            rects.append(option.render(self.screen))

        return rects

    def tick(self, dt):
        if self.menu_movement == MenuMovement.DOWN:
            self.menu[self.menu_pos].deactivate()
            self.menu_pos += 1
            if self.menu_pos >= len(self.menu):
                self.menu_pos = 0
            self.menu[self.menu_pos].activate()
        elif self.menu_movement == MenuMovement.UP:
            self.menu[self.menu_pos].deactivate()
            self.menu_pos -= 1
            if self.menu_pos < 0:
                self.menu_pos = len(self.menu) - 1
            self.menu[self.menu_pos].activate()
        self.menu_movement = MenuMovement.NONE

    def select_level(self):
        print("Selected a level")
        res.music("start.ogg")
        self._game.push_state(self.menu[self.menu_pos].press())

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                res.music("menumove.ogg")
                self.menu_movement = MenuMovement.UP
            elif event.key == pygame.K_DOWN:
                res.music("menumove.ogg")
                self.menu_movement = MenuMovement.DOWN
            if event.key == pygame.K_RETURN:
                res.music("cut.ogg")
                self.select_level()
            if event.key == pygame.K_ESCAPE:
                print("Go back to menu")
                res.music("back.ogg")
                self._game.remove_top_state()
