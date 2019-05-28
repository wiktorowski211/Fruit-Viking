import os
import pygame

from src.state_types import States
# Import all possible states
from src.states import *
# Change controller here
from src.controller import CameraController as UsedController


class Game:
    WIDTH = 1280
    HEIGHT = 720
    FPS = 30

    def __init__(self):
        # Game Initialization
        pygame.init()
        pygame.font.init()
        # Pygame uses SDL 1.2...!
        print(pygame.get_sdl_version())

        # Center the Game Application
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Game Resolution
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Add caption
        pygame.display.set_caption("Fruit Viking")

        # Initialize the clock
        self.clock = pygame.time.Clock()

        #
        self.state_change = True

        # Game states
        self.states = [MenuState(self)]

        # Game is running
        self.running = True

        self.controller = UsedController()

    def tick(self, dt):
        """
        :param dt: Timestep of the current frame
        :return: Nothing

        Procedure that updates active states of the game, starting from the ones on top.
        Stops on inactive state.
        """

        for i in self.states[::-1]:
            if i.active:
                if not i.tick(dt):
                    break

    def render(self):
        """
        :return: Nothing
        Procedure that draws active states of the game, starting from the ones on top.
        Stops on inactive state or if state doesn't wish to propagate further.
        """
        draw_rects = []
        if self.state_change is True:
            draw_rects.append((0, 0, self.WIDTH, self.HEIGHT))
            self.state_change = False
        for i in self.states[::-1]:
            if i.active:
                rects = i.render()
                if rects is not None:
                    draw_rects.extend(rects)
                if not getattr(i, 'propagate_render', False):
                    break
        #pygame.display.flip()
        pygame.display.update(draw_rects)

    def events(self, events):
        """
        :param events:
        :return: Nothing
        Procedure that propagates events to active states of the game, starting from the ones on top.
        Stops on inactive state.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F12:
                    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
                    self.state_change = True
                if event.key == pygame.K_F10:
                    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
                    self.state_change = True

            if event.type == pygame.QUIT:
                self.running = False

            for i in self.states[::-1]:
                if i.active:
                    if not i.event(event):
                        break

    def push_state(self, state):
        if not isinstance(state, States):
            raise Exception('{} is not a proper state'.format(state))
        self.state_change = True
        self.states[-1].active = False
        if States.CONTROLLER_TEST == state:
            self.states.append(ControllerTestState(self))
            return
        if States.MENU == state:
            self.states.append(MenuState(self))
            return
        if States.LEVEL_SELECTION == state:
            self.states.append(LevelSelectionState(self))
            return
        if States.LEVEL1 == state:
            self.states.append(LevelState1(self))
            return
        raise Exception('{} is not getting pushed properly'.format(state))

    def remove_top_state(self):
        self.states.pop()
        self.state_change = True
        self.states[-1].active = True

    def mainloop(self):
        """
        Main loop of the game
        """
        counter = 0
        time_elapsed = 0.0
        while self.running:
            time = self.clock.tick(self.FPS)
            dt = time / 1000.0
            #print(dt)
            time_elapsed += dt
            if time_elapsed >= 2.0 and counter > 0:
                print("FPS: " + str(counter/2))
                time_elapsed -= 2.0
                counter = 0
            counter += 1
            self.tick(dt)
            self.render()
            events = pygame.event.get()
            self.events(events)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.mainloop()

    quit()
