
# Create the spawner
apple_spawner = Spawner(type=Apple, ammunition=3, initial_delay=3.0, cooldown=2.0,
                             min_velocity=(200., -10.), max_velocity=(250., -40.), strategy_right=False,
                             screen=self.screen)
strawberry_spawner = Spawner(type=Strawberry, ammunition=2, initial_delay=1.5, cooldown=3.0,
                              min_velocity=(300., -10.), max_velocity=(320., -40.), strategy_right=True,
                              screen=self.screen)

melon_spawner = Spawner(type=Melon, ammunition=5, initial_delay=10., cooldown=1.0,
                            min_velocity=(150., -10.), max_velocity=(300., -40.), strategy_right=False,
                            screen=self.screen)

eggplant_spawner = Spawner(type=Eggplant, ammunition=5, initial_delay=5., cooldown=.4,
                         min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False,
                         screen=self.screen)

pear_spawner = Spawner(type=Pear, ammunition=4, initial_delay=14., cooldown=1.0,
                         min_velocity=(170., -10.), max_velocity=(270., -40.), strategy_right=True,
                         screen=self.screen)

cherry_spawner = Spawner(type=Cherry, ammunition=6, initial_delay=12., cooldown=.4,
                            min_velocity=(190., -10.), max_velocity=(240., -40.), strategy_right=False,
                            screen=self.screen)

banana_spawner = Spawner(type=Banana, ammunition=4, initial_delay=20., cooldown=0.10,
                        min_velocity=(200., -10.), max_velocity=(300., -60.), strategy_right=True,
                        screen=self.screen)

banana_spawner2 = Spawner(type=Banana, ammunition=4, initial_delay=20., cooldown=0.10,
                       min_velocity=(200., -10.), max_velocity=(300., -70.), strategy_right=False,
                       screen=self.screen)

self.spawners = [apple_spawner, strawberry_spawner, melon_spawner, eggplant_spawner, pear_spawner, cherry_spawner, banana_spawner, banana_spawner2]
