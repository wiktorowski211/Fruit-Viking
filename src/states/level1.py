from .state import State


class LevelState1:

    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)
        self.active = True


    def render(self):
        pass

    def tick(self, dt):
        pass

    def event(self, event):
        pass
