"""
This class is the vertex of the hexes on the game board. It contains references to tiles that share it,
the settlement that is on it and the edges connected to it.
"""
import Tile
import Edge
import Settlement
import City

class Vertex:
    def __init__(self):
        self.edge_arr = [self.e1, self.e2, self.e3] = [None, None, None]
        self.adj_vertices = set(())
        self.tile_arr = [self.t1, self.t2, self.t3] = [None, None, None]
        self.settlement = None
        self.city = None
