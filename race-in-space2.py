from Tracks import Track
from Pilots import Pilot
from Garages import Garage
from SpaceShips import SpaceShip,Cruiser,Fighter
  
if __name__=='__main__':
    track1=Track(2000)
    SpaceShip1=Cruiser(5,"SpaceS1")
    SpaceShip2=Fighter(8,"SpaceS2")
    SpaceShip3=Cruiser(6,"SpaceS3")
    SpaceShip4=Cruiser(7,"SpaceS4")
    SpaceShip5=Fighter(3,"SpaceS5")

    han_solo=Pilot(70)
    anakin=Pilot(90)
    chewbacca=Pilot(45)

    SpaceShip1.add_pilot(han_solo)
    SpaceShip2.add_pilot(anakin)
    SpaceShip3.add_pilot(chewbacca)

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

    track1.start_race()
    print(f' winner is {track1.get_winner()}')

    spaceship_wanted=SpaceShip(speed=8,colour='red')
    print(f'Spaceship wanted: {spaceship_wanted}')
    result=garage.search(spaceship_wanted)
    print(result)