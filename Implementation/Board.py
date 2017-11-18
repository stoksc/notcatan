"""
This class is an amalgamation of tiles, edges and vertices to represent the board. Don't ask how it works,
no one knows.
"""

# local imports
import Tile
import Edge
import Vertex


class Board:
    def __init__(self):
        self.tile_array = [
            [Tile.Tile() for _ in range(3)],
            [Tile.Tile() for _ in range(4)],
            [Tile.Tile() for _ in range(5)],
            [Tile.Tile() for _ in range(4)],
            [Tile.Tile() for _ in range(3)]]
        self.connect_tiles()
        self.add_edges()
        self.add_vertices()
        self.connect_edges_to_edges()
        self.connect_vertices_to_vertices()

    def connect_tiles(self):
        for i, row in enumerate(self.tile_array):
            for j, tile in enumerate(row):
                if i <= 1:
                    # check if vaild coordinate
                    if self.is_valid_coordinate(i, j + 1):
                        # connect tile to neighbor at 90degrees and connect neighbor back
                        tile.tile_arr[1] = self.tile_array[i][j + 1]
                        self.tile_array[i][j + 1].tile_arr[4] = tile
                    # connect tile to neigher at 150degree and connect neighbor back
                    tile.tile_arr[2] = self.tile_array[i + 1][j + 1]
                    self.tile_array[i + 1][j + 1].tile_arr[5] = tile
                    # connect tile to neighbor at 210degree and connect neighbor back
                    tile.tile_arr[3] = self.tile_array[i + 1][j]
                    self.tile_array[i + 1][j].tile_arr[0] = tile
                if i == 2:
                    # check if valid coordinate
                    if self.is_valid_coordinate(i, j + 1):
                        # connect tile at 90degree and connect neighbor back
                        tile.tile_arr[1] = self.tile_array[i][j + 1]
                        self.tile_array[i][j + 1].tile_arr[4] = tile
                if i > 2:
                    # connect neighbor at -30degrees and connect neighbor back
                    tile.tile_arr[5] = self.tile_array[i - 1][j]
                    self.tile_array[i - 1][j].tile_arr[2] = tile
                    # connect neighbor at 30degrees and connect neighbor back
                    tile.tile_arr[0] = self.tile_array[i - 1][j + 1]
                    self.tile_array[i - 1][j + 1].tile_arr[3] = tile
                    # check if valid coordinate
                    if self.is_valid_coordinate(i, j + 1):
                        # connect neighbor at 90 degrees and connect neighbor back
                        tile.tile_arr[1] = self.tile_array[i][j + 1]
                        self.tile_array[i][j + 1].tile_arr[4] = tile

    def add_edges(self):
        for row in self.tile_array:
            for tile in row:
                for index, edge in enumerate(tile.edge_arr):
                    # edge is made right any time it would be made, so if it is there, it is right; don't make again.
                    if edge is None:
                        # initialize edge and attach it to tile and vice versa
                        edge = tile.edge_arr[index] = Edge.Edge()
                        edge.tile_arr[0] = tile
                        if tile.tile_arr[index] is not None:
                            # attach edge to adjacent tile
                            tile.tile_arr[index].edge_arr[(index + 3) % 6] = edge
                            edge.tile_arr[1] = tile.tile_arr[index]

    def add_vertices(self):
        for row in self.tile_array:
            for tile in row:
                for index, vertex in enumerate(tile.vertex_arr):
                    if vertex is None:
                        # initialize vertex and attach it to tile and vice versa
                        vertex = tile.vertex_arr[index] = Vertex.Vertex()
                        vertex.tile_arr[0] = tile
                        if tile.tile_arr[index]:
                            # for one neighbor (border tiles) attach vertex to neighbor and vice versa
                            tile.tile_arr[index].vertex_arr[(index + 4) % 6] = vertex
                            vertex.tile_arr[1] = tile.tile_arr[index]
                            if tile.tile_arr[index - 1] is not None:
                                # for two neighbors (center tiles) do the same again for vertices
                                tile.tile_arr[index - 1].vertex_arr[(index + 2) % 6] = vertex
                                vertex.tile_arr[2] = tile.tile_arr[index - 1]


    def connect_edges_to_edges(self):
        for row in self.tile_array:
            for tile in row:
                for index, edge in enumerate(tile.edge_arr):
                    # edge's counterclockwise/clockwise 60degree neighbor
                    ccw_neighbor_index = (index - 1) % 6
                    cw_neighbor_index = (index + 1) % 6
                    # connect it to to the two edges on the same tile (existence is known)
                    edge.edge_arr[0] = tile.edge_arr[ccw_neighbor_index]
                    edge.edge_arr[3] = tile.edge_arr[cw_neighbor_index]
                    # check existence of first neighbor tile
                    if tile.tile_arr[ccw_neighbor_index] is not None:
                        # connect it to the this neighbor tile's edge
                        edge.edge_arr[1] = tile.tile_arr[ccw_neighbor_index].edge_arr[(ccw_neighbor_index + 2) % 6]
                    if tile.tile_arr[cw_neighbor_index] is not None:
                        # connect it to the this other neighbor tile's edge
                        edge.edge_arr[2] = tile.tile_arr[cw_neighbor_index].edge_arr[(cw_neighbor_index - 2) % 6]

    def connect_vertices_to_vertices(self):
        for row in self.tile_array:
            for tile in row:
                for index, vertex in enumerate(tile.vertex_arr):
                    vertex.adj_vertices.add(tile.vertex_arr[(index - 1) % 6])
                    vertex.adj_vertices.add(tile.vertex_arr[(index + 1) % 6])
                    if tile.tile_arr[index] is not None:
                        vertex.adj_vertices.add(tile.tile_arr[index].vertex_arr[(index - 1) % 6])

    def __repr__(self):
        r = ""
        for index, row in enumerate(self.tile_array):
            if (index == 0 or index == 4):
                r += (" "*30 + repr(row) + "\n")
            if (index == 1 or index == 3):
                r += (" "*15 + repr(row) + "\n")
            if (index == 2):
                r += (repr(row) + "\n")
        return r


    def is_valid_coordinate(self, x, y):
        try:
            self.tile_array[x][y]
            return True
        except IndexError:
            return False
