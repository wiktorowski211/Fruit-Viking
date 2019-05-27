from src.targets import  Strawberry
from enum import Enum, auto
from random import uniform, randrange
import pygame

class FruitType(Enum):
    STRAWBERRY = auto()


# Cooldown is in seconds
class Spawner:
    def __init__(self, type, ammunition, cooldown, min_velocity, max_velocity, screen):
        self.type = type
        self.ammunition = ammunition
        self.cooldown = cooldown
        self.timer = cooldown
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.side = "left"
        self.screen = screen

    def spawn(self):
        if not isinstance(self.type, FruitType):
            raise Exception('{} is not a proper state'.format(self.type))
        # decrease the ammunition count
        self.ammunition -= 1
        # decide the new target's parameters
        vel_x = uniform(self.min_velocity[0], self.max_velocity[0])
        vel_y = uniform(self.min_velocity[1], self.max_velocity[1])

        target = None
        screen_width, screen_height = pygame.display.get_surface().get_size()

        spawn_loc_y = randrange(int(screen_height*0.2), int(screen_height*0.7))
        # spawn it
        if FruitType.STRAWBERRY == self.type:
            target = Strawberry((0, spawn_loc_y), self.screen)

        target.velocity = (vel_x, vel_y)
        return target

    def finished(self):
        if self.ammunition <= 0:
            return True
        return False

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.cooldown:
            self.timer = 0
            return self.spawn()
        return None
