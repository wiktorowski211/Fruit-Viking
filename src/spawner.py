from src.targets.target import Target
from random import uniform, randrange
import pygame


# Cooldown is in seconds
class Spawner:
    def __init__(self, *, type, ammunition, initial_delay, cooldown, min_velocity, max_velocity, screen,
                 strategy_right: bool = False, debug: bool = False):
        self.type = type
        self.ammunition = ammunition
        self.cooldown = cooldown
        self.initial_delay = initial_delay
        self.timer = cooldown
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.strategy_right = strategy_right
        self.screen = screen
        self.debug = debug

        if not issubclass(self.type, Target):
            raise Exception('{} is not a proper target'.format(self.get_spawn_name()))

    def spawn(self):

        # decrease the ammunition count
        self.ammunition -= 1
        # decide the new target's parameters
        vel_x = uniform(self.min_velocity[0], self.max_velocity[0])
        vel_y = uniform(self.min_velocity[1], self.max_velocity[1])

        target = None
        screen_width, screen_height = pygame.display.get_surface().get_size()

        spawn_loc_y = randrange(int(screen_height * 0.2), int(screen_height * 0.7))
        spawn_loc_x = 0
        if self.strategy_right is True:
            spawn_loc_x = screen_width
            vel_x *= -1.0

        # spawn it
        target = self.type((spawn_loc_x, spawn_loc_y), self.screen, debug=self.debug)

        target.velocity = (vel_x, vel_y)
        return target

    def finished(self):
        if self.ammunition <= 0:
            return True
        return False

    def update(self, dt):
        # If it isn't supposed to spawn anything yet
        if self.initial_delay > 0.0:
            self.initial_delay -= dt
            return None

        self.timer += dt
        if self.timer >= self.cooldown:
            self.timer = 0
            return self.spawn()
        return None

    def get_spawn_name(self):
        return self.type.__name__.upper()
