class Track():
    def __init__(self,distance):
        self._distance=distance
        self._spaceship_list=[]
        self._winner=None
    def add_spaceship(self,spaceship):
        self._spaceship_list.append(spaceship)
    def start_race(self):
        self._winner= sorted(self._spaceship_list,key=lambda item:item.get_vitesse())[-1:]
    def get_winner(self):
        return self._winner

class SpaceShip():
    def __init__(self,nom,vitesse):
        self._vitesse=vitesse
        self._nom=nom
    def get_vitesse(self):
        return self._vitesse
    def __repr__(self):
        return f'{self._nom}:{self._vitesse} km/h'

track1=Track(2000)
SpaceShip1=SpaceShip(5,"SpaceS1")
SpaceShip2=SpaceShip(8,"SpaceS2")
SpaceShip3=SpaceShip(6,"SpaceS3")
SpaceShip4=SpaceShip(7,"SpaceS4")
SpaceShip5=SpaceShip(3,"SpaceS5")

track1.add_spaceship(SpaceShip1)
track1.add_spaceship(SpaceShip2)
track1.add_spaceship(SpaceShip3)
track1.add_spaceship(SpaceShip4)
track1.add_spaceship(SpaceShip5)

track1.start_race()
print(track1.get_winner())