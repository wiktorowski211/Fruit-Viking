# Create the spawner
banana_spawner1 = Spawner(type=Banana, ammunition=3, initial_delay=1., cooldown=1.0,
                        min_velocity=(250., -10.), max_velocity=(300., -40.), strategy_right=False,
                        screen=self.screen)

banana_spawner2 = Spawner(type=Banana, ammunition=5, initial_delay=3., cooldown=0.10,
                         min_velocity=(270., -10.), max_velocity=(310., -60.), strategy_right=True,
                         screen=self.screen)

banana_spawner3 = Spawner(type=Banana, ammunition=5, initial_delay=4., cooldown=0.10,
                          min_velocity=(270., -10.), max_velocity=(310., -70.), strategy_right=False,
                          screen=self.screen)

banana_spawner4 = Spawner(type=Banana, ammunition=3, initial_delay=6., cooldown=2.0,
                          min_velocity=(270., -10.), max_velocity=(310., -40.), strategy_right=False,
                          screen=self.screen)

banana_spawner5 = Spawner(type=Banana, ammunition=4, initial_delay=10., cooldown=0.5,
                          min_velocity=(250., -10.), max_velocity=(300., -60.), strategy_right=True,
                          screen=self.screen)

banana_spawner6 = Spawner(type=Banana, ammunition=6, initial_delay=12., cooldown=0.5,
                          min_velocity=(250., -10.), max_velocity=(300., -70.), strategy_right=False,
                          screen=self.screen)

banana_spawner7 = Spawner(type=Banana, ammunition=1, initial_delay=19., cooldown=2.0,
                          min_velocity=(300., -10.), max_velocity=(400., -40.), strategy_right=False,
                          screen=self.screen)

banana_spawner8 = Spawner(type=Banana, ammunition=15, initial_delay=19., cooldown=0.05,
                          min_velocity=(380., -10.), max_velocity=(450., -100.), strategy_right=True,
                          screen=self.screen)

banana_spawner9 = Spawner(type=Banana, ammunition=15, initial_delay=19., cooldown=0.05,
                          min_velocity=(380., -10.), max_velocity=(450., -100.), strategy_right=False,
                          screen=self.screen)

self.spawners = [banana_spawner1, banana_spawner2, banana_spawner3, banana_spawner4, banana_spawner5, banana_spawner6, banana_spawner7, banana_spawner8, banana_spawner9]
