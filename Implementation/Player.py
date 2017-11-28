"""
Class Player contains all the objects that belong to the Player and all the methods that the Player
can execute.

The Player has an inventory, a color, a name and turn variable which the Game accesses to give the player
permission to act on the GameBoard.

The player can place a road, place a settlement, upgrade a settlement and roll the dice.
"""

import Inventory


class Player:
    def __init__(self, netid, color, name):
        self.netid = netid
        self.name = name
        self.color = color
        self.vps = 0
        self.inventory = Inventory.Inventory()

    def longest_road(self):
        lr = 0
        for road in self.inventory.roads:
            rl = self.road_length(road, [], [])
            print(rl)
            if rl > lr:
                lr = rl
        return lr

    def road_length(self, road, visited_roads, lr_arr):
        visited_roads.append(road)
        for edge in road.edge.edge_arr:
            if edge.road != None:
                if edge.road in self.inventory.roads:
                    if not (edge.road in visited_roads):
                        return 1 + self.road_length(edge.road, visited_roads, lr_arr)
            return 1
