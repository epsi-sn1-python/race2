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

class SpaceShip():
    def __init__(self,speed=0,nom='',colour="white",width=0,height=0,brand="none"):
        self._speed=speed
        self._nom=nom
        self._colour=colour
        self._width=width
        self._height=height
        self._brand=brand
    def get_speed(self):
        return self._speed
    def get_colour(self):
        return self._colour
    def get_height(self):
        return self._height
    def get_width(self):
        return self._width
    def get_brand(self):
        return self._brand

    def __repr__(self):
        return f'{self._nom}:{self._speed} km/h,{self._colour},{self._height},{self._width},{self._brand}'

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

class Garage():
    def __init__(self,max_size):
        self._max_size=max_size
        self._spaceship_list=[]

    def add_spaceship(self,spaceship):
        if len(self._spaceship_list)<self._max_size:
            self._spaceship_list.append(spaceship)
        else :
            return "le garage est plein"

    # def search(self,speed,colour,height,width,brand):
    #     resultat=[]
    #     for elt in self._spaceship_list:
    #         if elt.get_speed()==speed:
    #             resultat.append(elt)
    #             continue
    #         if elt.get_colour()==colour:
    #             resultat.append(elt)
    #             continue
    #         if elt.get_height()==height:
    #             resultat.append(elt)
    #             continue
    #         if elt.get_width()==width:
    #             resultat.append(elt)
    #             continue
    #         if elt.get_brand()==brand:
    #             resultat.append(elt)
    #             continue
    #     return resultat

    def search(self,spaceship_wanted):
        result=[]
        for elt in self._spaceship_list:
            if elt==spaceship_wanted:
                result.append(elt)
        return result


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

garage=Garage(12)
garage.add_spaceship(SpaceShip1)
garage.add_spaceship(SpaceShip2)
garage.add_spaceship(SpaceShip3)
garage.add_spaceship(SpaceShip4)
garage.add_spaceship(SpaceShip5)

# track1.start_race()
# print(track1.get_winner())

spaceship_wanted=SpaceShip(speed=8,colour='red')
print(f'Spaceship wanted: {spaceship_wanted}')
result=garage.search(spaceship_wanted)
print(result)