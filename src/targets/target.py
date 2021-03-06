import pygame
from src.colors import green, red
from src.util import circle_collision


class Target:
    def __init__(self, image, pos, screen, debug: bool = False):
        self.img = image
        self.pos = pos
        self.real_pos = pos
        self.screen = screen
        self.velocity = (0, 0)
        self.offset = (0, 0)

        w, _h = image.get_size()
        self.radius = int(w / 2.75)

        self.last_area = 0
        self.current_area = self.screen.blit(self.img, (self.pos[0] + self.radius, self.pos[1] + self.radius))

        # For tracking if target should get killed
        self.under_cursor = False
        self.defeated = False
        self.left_screen = False

        self.debug = debug
        if debug is True:
            self.color = red

    def update(self, dt, controller_pos, controller_radius) -> bool:
        # Update the last drawn area to previous frame's current
        self.last_area = self.current_area

        # Move the body
        pos_x = self.real_pos[0] + self.velocity[0] * dt
        pos_y = self.real_pos[1] + self.velocity[1] * dt

        self.real_pos = pos_x, pos_y
        self.pos = int(pos_x), int(pos_y)

        # When it goes out of screen
        self.out_of_screen()

        # When collision occurs
        if circle_collision(controller_pos, self.pos, self.radius, controller_radius) is True:
            self.color = green
            self.under_cursor = True
            return True
        self.color = red

        # If it already collided previously
        if self.under_cursor is True:
            self.defeated = True

        return False

    def render(self):
        if self.debug is True:
            pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
        blit_x_pos = self.pos[0] - self.radius - self.offset[0]
        blit_y_pos = self.pos[1] - self.radius - self.offset[1]
        self.current_area = self.screen.blit(self.img, (blit_x_pos, blit_y_pos))

        return self.last_area, self.current_area

    def out_of_screen(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        if self.pos[0] > screen_width + self.radius * 3 or self.pos[0] < - self.radius * 3:
            self.left_screen = True
        if self.pos[1] > screen_height + self.radius * 3 or self.pos[1] < - self.radius * 3:
            self.left_screen = True

    def get_pos(self):
        return self.pos[0] - self.radius - self.offset[0], self.pos[1] - self.radius - self.offset[1]

    def on_defeat(self, targets):
        pass

    # If the target is supposed to be sliced
    @staticmethod
    def is_fruit():
        return True

    @staticmethod
    def get_image():
        pass
