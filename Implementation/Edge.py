"""
This is the edge class. It contains all connected edges and the two tiles it belongs to.
"""


class Edge:

    def __init__(self):
        self.edge_array = [self.e1, self.e2, self.e3, self.e4] = [None, None, None, None]
        self.tile_array = [self.t1, self.t2] = [None, None]
        self.road = None