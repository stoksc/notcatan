"""
Class Inventory contains a set of objects belonging to a player and methods to manipulate and check them.
"""

# local imports
import Constants
import Settlement
import City
import Road


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
        '''
        Adds the passed road to the player inventory and removes the resources.

        Args:
            Road
        Returns:
            None
        '''
        self.brick -= 1
        self.lumber -= 1
        self.roads.append(road)

    def add_settlement(self, settlement):
        '''
        Adds the passed settlement to the player inventory and removes the resources.

        Args:
            Settlement
        Returns:
            None
        '''
        self.brick -= 1
        self.lumber -= 1
        self.wool -= 1
        self.grain -= 1
        self.settlements.append(settlement)

    def add_city(self, city):
        '''
        Adds the passed city to the player inventory and removes the resources.

        Args:
            City
        Returns:
            None
        '''
        self.grain -= 2
        self.ore -= 3
        self.cities.append(city)

    def add_dev_card(self, dev_card):
        '''
        Adds the passed dev_card to the player inventory and removes the resources.

        Args:
            DevelopmentCard
        Returns:
            None
        '''
        self.wool -= 1
        self.grain -= 1
        self.ore -= 1
        self.dev_cards.append(dev_card)

    def has_road(self):
        '''
        Checks if the player has the resources to build a road.

        Args:
            None
        Returns:
            bool
        '''
        if self.brick >= 1 and self.lumber >= 1 and len(self.roads) < Constants.MAX_ROADS:
            return True
        else:
            return False

    def has_settlement(self):
        '''
        Checks if the player has the resources to build a settlement.

        Args:
            None
        Returns:
            bool
        '''
        if self.brick >= 1 and self.lumber >= 1 and self.wool >= 1 and self.grain >= 1\
                and len(self.settlements) < Constants.MAX_SETTLEMENTS:
            return True
        else:
            return False

    def has_city(self):
        '''
        Checks if the player has the resources to build a city.

        Args:
            None
        Returns:
            bool
        '''
        if self.grain >= 2 and self.ore >= 3 and len(self.cities) < Constants.MAX_CITIES:
            return True
        else:
            return False

    def has_dev_card(self):
        '''
        Checks if the player has the resources to build a dev card.

        Args:
            None
        Returns:
            bool
        '''
        if self.wool >= 1 and self.grain >= 1 and self.ore >= 1:
            return True
        else:
            return False
