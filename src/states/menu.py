from .state import State

import pygame
from pygame.sprite import DirtySprite


# Text Renderer
def text_format(message, text_font, text_size, text_color):
    new_font = pygame.font.Font(text_font, text_size)
    new_text = new_font.render(message, 0, text_color)

    return new_text


def blit_rotate(surf, image, pos, origin_pos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot = pygame.math.Vector2(origin_pos[0], -origin_pos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - origin_pos[0] + min_box[0] - pivot_move[0], pos[1] - origin_pos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

    # draw rectangle around the image
    #pygame.draw.rect (surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


# Game Fonts
font = "../media/Splatch.ttf"

# TODO: The mysterious banana should be a resource, like pretty much all the things above
banana_img = "../media/Banana_happy.png"


class Banana(DirtySprite):
    def __init__(self, pos):
        DirtySprite.__init__(self)
        self.pos = pos

        banana = pygame.image.load(banana_img).convert_alpha()
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
        self.title = text_format("<FRUIT VIKING>", font, 90, yellow)
        self.text_start = text_format("START", font, 75, white)
        self.text_quit = text_format("QUIT", font, 75, black)
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
            self.text_start = text_format("START", font, 75, white)
        else:
            self.text_start = text_format("START", font, 75, black)
        if self.selected == "quit":
            self.text_quit = text_format("QUIT", font, 75, white)
        else:
            self.text_quit = text_format("QUIT", font, 75, black)

        # Banana
        self.banana.update(dt)

    def start_game(self):
        print("Start")

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
