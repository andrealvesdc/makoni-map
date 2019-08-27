import googlemaps
from datetime import datetime

class Map(object):
    def __init__(self,keymap):
        self.key=keymap
        if self.key != None:
            self.instance = googlemaps.Client(key=self.key)
            print("Instance created")