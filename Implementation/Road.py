"""
This is the road class. It contains a reference to a player that owns it and the edge it exists on.
"""

class Road:

    def __init__(self, player, edge):
        self.owner = player
        self.edge = edge