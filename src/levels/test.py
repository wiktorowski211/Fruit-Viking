from src.targets import *
from src.states import GameLevelState
from src.spawner import Spawner


def create_level_test(game):
    spawners = list()
    spawners.append(Spawner(spawn_type=Pineapple, ammunition=20, initial_delay=0.0, cooldown=0.05,
                            min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False,
                            screen=game.screen))

    return GameLevelState(game, spawners=spawners, start_timer=0.0, debug=True)
