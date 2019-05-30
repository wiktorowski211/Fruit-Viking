from .state import State

import src.resources as res

import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = res.gfx(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)

    def render(self, screen):
        screen.blit(self.image, self.rect)


class GameLevelState(State):

    def __init__(self, *args, spawners=[], targets=[], debug: bool = False, start_timer: float = 1.0,
                 finish_timer: float = 3.0, music='metin.ogg', background='background.jpg', **kwargs):
        State.__init__(self, *args, **kwargs)
        self.active = True

        self.targets = targets.copy()

        self.background = Background(background)

        # For rect cleanup
        self.deleteds_area = list()

        # Scoring mechanisms
        self.score = 0
        self.hitnmiss = dict()
        self.finish_timer = finish_timer
        self.spawners = spawners.copy()

        for spawner in self.spawners:
            spawner.debug = debug
            # force stage start delay by adding the initial wait to spawners
            spawner.initial_delay += start_timer

        res.music(music)
        for s in self.spawners:
            self.hitnmiss[s.get_spawn_name()] = {"hits": 0, "misses": 0}

    def render(self):
        rects = list() + self.deleteds_area

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
        finished_spawners = list()
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
        marked_for_delete = list()
        for i, target in enumerate(self.targets):
            # Apply gravity
            target.velocity = target.velocity[0], target.velocity[1] + 20. * dt

            # Update target
            target.update(dt, controller_pos, self._game.controller.radius)
            if target.defeated is True:
                self.hitnmiss[target.__class__.__name__]["hits"] += 1
                # print("Killed berry")
                res.sfx("cut.ogg", True)
                marked_for_delete.append(i)
                self.deleteds_area.append(target.last_area)
            elif target.left_screen is True:
                self.hitnmiss[target.__class__.__name__]["misses"] += 1
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
