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
        '''
        Finds the length of the player's longest road.

        Args:
            None
        Returns:
            int
        '''
        lr = 0
        for road in self.inventory.roads:
            rl = self.road_length(road, [])
            if rl > lr:
                lr = rl
        return lr

    def road_length(self, road, visited_roads):
        '''
        Finds the longest road that can be made by following the passed road segment.

        Args:
            Road, [Road] (initially [])
        Returns:
            int
        '''
        visited_roads.append(road)
        roads_to_visit = []
        for edge in road.edge.edge_arr:
            if edge != None:
                if edge.road != None:
                    if edge.road in self.inventory.roads:
                        if not (edge.road in visited_roads):
                            roads_to_visit.append(edge.road)
        if len(roads_to_visit) == 0:
            return 1
        return max([1+self.road_length(road, visited_roads) for road in roads_to_visit])
