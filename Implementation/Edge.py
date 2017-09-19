"""
This is the edge class. It contains all connected edges and the two tiles it belongs to.
"""


class Edge:

    def __init__(self):
        self.edge_array = [self.e1, self.e2, self.e3, self.e4] = [None, None, None, None]
        self.tile_array = [self.t1, self.t2] = [None, None]
        self.vertex_array = [self.v1, self.v2] = [None, None]
        self.road = None

    def get_road(self):
        return self.road

    def other_vertex(self, vertex):
        if vertex == self.vertex_array[v1]:
            return self.vertex_array[v2]
        else:
            return self.vertex_array[v1]