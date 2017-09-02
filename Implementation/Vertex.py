"""
This class is the vertex of the hexes on the game board. It contains references to tiles that share it,
the settlement that is on it and the edges connected to it.
"""


class Vertex:

    def __init__(self, e1, e2, e3, t1, t2, t3):
        self.edge_array = [self.e1, self.e2, self.e3] = [e1, e2, e3]
        self.tile_array = [self.t1, self.t2, self.t3] = [t1, t2, t3]
        self.settlement = None
