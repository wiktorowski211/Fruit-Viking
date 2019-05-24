from .state import State
from src.util import text_format, circle_collision
from src.colors import gray, green, red, blue, white
import pygame


class TargetCircle:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
        self.color = red
        self.timer = 0.0

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def tick(self, dt, controller_pos, controller_radius):
        if circle_collision(controller_pos, self.pos , self.radius, controller_radius) is True:
            self.color = green
        else:
            self.color = red


class ControllerTestState(State):
    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)
        self.active = True
        self.text = text_format("AIM AT CIRCLES TILL THEY TURN GREEN ", 'Splatch.ttf', 45, green)
        self.escape = text_format("ESC TO GO BACK", 'Splatch.ttf', 20, white)

        self.controller_pos = (0, 0)

        self.last_controller_area = (0, 0, 0, 0)

        self.targets = []
        self.targets.append(TargetCircle((400, 400), 100))
        self.targets.append(TargetCircle((800, 500), 50))
        self.targets.append(TargetCircle((650, 350), 25))

    def render(self):

        rects = []

        text_rect = self.text.get_rect()
        escape_rect = self.escape.get_rect()

        self.screen.fill(gray)
        self.screen.blit(self.text, (self._game.WIDTH / 2 - (text_rect[2] / 2), 40))
        self.screen.blit(self.escape, (self._game.WIDTH / 2 - (escape_rect[2] / 2), 10))

        for t in self.targets:
            t.render(self.screen)

        draw_pointer = pygame.draw.circle(self.screen, blue, self.controller_pos, 10)

        rects.append(self.last_controller_area)
        rects.append(draw_pointer)

        self.last_controller_area = draw_pointer

        return rects

    def tick(self, dt):
        # plug controller here tuple of (x, y) that is in game's screen boundary
        img = self._game.camera.image()

        self.controller_pos = self._game.controller.get_position(img)

        self.controller_pos = pygame.mouse.get_pos()

        for t in self.targets:
            t.tick(dt, self.controller_pos, 10)
        #print(self.controller_pos)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Go back to level selection")
                self._game.remove_top_state()