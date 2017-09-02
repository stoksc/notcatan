"""
This class is the Tile class. It contains references to the six adjacent tiles, its six edges 
and its six vertices.
"""


class Tile:

    def __init__(self):
        self.tile_arr = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6] = [None, None, None, None, None, None]
        self.vertex_arr = [self.v1, self.v2, self.v3, self.v4, self.v5, self.v6] = [None, None, None, None, None, None]
        self.edge_arr = [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6] = [None, None, None, None, None, None]
        self.type = None
        self.value = None