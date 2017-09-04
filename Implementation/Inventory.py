"""
Class Inventory contains a set of objects belonging to a player and methods to manipulate and check them.
"""

# local imports
from Implementation import Constants


class Inventory:
    """
    Think about placing the resources in an array with references to the index as dictionary e.g.:
    self.resources_arr = [self.b, self.l, self.w, self.g, self.o]
    This way we can make a dictionary referring to the object that needs to be built and when passed
    to the add_object method subtract from the array of resources based on the dictionary reference passed
    to the method e.g.:

    def add_object(self, self.resources_arr, object_to_add):
        if object_to_add == ROAD:
            if has_road(self):
                self.resources_arr[self.b] = self.resources_arr[self.b -1]
                self.resources_arr[self.l] = self.resources_arr[self.l -1]
                self.roads.append(road)
        if object_to_add == SETTLEMENT:
            if has_settlement(self):
                self.resources_arr[self.b] = self.resources_arr[self.b -1]
                self.resources_arr[self.l] = self.resources_arr[self.l -1]
                self.resources_arr[self.w] = self.resources_arr[self.w -1]
                self.resources_arr[self.g] = self.resources_arr[self.g -1]
                self.settlesments.append(settlement)
        if object_to_add == CITY:
            if has_city(self):
                self.resources_arr[self.g] = self.resources_arr[self.g -2]
                self.resources_arr[self.o] = self.resources_arr[self.o -3]
        if object_to_add == DEV_CARD:
            if has_dev_card(self):
                self.resources_arr[arr.w] = self.resources_arr[self.w -1]
                self.resources_arr[arr.g] = self.resources_arr[self.g -1]
                self.resources_arr[arr.o] = self.resources_arr[self.o -1]
                self.dev_cards.append(dev_card)

    """
    def __init__(self):
        # player resources
        self.brick = 0
        self.lumber = 0
        self.wool = 0
        self.grain = 0
        self.ore = 0

        # player assets
        self.roads = []
        self.settlements = []
        self.cities = []
        self.dev_cards = []

    def add_road(self, road):
        self.brick -= 1
        self.lumber -= 1
        self.roads.append(road)

    def add_settlement(self, settlement):
        self.brick -= 1
        self.lumber -= 1
        self.wool -= 1
        self.grain -= 1
        self.settlements.append(settlement)

    def add_city(self, city):
        self.grain -= 2
        self.ore -= 3
        self.cities.append(city)

    def add_dev_card(self, dev_card):
        self.wool -= 1
        self.grain -= 1
        self.ore -= 1
        self.dev_cards.append(dev_card)

    def has_road(self):
        if self.brick >= 1 and self.lumber >= 1 and len(self.roads) < Constants.MAX_ROADS:
            return True
        else:
            return False

    def has_settlement(self):
        if self.brick >= 1 and self.lumber >= 1 and self.wool >= 1 and self.grain >= 1\
                and len(self.settlements) < Constants.MAX_SETTLEMENTS:
            return True
        else:
            return False

    def has_city(self, settlement):
        if self.grain >= 2 and self.ore >= 3 and len(self.cities) < Constants.MAX_CITIES:
            if settlement in self.settlements:
                return True
            else:
                return False
        else:
            return False

    def has_dev_card(self):
        if self.wool >= 1 and self.grain >= 1 and self.ore >= 1:
            return True
        else:
            return False
