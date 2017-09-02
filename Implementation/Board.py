"""
This class is an amalgation of tiles, edges and vertices to represent the board. Don't ask how it works, 
no one knows.
"""

from Implementation import Tile


class Board:

    def __init__(self):
        self.tile_array = [
            [Tile.Tile() for x in range(3)],
            [Tile.Tile() for x in range(4)],
            [Tile.Tile() for x in range(5)],
            [Tile.Tile() for x in range(4)],
            [Tile.Tile() for x in range(3)],
        ]
        self.connect_tiles()

    def connect_tiles(self):
        for i, row in self.tile_array:
            for j, tile in row:
                if i <= 1:
                    # check if vaild coordinate
                    if self.is_valid_coordinate(i, j+1):
                        # connect tile to neighbor at 90degrees and connect neighbor back
                        tile.t2 = self.tile_array[i][j+1]
                        self.tile_array[i][j+1].t5 = tile
                    # connect tile to neigher at 150degree and connect neighbor back
                    tile.t3 = self.tile_array[i+1][j+1]
                    self.tile_array[i+1][j+1].t6 = tile
                    # connect tile to neighbor at 210degree and connect neighbor back
                    tile.t4 = self.tile_array[i+1][j]
                    self.tile_array[i+1][j].t1 = tile
                if i == 2:
                    # check if valid coordinate
                    if self.is_valid_coordinate(i, j+1):
                        # connect tile at 90degree and connect neighbor back
                        tile.t2 = self.tile_array[i][j+1]
                        self.tile_array[i][j+1].t5 = tile
                if i > 2:
                    # connect neighbor at -30degrees and connect neighbor back
                    tile.t6 = self.tile_array[i-1][j]
                    self.tile_array[i-1][j].t3 = tile
                    # connect neighbor at 30degrees and connect neighbor back
                    tile.t1 = self.tile_array[i-1][j+1]
                    self.tile_array[i-1][j+1].t4 = tile
                    # check if valid coordinate
                    if self.is_valid_coordinate(i,j+1):
                        # connect neighbor at 90 degrees and connect neighbor back
                        tile.t2 = self.tile_array[i][j+1]
                        self.tile_array[i][j+1].t5 = tile

    def is_valid_coordinate(self, x, y):
        if x == 0 or x == 4:
            if 0 <= y <= 2:
                return True
            else:
                return False
        elif x == 1 or x == 3:
            if 0 <= y <= 3:
                return True
            else:
                return False
        elif x == 2:
            if 0 <= y <= 4:
                return True
            else:
                return False
        else:
            return False


