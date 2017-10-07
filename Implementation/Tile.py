"""
This class is the Tile class. It contains references to the six adjacent tiles, its six edges 
and its six vertices.
"""
from Implementation import Vertex
from Implementation import Edge


class Tile:

    def __init__(self):
        self.tile_arr = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6] = [None, None, None, None, None, None]
        self.vertex_arr = [self.v1, self.v2, self.v3, self.v4, self.v5, self.v6] = [None, None, None, None, None, None]
        self.edge_arr = [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6] = [None, None, None, None, None, None]
        self.type = None
        self.value = None

    def get_tile_array(self):
        return self.tile_arr

    def get_vertex_arr(self):
        return self.vertex_arr

    def get_edge_arr(self):
        return self.edge_arr

    def get_type(self):
        return self.type

    def get_value(self):
        return self.value

    def get_vertex(self, vx):
        if vx == "v1":
            return self.vertex_arr[self.v1]
        elif vx == "v2":
            return self.vertex_arr[self.v2]
        elif vx == "v3":
            return self.vertex_arr[self.v3]
        elif vx == "v4":
            return self.vertex_arr[self.v4]
        elif vx == "v5":
            return self.vertex_arr[self.v5]
        elif vx == "v6":
            return self.vertex_arr[self.v6]

    def get_edge(self, ex):
        if ex == "e1":
            return self.edge_arr[self.e1]
        elif ex == "e2":
            return self.edge_arr[self.e2]
        elif ex == "e3":
            return self.edge_arr[self.e3]
        elif ex == "e4":
            return self.edge_arr[self.e4]
        elif ex == "e5":
            return self.edge_arr[self.e5]
        elif ex == "e6":
            return self.edge_arr[self.e6]

    def get_tile(self, tx):
        if tx == "t1":
            return self.tile_arr[self.t1]
        elif tx == "t2":
            return self.tile_arr[self.t2]
        elif tx == "t3":
            return self.tile_arr[self.t3]
        elif tx == "t4":
            return self.tile_arr[self.t4]
        elif tx == "t5":
            return self.tile_arr[self.t5]
        elif tx == "t6":
            return self.tile_arr[self.t6]
