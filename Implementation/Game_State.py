"""
This class is the GameState class. It contains the information that represents the current state of the Settlers of
Definitely Not Katan game.
"""

class Game_State:

    def __init__(self):
        " Game_Engine will handle populating the player_array and invalid_vertices_to_build_array with logic residing in Game_Engine from player input"
        self.board = Board.Board()
        self.player_array = []
        self.invalid_vertices_to_build_array = []

    def add_invalid_vertices_to_build(self, vertex):
        """
        The Game_State uses this method to add a set of invalid vertices to the invalid vertices array.

        Args:
            vertex (Vertex): The vertex used to find the set of invalid vertices to add to the invalid_vertices_to_
            build_array.

        Returns:
            None
        """
        for i in range(len(vertex.edge_array)):
            self.invalid_vertices_to_build_array.append(vertex.edge_array[i].other_vertex())

    def vertex_check(self, vertex):
        """
        The Game_State uses this method to check whether or not the vertex passed exists in the invalid_vertices_to_
        build_array.

        Args:
            vertex (Vertex): The vertex passed to check

        Returns:
            bool: if the vertex is in the invalid_vertices_to_build_array, returns False; else True.
        """
        if self.invalid_vertices_to_build_array.__contains__(vertex):
            return False
        return True

    def append_player(self, player):
            self.player_array.append(player)