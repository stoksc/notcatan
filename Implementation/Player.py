"""
Class Player contains all the objects that belong to the Player and all the methods that the Player
can execute. 

The Player has an inventory, a color, a name and turn variable which the Game accesses to give the player
permission to act on the GameBoard.

The player can place a road, place a settlement, upgrade a settlement and roll the dice.
"""

from Implementation import Inventory
from Implementation import GameEngine
from Implementation import Vertex


class Player:
    def __init__(self, color, name):
        # this variable will be a mutex lock that is passed between players
        self.turn = False
        self.name = name
        self.color = color
        self.inventory = Inventory.Inventory()

    def place_road(self, edge):
        """
        The Player uses this method to place a road.
        
        Args:
            edge (Edge): The edge where the player wishes to place a road.
            
        Returns:
            Road? : If the road was placed successfully, returns the road which was placed. Otherwise, returns None.        
        """
        if self.turn:
            if self.inventory.has_road():
                # TODO: make the GameEngine
                road = GameEngine.place_road(self, edge)
                if road != None:
                    self.inventory.add_road(road)
                else:
                    return None


    def place_settlement(self, vertex):
        """
        The Player uses this method to place a settlement.
        
        Args:
            vertex (Vertex): The vertex where the Player wishes to place a settlement.
             
        Returns:
            Settlement? : If the road was placed successfully, returns the road which was placed.
            Otherwise, returns None.
        """
        if self.turn:
            if self.inventory.has_settlement():
                settlement = GameEngine.place_settlement(vertex)
                if settlement != None:
                    self.inventory.add_settlement(settlement)
                else:
                    return None

    def upgrade_settlement(self, vertex):
        """
        The Player uses this method to upgrade a settlement.
        
        Args:
            vertex (Vertex): The vertex where the Player wishes to upgrade an existing settlement.
            
        Returns:
             bool: If the settlement was upgraded successfully, returns True; else, False. 
        """
        if self.turn:
            if self.inventory.has_city(vertex.get_settlement()):
                city = GameEngine.place_city(vertex)
                if city != None:
                    self.inventory.add_city(city)
                else:
                    return None

    def roll_dice(self):
        """
        The Player uses this method to invoke Game.roll_dice(). 
        
        Args:
            None
            
        Returns:
            bool: If the dice was rolled, returns True; else, returns False.
        """

    def longest_road(self):
        """
        This method takes no parameters and uses the inventory to determine the longest road
        which the player owns and returns the length as an Int.
        """
