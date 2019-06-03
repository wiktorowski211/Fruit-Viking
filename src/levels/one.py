from src.targets import *
from src.states import GameLevelState
from src.spawner import Spawner


def create_level_one(game):
    spawners = list()
    spawners.append(Spawner(spawn_type=Strawberry, ammunition=3, initial_delay=3.0, cooldown=2.0,
                             min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False))
    spawners.append(Spawner(spawn_type=Strawberry, ammunition=6, initial_delay=1.5, cooldown=3.0,
                              min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=True))
    spawners.append(Spawner(spawn_type=Tangerine, ammunition=5, initial_delay=10., cooldown=1.0,
                            min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False))

    return GameLevelState(game, spawners=spawners, start_timer=3.0, debug=False)
