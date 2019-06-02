from src.targets import *
from src.states import GameLevelState
from src.spawner import Spawner
from src.targets.peach import Peach
from src.targets.watermelon import Watermelon


def create_level_test(game):
    spawners = list()
    spawners.append(Spawner(spawn_type=Apple, ammunition=1, initial_delay=0.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Avocado, ammunition=1, initial_delay=1.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Banana, ammunition=1, initial_delay=2.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Cherry, ammunition=1, initial_delay=3.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Eggplant, ammunition=1, initial_delay=4.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Grapes, ammunition=1, initial_delay=5.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Kiwi, ammunition=1, initial_delay=6.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Lemon, ammunition=1, initial_delay=7.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Melon, ammunition=1, initial_delay=8.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Peach, ammunition=1, initial_delay=9.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Pear, ammunition=1, initial_delay=10.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Pineapple, ammunition=1, initial_delay=11.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Strawberry, ammunition=1, initial_delay=12.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Tangerine, ammunition=1, initial_delay=13.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))

    spawners.append(Spawner(spawn_type=Watermelon, ammunition=1, initial_delay=14.0, cooldown=0.05,
                            min_velocity=(100., -10.), max_velocity=(100., -40.), strategy_right=False,
                            screen=game.screen))


    return GameLevelState(game, spawners=spawners, start_timer=0.0, debug=True)
