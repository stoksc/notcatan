"""
This is the settlement class. It contains a reference to a player that owns it and the vertex it exists on.
"""
import Player
import Vertex


class Settlement:

    def __init__(self, vertex):
        self.owner = None
        self.vertex = vertex
