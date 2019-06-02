import pygame
import src.resources as res


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = res.gfx(image_file, convert=True)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)

    def render(self, screen):
        screen.blit(self.image, self.rect)
