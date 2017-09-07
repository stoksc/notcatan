"""
This class is the vertex of the hexes on the game board. It contains references to tiles that share it,
the settlement that is on it and the edges connected to it.
"""


class Vertex:

    def __init__(self):
        self.edge_array = [self.e1, self.e2, self.e3] = [None, None, None]
        self.tile_array = [self.t1, self.t2, self.t3] = [None, None, None]
        self.settlement = None
        self.city = None

    def get_settlement(self):
        return self.settlement

    def get_city(self):
        return self.city
