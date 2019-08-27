import googlemaps
from datetime import datetime

class Map(object):
    # generate only instance of google maps;
    def __init__(self,keymap):
        self.key=keymap
        if self.key != None:
            self.instance = googlemaps.Client(key=self.key)
            print("Instance created")

    # return json informations of adress searching.
    # Json response attributes: 
    # lat,long - city,state, short_name = CEP
    #formated adress: full;
    def geocode(self,adress):
        if self.instance != None:
            result = self.instance.geocode(adress)
            return result
    
