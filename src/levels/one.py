from src.targets import *
from src.states import GameLevelState
from src.spawner import Spawner


def create_level_one(game):
    spawners = list()
    spawners.append(Spawner(spawn_type=Strawberry, ammunition=3, initial_delay=3.0, cooldown=2.0,
                            min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False,
                            screen=game.screen))
    spawners.append(Spawner(spawn_type=Strawberry, ammunition=6, initial_delay=1.5, cooldown=3.0,
                            min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=True,
                            screen=game.screen))
    spawners.append(Spawner(spawn_type=Tangerine, ammunition=5, initial_delay=10., cooldown=1.0,
                            min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False))

    spawners.append(Spawner(spawn_type=Kiwi, ammunition=10, initial_delay=20., cooldown=0.05,
                            min_velocity=(150., -10.), max_velocity=(240., -40.), strategy_right=True))

    spawners.append(Spawner(spawn_type=Kiwi, ammunition=10, initial_delay=20., cooldown=0.05,
                            min_velocity=(150., -10.), max_velocity=(240., -40.), strategy_right=False))

    spawners.append(Spawner(spawn_type=Pineapple, ammunition=5, initial_delay=5., cooldown=.4,
                            min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False))

    spawners.append(Spawner(spawn_type=Lemon, ammunition=4, initial_delay=14., cooldown=1.0,
                            min_velocity=(200., -10.), max_velocity=(240., -40.), strategy_right=True))

    spawners.append(Spawner(spawn_type=Grapes, ammunition=10, initial_delay=12., cooldown=.4,
                            min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False))

    spawners.append(Spawner(spawn_type=Apple, ammunition=1, initial_delay=0.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    return GameLevelState(game, spawners=spawners, start_timer=3.0, debug=False)
