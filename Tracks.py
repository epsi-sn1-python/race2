class Track():
    def __init__(self, distance):
        self._distance=distance
        self._spaceship_list=[]
        self._winner=None
    def add_spaceship(self,spaceship):
        self._spaceship_list.append(spaceship)
    def start_race(self):
        self._winner= sorted(self._spaceship_list,key=lambda item:item.get_speed())[-1:]
    def get_winner(self):
        return self._winner