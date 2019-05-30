# Create the spawner
strawberry_spawner = Spawner(type=Strawberry, ammunition=6, initial_delay=3.0, cooldown=2.0,
                             min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False,
                             screen=self.screen)
strawberry_spawner2 = Spawner(type=Strawberry, ammunition=6, initial_delay=1.5, cooldown=3.0,
                              min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=True,
                              screen=self.screen)
tangerine_spawner = Spawner(type=Tangerine, ammunition=5, initial_delay=10., cooldown=1.0,
                            min_velocity=(160., -10.), max_velocity=(200., -40.), strategy_right=False,
                            screen=self.screen)

pineapple_spawner = Spawner(type=Pineapple, ammunition=5, initial_delay=5., cooldown=.4,
                         min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False,
                         screen=self.screen)

lemon_spawner = Spawner(type=Lemon, ammunition=4, initial_delay=14., cooldown=1.0,
                         min_velocity=(200., -10.), max_velocity=(240., -40.), strategy_right=True,
                         screen=self.screen)

grapes_spawner = Spawner(type=Grapes, ammunition=6, initial_delay=12., cooldown=.4,
                            min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False,
                            screen=self.screen)

kiwi_spawner = Spawner(type=Kiwi, ammunition=10, initial_delay=20., cooldown=0.05,
                        min_velocity=(150., -10.), max_velocity=(240., -40.), strategy_right=True,
                        screen=self.screen)

kiwi_spawner2 = Spawner(type=Kiwi, ammunition=10, initial_delay=20., cooldown=0.05,
                       min_velocity=(150., -10.), max_velocity=(240., -40.), strategy_right=False,
                       screen=self.screen)

self.spawners = [strawberry_spawner, strawberry_spawner2, tangerine_spawner, lemon_spawner, grapes_spawner, kiwi_spawner, kiwi_spawner2, pineapple_spawner]