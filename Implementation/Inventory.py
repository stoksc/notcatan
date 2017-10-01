"""
Class Inventory contains a set of objects belonging to a player and methods to manipulate and check them.
"""

# local imports
from Implementation import Constants
from Implementation import Settlement
from Implementation import City
from Implementation import Road


class Inventory:

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

    def get_settlements(self) -> [Settlement]:
        return self.settlements

    def get_roads(self) -> [Road]:
        return self.roads

    def get_cities(self) -> [City]:
        return self.cities
