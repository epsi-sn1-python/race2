from Pilots import PilotNone, Pilot

class SpaceShip():
    def __init__(self,speed=0,nom='',colour="white",width=0,height=0,brand="none"):
        self._speed=speed
        self._nom=nom
        self._colour=colour
        self._width=width
        self._height=height
        self._brand=brand
        self._pilot=PilotNone()
    def get_speed(self):
        return round(self._speed*self._pilot.get_level()/100,2)
    def get_colour(self):
        return self._colour
    def get_height(self):
        return self._height
    def get_width(self):
        return self._width
    def get_brand(self):
        return self._brand

    def add_pilot(self,pilot:Pilot):
        self._pilot=pilot

    def __repr__(self):
        return f'{self._nom}:{self._speed} km/h vaisseaux,{self.get_speed()} km/h pilote,{self._colour},{self._height},{self._width},{self._brand}\n'

    def __eq__(self, other):
        if self._speed >= other._speed:
            return True
        if self._colour == other._colour:
            return True
        if self._width == other._width:
            return True
        if self._height == other._height:
            return True
        if self._brand == other._brand:
            return True
        return False


#class fille(class mere):
'''cruiser decreseases the speed by 5%'''
class Cruiser(SpaceShip):
    def __init__(self,speed=0,nom='',color="white",width=0,height=0,brand="none"):
        super().__init__(round(speed*0.95,2),nom,color,width,height,brand)
'''fighter updrade the speed by 5%'''
class Fighter(SpaceShip):
    def __init__(self,speed=0,nom='',color="white",width=0,height=0,brand="none"):
        super().__init__(round(speed*1.05,2),nom,color,width,height,brand)