"""
This class is the GameEngine class. It contains the object repository and the logic that the game follows so that the
Katan players can experience the functionality of the game itself.
"""

from Implementation import Board
from Implementation import Road
from Implementation import Settlement
from Implementation import City


class Game_Engine:

    def __init__(self):
        """
        Upon initialization, the Game_Engine needs to create socket connections for each Player for a full game.
        Upon complete connection confirmation, Game_Engine then begins initial setup logic. Waiting on individual
        inputs from each socket following initial setup logic.

        Args:
            None

        Returns:
            None
        """
        self.game_state = Game_State.Game_State()


    def place_road(self, edge):
        """
        The GameEngine uses this method to place a road.

        Args:
            player (Player): The player attempting to place a road.
            edge (Edge): The edge where the player wishes to place a road.

        Returns:
            Road? : If the edge where the road is to be placed doesn't have an existing road, returns the road which
            was placed. Otherwise, returns None.
        """
        if(edge.road == None):
            edge.road = Road.Road(edge)
            return edge.get_road()
        return None

    def place_settlement(self, vertex):
        """
        The GameEngine uses this method to place a settlement.

        Args:
            player (Player): The player attempting to place a settlement.
            vertex (Vertex): The vertex where the player wishes to place a settlement.

        Returns:
            Settlement? : If the vertex where the settlement is to be placed doesn't have an existing settlement and
            is a valid vertex for a player to place the settlement, returns the settlement which was placed. Otherwise,
            returns None.
        """
        if(vertex.get_settlement == None) and (self.game_state.vertex_check(vertex)):
            vertex.settlement = Settlement.Settlement(vertex)
            self.game_state.add_invalid_vertex_to_build(vertex)
            return vertex.get_settlement()
        return None

    def upgrade_settlement(self, vertex):
        """
        The GameEngine uses this method to upgrade a settlement into a city.

        Args:
             player (Player): The player attempting to upgrade a settlement.
             vertex (Vertex): The vertex where the player wishes to upgrade a settlement.

        Returns:
            City : If the settlement was successfully upgraded, returns the city which the settlement upgraded to.
            Otherwise, returns None.
        """
        vertex.settlement = None
        vertex.city = City.City(vertex)
        return vertex.city

    def build_item(self, object_to_build_on):
        if isinstance(object_to_build_on, self.board.Vertex):
            if object_to_build_on.get_settlement() != None:
                return self.upgrade_settlement(object_to_build_on)
            return self.place_settlement(object_to_build_on)
        if isinstance(object_to_build_on, self.game_state.board.Edge):
            return self.place_road(object_to_build_on)
        return None