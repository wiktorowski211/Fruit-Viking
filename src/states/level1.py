from .state import State
from src.targets import Strawberry
from src.colors import gray
from src.spawner import Spawner, FruitType
import pygame


class LevelState1(State):

    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)
        self.active = True

        target1 = Strawberry((200, 200), self.screen, True)

        target2 = Strawberry((300, 300), self.screen, True)

        self.targets = [target2]
        self.targets.append(target1)

        # For rect cleanup
        self.deleteds_area = []

        self.score = 0

        # Create the spawner
        strawberry_spawner = Spawner(FruitType.STRAWBERRY, 3, 3.5, (160., -10.), (200., -40.), self.screen)
        self.spawners = [strawberry_spawner]

    def render(self):
        rects = [] + self.deleteds_area

        self.deleteds_area.clear()

        self.screen.fill(gray)
        for target in self.targets:
            rect_a, rect_b = target.render()
            rects.append(rect_a)
            rects.append(rect_b)

        return rects

    def tick(self, dt):
        # Check if anything spawned
        finished_spawners = []
        for i, spawner in enumerate(self.spawners):
            new_target = spawner.update(dt)
            if spawner.finished() is True:
                finished_spawners.append(i)
            if new_target  is not None:
                self.targets.append(new_target)

        # Update targets
        marked_for_delete = []
        for i, target in enumerate(self.targets):
            # Apply gravity
            target.velocity = target.velocity[0], target.velocity[1] + 20. * dt

            # Update target
            target.update(dt, (300, 300), 1)
            if target.defeated is True:
                marked_for_delete.append(i)
                self.deleteds_area.append(target.last_area)
        # TODO: Delete off screen targets
        # Delete dead targets
        for index in marked_for_delete[::-1]:
            del self.targets[index]

        # Delete finished spawners
        for index in finished_spawners[::-1]:
            del self.spawners[index]


    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Go back to level selection")
                self._game.remove_top_state()
