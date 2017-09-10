"""
This class is the GameEngine class. It contains the object repository and the logic that the game follows so that the
Katan players can experience the functionality of the game itself.
"""

from Implementation import Board
from Implementation import Road
from Implementation import Settlement
from Implementation import City


class GameEngine:

    def __init__(self, players):
        self.board = Board.Board()
        self.players = players

    def place_road(self, player, edge):
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
            edge.road = Road.Road(player, edge)
            return edge.get_road()
        return None

    def place_settlement(self, player, vertex):
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
        if(vertex.get_settlement == None) and (self.vertex_check(player)):
            vertex.settlement = Settlement.Settlement(player, vertex)
            return vertex.get_settlement()
        return None

    def upgrade_settlement(self, player, vertex):
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
        vertex.city = City.City(player, vertex)
        return vertex.city

