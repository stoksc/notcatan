"""
This is the road class. It contains a reference to a player that owns it and the edge it exists on.
"""
import Player
import Edge


class Road:

    def __init__(self, edge):
        self.owner = None
        self.edge = edge
