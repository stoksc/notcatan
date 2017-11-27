"""
This class is the GameState class. It contains the information that represents the current state of the Settlers of
Definitely Not Katan game.
"""

import Vertex
import Board
import Player
import Settlement
import Road
import Constants


class GameState:

    def __init__(self, player_array):
        """
        Game_Engine will handle populating the player_array and invalid_vertices_to_build_array with logic residing
        in Game_Engine from player input for this Game_State to be initialized.

        Args:
            player_array ([Player]): An array of the Player class argument that is passed to this method to properly
            initialize the Game_State.
        Returns:
            None
        """
        self.board = Board.Board()
        self.player_array = player_array
        self.invalid_vertices_to_build_array = set(())
        self.current_player = self.player_array[0]
        self.current_player_number = 0
        self.robber_tile = None
        if len(self.player_array) == Constants.NUMBER_OF_CLIENTS:
            self.initial_setup()
            self.robber_tile = self.board.tile_array[0][2]

    def initial_setup(self):
        """
        This method sets the tile types and values for the default setup.
        Args:
            None.
        Returns:
            None.
        """
        tile_type_array = [self.board.tile_array[0][0], self.board.tile_array[2][1], \
                               self.board.tile_array[2][3], self.board.tile_array[4][2]]
        for tile in tile_type_array:
            tile.type = 'lumber'

        tile_type_array = [self.board.tile_array[0][1], self.board.tile_array[1][3], \
                               self.board.tile_array[3][1], self.board.tile_array[3][2]]
        for tile in tile_type_array:
            tile.type = 'wool'

        tile_type_array = [self.board.tile_array[0][2], self.board.tile_array[2][2], \
                               self.board.tile_array[2][4], self.board.tile_array[4][1]]
        for tile in tile_type_array:
            tile.type = 'grain'

        tile_type_array = [self.board.tile_array[1][0], self.board.tile_array[1][2], \
                               self.board.tile_array[3][0]]
        for tile in tile_type_array:
            tile.type = 'brick'

        tile_type_array = [self.board.tile_array[1][1], self.board.tile_array[3][3], \
                               self.board.tile_array[4][0]]
        for tile in tile_type_array:
            tile.type = 'ore'

        # row 1
        self.board.tile_array[0][0].value = 11
        self.board.tile_array[0][1].value = 12
        self.board.tile_array[0][2].value = 9

        # row 2
        self.board.tile_array[1][0].value = 4
        self.board.tile_array[1][1].value = 6
        self.board.tile_array[1][2].value = 5
        self.board.tile_array[1][3].value = 10

        # row 3
        self.board.tile_array[2][0].value = 0
        self.board.tile_array[2][1].value = 3
        self.board.tile_array[2][2].value = 11
        self.board.tile_array[2][3].value = 4
        self.board.tile_array[2][4].value = 8

        # row 4
        self.board.tile_array[3][0].value = 8
        self.board.tile_array[3][1].value = 10
        self.board.tile_array[3][2].value = 9
        self.board.tile_array[3][3].value = 3

        # row 5
        self.board.tile_array[4][0].value = 5
        self.board.tile_array[4][1].value = 2
        self.board.tile_array[4][2].value = 6

    def add_invalid_vertices_to_build(self, vertex):
        """
        The Game_State uses this method to add a set of invalid vertices to the invalid vertices array.

        Args:
            vertex (Vertex): The vertex used to find the set of invalid vertices to add to the invalid_vertices_to_
            build_array.
        Returns:
            None
        """
        self.invalid_vertices_to_build_array.union(vertex.adj_vertices)

    def vertex_check(self, vertex):
        """
        The Game_State uses this method to check whether or not the vertex passed exists in the invalid_vertices_to_
        build_array.

        Args:
            vertex (Vertex): The vertex passed to check

        Returns:
            bool: if the vertex is in the invalid_vertices_to_build_array, returns False; else True.
        """
        return not self.invalid_vertices_to_build_array.__contains__(vertex)
