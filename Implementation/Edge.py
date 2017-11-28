"""
This is the edge class. It contains all connected edges and the two tiles it belongs to.
"""
import Road
import Tile
import Vertex


class Edge:
    def __init__(self):
        self.edge_arr = [self.e1, self.e2, self.e3, self.e4] = [None, None, None, None]
        self.tile_arr = [self.t1, self.t2] = [None, None]
        self.vertex_arr = [self.v1, self.v2] = [None, None]
        self.road = None
