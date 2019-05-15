import os
import pygame

from image_processing.camera import Camera
from image_processing.tracker import Tracker
from src.state_types import States
from src.states import ControllerTestState
from src.states import MenuState


class Game:
    WIDTH = 1280
    HEIGHT = 720
    FPS = 30

    def __init__(self):
        # Game Initialization
        pygame.init()
        pygame.font.init()

        # Center the Game Application
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Game Resolution
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Add caption
        pygame.display.set_caption("Fruit Viking")

        # Initialize the clock
        self.clock = pygame.time.Clock()

        # Game states
        self.states = [MenuState(self)]

        # Game is running
        self.running = True

        self.camera = Camera(1280, 720)

        self.controller = Tracker()


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
        for i in self.states[::-1]:
            if i.active:
                if not i.render():
                    break
                if not getattr(i, 'propagate_render', False):
                    break
        pygame.display.flip()

    def events(self, events):
        """
        :param events:
        :return: Nothing
        Procedure that propagates events to active states of the game, starting from the ones on top.
        Stops on inactive state.
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            for i in self.states[::-1]:
                if i.active:
                    if not i.event(event):
                        break

    def push_state(self, state):
        if not isinstance(state, States):
            raise Exception('{} is not a proper state'.format(state))
        if States.CONTROLLER_TEST == state:
            self.states.append(ControllerTestState(self))
            return
        if States.MENU == state:
            self.states.append(MenuState(self))
            return
        raise Exception('{} is not getting pushed properly'.format(state))

    def mainloop(self):
        """
        Main loop of the game
        """

        while self.running:
            dt = self.clock.tick(self.FPS) / 1000.0
            self.tick(dt)
            self.render()
            events = pygame.event.get()
            self.events(events)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.mainloop()

    quit()
