"""
This class is the GameState class. It contains the information that represents the current state of the Settlers of
Definitely Not Katan game.
"""

from Implementation import Vertex
from Implementation import Board
from Implementation import Player
from Implementation import Settlement
from Implementation import Road


class Game_State:

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
        self.robber = self.board.get_tile_array()[2][0]
        self.tile_forest_type_array = []
        self.tile_forest_type_array.append(self.board.get_tile_array()[0][0], self.board.get_tile_array()[2][1],\
                                           self.board.get_tile_array()[0][3], self.board.get_tile_array()[4][2])
        for tile in self.tile_forest_type_array:
            tile.type = "forest"

        self.tile_forest_type_array.append(self.board.get_tile_array()[0][0], self.board.get_tile_array()[2][1], \
                                           self.board.get_tile_array()[0][3], self.board.get_tile_array()[4][2])
        for tile in self.tile_forest_type_array:
            tile.type = "forest"

    def initial_setup(self):
        """
        The Game_State class invokes this method in order to proceed with the logic and initialization of the beginner
        setup for a Settlers of Definitely Not Katan game.

        Args:
            None.
        Returns:
            None.
        """
        if len(self.player_array) == 4:
            settlement1 = Settlement.Settlement(self.board.get_tile_array()[0][0].get_vertex("v4"))
            settlement2 = Settlement.Settlement(self.board.get_tile_array()[3][2].get_vertex("v3"))
            road1 = Road.Road(self.board.get_tile_array()[0][0].get_edge("e3"))
            road2 = Road.Road(self.board.get_tile_array()[3][2].get_edge("e3"))
            self.setup_helper(settlement1, settlement2, road1, road2, self.player_array[0])

            settlement1 = Settlement.Settlement(self.board.get_tile_array()[1][1].get_vertex("v3"))
            settlement2 = Settlement.Settlement(self.board.get_tile_array()[2][2].get_vertex("v3"))
            road1 = Road.Road(self.board.get_tile_array()[1][1].get_edge("e2"))
            road2 = Road.Road(self.board.get_tile_array()[2][2].get_edge("e2"))
            self.setup_helper(settlement1, settlement2, road1, road2, self.player_array[1])

            settlement1 = Settlement.Settlement(self.board.get_tile_array()[0][2].get_vertex("v3"))
            settlement2 = Settlement.Settlement(self.board.get_tile_array()[1][3].get_vertex("v4"))
            road1 = Road.Road(self.board.get_tile_array()[0][2].get_edge("e3"))
            road2 = Road.Road(self.board.get_tile_array()[2][3].get_edge("e2"))
            self.setup_helper(settlement1, settlement2, road1, road2, self.player_array[2])

            settlement1 = Settlement.Settlement(self.board.get_tile_array()[3][0].get_vertex("v3"))
            settlement2 = Settlement.Settlement(self.board.get_tile_array()[4][1].get_vertex("v3"))
            road1 = Road.Road(self.board.get_tile_array()[3][0].get_edge("e2"))
            road2 = Road.Road(self.board.get_tile_array()[4][1].get_edge("e3"))
            self.setup_helper(settlement1, settlement2, road1, road2, self.player_array[3])

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
        settlement1.set_owner(player)
        settlement2.set_owner(player)
        player.get_inventory().get_settlements().append(settlement1)
        player.get_inventory().get_settlements().append(settlement2)
        self.add_invalid_vertices_to_build(settlement1.get_vertex())
        self.add_invalid_vertices_to_build(settlement2.get_vertex())
        road1.set_owner(player)
        road2.set_owner(player)
        player.get_inventory().get_roads().append(road1)
        player.get_inventory().get_roads().append(road2)

    def add_invalid_vertices_to_build(self, vertex):
        """
        The Game_State uses this method to add a set of invalid vertices to the invalid vertices array.

        Args:
            vertex (Vertex): The vertex used to find the set of invalid vertices to add to the invalid_vertices_to_
            build_array.
        Returns:
            None
        """
        for i in range(len(vertex.get_edge_array())):
            self.invalid_vertices_to_build_array.append(vertex.get_edge_array()[i].other_vertex(vertex))

    def vertex_check(self, vertex):
        """
        The Game_State uses this method to check whether or not the vertex passed exists in the invalid_vertices_to_
        build_array.

        Args:
            vertex (Vertex): The vertex passed to check

        Returns:
            bool: if the vertex is in the invalid_vertices_to_build_array, returns False; else True.
        """
        return self.invalid_vertices_to_build_array.__contains__(vertex)

    def append_player(self, player):
        if len(self.get_player_array()) == 0:
            self.current_player = player
            self.player_array.append(player)

    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.current_player

    def get_player_array(self):
        return self.player_array
