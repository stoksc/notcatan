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
        The Game_State class invokes this method in order to proceed with the logic and initialization of the beginner
        setup for a Settlers of Definitely Not Katan game.

        Args:
            None.
        Returns:
            None.
        """
        settlement1 = Settlement.Settlement(self.board.tile_array[0][0].vertex_arr[3])
        settlement2 = Settlement.Settlement(self.board.tile_array[3][2].vertex_arr[2])
        road1 = Road.Road(self.board.tile_array[0][0].edge_arr[2])
        road2 = Road.Road(self.board.tile_array[3][2].edge_arr[2])
        self.setup_helper(settlement1, settlement2, road1, road2, self.player_array[0])

        settlement1 = Settlement.Settlement(self.board.tile_array[1][1].vertex_arr[2])
        settlement2 = Settlement.Settlement(self.board.tile_array[2][2].vertex_arr[2])
        road1 = Road.Road(self.board.tile_array[1][1].edge_arr[1])
        road2 = Road.Road(self.board.tile_array[2][2].edge_arr[2])
        self.setup_helper(settlement1, settlement2, road1, road2, self.player_array[1])

        # settlement1 = Settlement.Settlement(self.board.tile_array[0][2].vertex_arr[2])
        # settlement2 = Settlement.Settlement(self.board.tile_array[1][3].vertex_arr[3])
        # road1 = Road.Road(self.board.tile_array[0][2].edge_arr[2])
        # road2 = Road.Road(self.board.tile_array[2][3].edge_arr[1])
        # self.setup_helper(settlement1, settlement2, road1, road2, self.player_array[2])
        #
        # settlement1 = Settlement.Settlement(self.board.tile_array[3][0].vertex_arr[2])
        # settlement2 = Settlement.Settlement(self.board.tile_array[4][1].vertex_arr[2])
        # road1 = Road.Road(self.board.tile_array[3][0].edge_arr[1])
        # road2 = Road.Road(self.board.tile_array[4][1].edge_arr[2])
        # self.setup_helper(settlement1, settlement2, road1, road2, self.player_array[3])

        tile_type_array = []
        tile_type_array += [self.board.tile_array[0][0], self.board.tile_array[2][1], \
                               self.board.tile_array[2][3], self.board.tile_array[4][2]]
        for tile in tile_type_array:
            tile.type = "Forest"

        tile_type_array = []
        tile_type_array += [self.board.tile_array[0][1], self.board.tile_array[1][3], \
                               self.board.tile_array[3][1], self.board.tile_array[3][2]]
        for tile in tile_type_array:
            tile.type = "Pasture"

        tile_type_array = []
        tile_type_array += [self.board.tile_array[0][2], self.board.tile_array[2][2], \
                               self.board.tile_array[2][4], self.board.tile_array[4][1]]
        for tile in tile_type_array:
            tile.type = "Fields"

        tile_type_array = []
        tile_type_array += [self.board.tile_array[1][0], self.board.tile_array[1][2], \
                               self.board.tile_array[3][0]]
        for tile in tile_type_array:
            tile.type = "Hills"

        tile_type_array = []
        tile_type_array += [self.board.tile_array[1][1], self.board.tile_array[3][3], \
                               self.board.tile_array[4][0]]
        for tile in tile_type_array:
            tile.type = "Mountains"

    def setup_helper(self, settlement1, settlement2, road1, road2, player):
        """
        The Game_State class invokes this method when initializing the beginner setup for a Settlers of Definitely Not
        Katan game.

        Args:
            settlement1 (Settlement): A settlement object passed, that was instantiated before this method was invoked,
            to instantiate the proper values for the object in the Game_State.
            settlement2 (Settlement): A settlement object passed, that was instantiated before this method was invoked,
            to instantiate the proper values for the object in the Game_State.
            road1 (Road): A road object passed, that was instantiated before this method was invoked, to instantiate the
            proper values for the object in the Game_State.
            road2 (Road): A road object passed, that was instantiated before this method was invoked, to instantiate the
            proper values for the object in the Game_State.
            player (Player): A player object passed, that was instantiated before this method was invoked and that the
            previous arguments passed to this method are to use to assist in instantiating the proper values for the
            previous arguments passed in the Game_State.
        Returns:
             None.
        """
        settlement1.owner = player
        settlement2.owner = player
        player.inventory.settlements.append(settlement1)
        player.inventory.settlements.append(settlement2)
        self.add_invalid_vertices_to_build(settlement1.vertex)
        self.add_invalid_vertices_to_build(settlement2.vertex)
        road1.owner = player
        road2.owner = player
        player.inventory.roads.append(road1)
        player.inventory.roads.append(road2)

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

    def next_player(self):
        self.current_player_number = (self.current_player_number + 1) % Constants.NUMBER_OF_CLIENTS
        self.current_player = self.player_array[self.current_player_number]
