from src.targets import *
from src.states import GameLevelState
from src.spawner import Spawner


def create_level_three(game):
    spawners = list()
    spawners.append(Spawner(spawn_type=Apple, ammunition=3, initial_delay=3.0, cooldown=2.0,
                            min_velocity=(200., -10.), max_velocity=(250., -40.), strategy_right=False))
    spawners.append(Spawner(spawn_type=Strawberry, ammunition=2, initial_delay=1.5, cooldown=3.0,
                            min_velocity=(300., -10.), max_velocity=(320., -40.), strategy_right=True))

    spawners.append(Spawner(spawn_type=Melon, ammunition=5, initial_delay=10., cooldown=1.0,
                            min_velocity=(150., -10.), max_velocity=(300., -40.), strategy_right=False))

    spawners.append(Spawner(spawn_type=Eggplant, ammunition=5, initial_delay=5., cooldown=.4,
                            min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False))

    spawners.append(Spawner(spawn_type=Pear, ammunition=4, initial_delay=14., cooldown=1.0,
                            min_velocity=(170., -10.), max_velocity=(270., -40.), strategy_right=True))

    spawners.append(Spawner(spawn_type=Cherry, ammunition=6, initial_delay=12., cooldown=.4,
                            min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False))

    spawners.append(Spawner(spawn_type=Banana, ammunition=4, initial_delay=20., cooldown=0.10,
                            min_velocity=(200., -10.), max_velocity=(300., -60.), strategy_right=True))

    spawners.append(Spawner(spawn_type=Banana, ammunition=4, initial_delay=20., cooldown=0.10,
                            min_velocity=(200., -10.), max_velocity=(300., -70.), strategy_right=False))

    return GameLevelState(game, spawners=spawners, start_timer=0.0, debug=False)
