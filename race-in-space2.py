class Track():
    def __init__(self):
        self._ship_list=[]
    def add_ship(self):
        self._ship_list.append(self)

class Ship():
    def __init__(self,nom,vitesse):
        self._vitesse=vitesse
        self._nom=nom
    def get_nom(self):
        return self._nom

course1=Track()
SShip1=Ship("baltazar1",15)
SShip2=Ship("baltazar2",5)
SShip3=Ship("baltazar3",2)
SShip4=Ship("baltazar4",20)
SShip5=Ship("baltazar5",8)

course1.add_ship()