"""
This is the city class. It contains a reference to a player that owns it and the vertex it exists on.
"""
from Implementation import Player
from Implementation import Vertex


class City:
    def __init__(self, vertex):
        self.owner = None
        self.vertex = vertex

    def get_owner(self) -> Player:
        return self.owner

    def get_vertex(self) -> Vertex:
        return self.vertex
