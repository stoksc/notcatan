"""
This is the settlement class. It contains a reference to a player that owns it and the vertex it exists on.
"""

class Settlement:

    def __init__(self, player, vertex):
        self.owner = player
        self.vertex = vertex