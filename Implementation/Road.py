"""
This is the road class. It contains a reference to a player that owns it and the edge it exists on.
"""
from Implementation import Player
from Implementation import Edge


class Road:

    def __init__(self, edge):
        self.owner = None
        self.edge = edge

    def get_owner(self) -> Player:
        return self.owner

    def get_edge(self) -> Edge:
        return self.edge

    def set_owner(self, player):
        self.owner = player
