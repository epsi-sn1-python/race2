class Pilot():
    def __init__(self,level):
        self._level=level
    def get_level(self):
        return self._level
class PilotNone(Pilot):
    def __init__(self):
        super().__init__(0)