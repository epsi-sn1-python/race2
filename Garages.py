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