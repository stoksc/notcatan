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
        self.invalid_vertices_to_build_array = []
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
        if vertex in self.invalid_vertices_to_build_array:
            self.invalid_vertices_to_build_array.append(vertex)
        for v1 in vertex.adj_vertices:
            if v1 in self.invalid_vertices_to_build_array:
                pass
            else:
                self.invalid_vertices_to_build_array.append(v1)

    def vertex_check(self, vertex):
        """
        The Game_State uses this method to check whether or not the vertex passed exists in the invalid_vertices_to_
        build_array.

        Args:
            vertex (Vertex): The vertex passed to check

        Returns:
            bool: if the vertex is in the invalid_vertices_to_build_array, returns False; else True.
        """
        if vertex in self.invalid_vertices_to_build_array:
            return False
        else:
            if self.has_connected_road(vertex):
                return True
            return False

    def has_connected_road(self, vertex):
        for tile in vertex.tile_arr:
            if tile != None:
                vertex_index = tile.vertex_arr.index(vertex)
                r1 = tile.edge_arr[(vertex_index-1)%6].road
                r2 = tile.edge_arr[vertex_index].road
                if r1 != None:
                    if r1.owner == self.current_player:
                        return True
                if r2 != None:
                    if r2.owner == self.current_player:
                        return True
        return False

    def not_on_opp_sett(self, edge):
        for tile in edge.tile_arr:
            if tile != None:
                t1 = tile
        edge_index = t1.edge_arr.index(edge)
        s1 = tile.vertex_arr[edge_index].settlement
        s2 = tile.vertex_arr[(edge_index+1)%6].settlement
        if s1 != None:
            if s1.owner != self.current_player:
                return False
        if s2 != None:
            if s2.owner != self.current_player:
                return False
        return True
