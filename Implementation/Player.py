"""
Class Player contains all the objects that belong to the Player and all the methods that the Player
can execute. 

The Player has an inventory, a color, a name and turn variable which the Game accesses to give the player
permission to act on the GameBoard.

The player can place a road, place a settlement, upgrade a settlement and roll the dice.
"""

from Implementation import Inventory


class Player:
    def __init__(self, color, name):
        self.name = name
        self.color = color
        self.inventory = Inventory.Inventory()

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_inventory(self):
        return self.inventory
