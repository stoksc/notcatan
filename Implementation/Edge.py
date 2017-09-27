"""
This is the edge class. It contains all connected edges and the two tiles it belongs to.
"""
from Implementation import Road
from Implementation import Tile
from Implementation import Vertex


class Edge:

    def __init__(self):
        self.edge_array = [self.e1, self.e2, self.e3, self.e4] = [None, None, None, None]
        self.tile_array = [self.t1, self.t2] = [None, None]
        self.vertex_array = [self.v1, self.v2] = [None, None]
        self.road = None

    def get_road(self) -> Road:
        return self.road

    def get_edge_array(self) -> [object]:
        return self.edge_array

    def get_tile_array(self) -> [Tile]:
        return self.tile_array

    def other_vertex(self, vertex) -> Vertex:
        if vertex == self.vertex_array[self.v1]:
            return self.vertex_array[self.v2]
        else:
            return self.vertex_array[self.v1]