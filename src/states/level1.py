from src.targets.grapes import Grapes
from src.targets.kiwi import Kiwi
from src.targets.lemon import Lemon
from src.targets.pineapple import Pineapple
from .state import State
from src.targets import Strawberry, Tangerine
from src.colors import gray
from src.spawner import Spawner

import src.resources as res

import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def render(self, screen):
        screen.blit(self.image, self.rect)

class LevelState1(State):

    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)
        self.active = True

        self.targets = []

        self.background = Background('../media/background.jpg', [0, 0])

        # For rect cleanup
        self.deleteds_area = []

        # Scoring mechanisms
        self.score = 0
        self.hitnmiss = dict()
        self.start_timer = 3.0
        self.finish_timer = 2.0

        # Create the spawner
        strawberry_spawner = Spawner(type=Strawberry, ammunition=3, initial_delay=3.0, cooldown=2.0,
                                     min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False,
                                     screen=self.screen)
        strawberry_spawner2 = Spawner(type=Strawberry, ammunition=6, initial_delay=1.5, cooldown=3.0,
                                      min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=True,
                                      screen=self.screen)
        tangerine_spawner = Spawner(type=Tangerine, ammunition=5, initial_delay=10., cooldown=1.0,
                                    min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False,
                                    screen=self.screen)

        kiwi_spawner = Spawner(type=Kiwi, ammunition=10, initial_delay=20., cooldown=0.05,
                                min_velocity=(150., -10.), max_velocity=(240., -40.), strategy_right=True,
                                screen=self.screen)

        kiwi_spawner2 = Spawner(type=Kiwi, ammunition=10, initial_delay=20., cooldown=0.05,
                               min_velocity=(150., -10.), max_velocity=(240., -40.), strategy_right=False,
                               screen=self.screen)

        pineapple_spawner = Spawner(type=Pineapple, ammunition=5, initial_delay=5., cooldown=.4,
                                 min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False,
                                 screen=self.screen)

        lemon_spawner = Spawner(type=Lemon, ammunition=4, initial_delay=14., cooldown=1.0,
                                 min_velocity=(200., -10.), max_velocity=(240., -40.), strategy_right=True,
                                 screen=self.screen)

        grapes_spawner = Spawner(type=Grapes, ammunition=10, initial_delay=12., cooldown=.4,
                                    min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False,
                                    screen=self.screen)

        self.spawners = [strawberry_spawner, strawberry_spawner2, tangerine_spawner, lemon_spawner, grapes_spawner, kiwi_spawner, kiwi_spawner2, pineapple_spawner]
        res.music("metin.ogg")
        for s in self.spawners:
            self.hitnmiss[s.get_spawn_name()] = {"hits": 0, "misses": 0}

    def render(self):
        rects = [] + self.deleteds_area

        self.deleteds_area.clear()

        # self.screen.fill(gray)


        # self.screen.fill([255, 255, 255])
        self.background.render(self.screen)

        for target in self.targets:
            rect_a, rect_b = target.render()
            rects.append(rect_a)
            rects.append(rect_b)

        old_controller_area, new_controller_area = self._game.controller.render(self.screen)
        rects.append(old_controller_area)
        rects.append(new_controller_area)
        return rects

    def tick(self, dt):
        self.start_timer -= dt
        if self.start_timer >= 0:
            return
        self.update_spawners(dt)
        self.update_targets(dt)
        self.check_for_stage_end(dt)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Go back to level selection")
                res.music("loser.ogg", True, True)
                self._game.remove_top_state()

    def update_spawners(self, dt):
        # Check if anything spawned
        finished_spawners = []
        for i, spawner in enumerate(self.spawners):
            new_target = spawner.update(dt)
            if spawner.finished() is True:
                finished_spawners.append(i)
            if new_target is not None:
                self.targets.append(new_target)

        # Delete finished spawners
        for index in finished_spawners[::-1]:
            del self.spawners[index]

    def update_targets(self, dt):
        # Update controller position
        controller_pos = self._game.controller.update_position()

        # Update targets
        marked_for_delete = []
        for i, target in enumerate(self.targets):
            # Apply gravity
            target.velocity = target.velocity[0], target.velocity[1] + 20. * dt

            # Update target
            target.update(dt, controller_pos, self._game.controller.radius)
            if target.defeated is True:
                self.hitnmiss[target.__class__.__name__.upper()]["hits"] += 1
                # print("Killed berry")
                res.sfx("cut.ogg", True)
                marked_for_delete.append(i)
                self.deleteds_area.append(target.last_area)
            elif target.left_screen is True:
                self.hitnmiss[target.__class__.__name__.upper()]["misses"] += 1
                # print("Deleted out of screen berry")
                marked_for_delete.append(i)
                self.deleteds_area.append(target.last_area)

        # Delete dead targets
        for index in marked_for_delete[::-1]:
            del self.targets[index]

    def check_for_stage_end(self, dt):
        if len(self.spawners) + len(self.targets) == 0:
            self.finish_timer -= dt
            if self.finish_timer <= 0:
                res.music("end.ogg", True, True)
                print(self.hitnmiss)
                self._game.remove_top_state()
