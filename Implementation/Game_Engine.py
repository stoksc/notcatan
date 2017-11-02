"""
This class is the GameEngine class. It contains the object repository and the logic that the game follows so that the
Katan players can experience the functionality of the game itself.
"""
from Implementation import Game_State
from Implementation import Vertex
from Implementation import Edge
from Implementation import Road
from Implementation import Settlement
from Implementation import City
from Implementation import Build_Info


class Game_Engine:

    def __init__(self, player_array):
        self.game_state = Game_State.Game_State(player_array)
        if len(player_array) == 4:
            self.game_state.initial_setup()

    def build(self, build_info):
        """
        The Game_Engine uses this method in order to determine which action, if said action is valid, and to complete
        the instantiation of the object.

        Args:
            build_info (Build_Info): Object with relevant information to dynamically determine what and where the
            object to instantiate in the game_state.
        Returns:
            True (bool): Returns a True boolean value if the game_state was modified and the item determined from the
            passed info was built.
            False (bool): Returns a False boolean value if the game_state was not modified for any reason.
        """
        if self.check_player_inventory(build_info.get_build_type()):
            location_to_build = None
            if build_info.get_build_type() == "Road":
                location_to_build = self.game_state.get_board().get_tile_array()[build_info.get_row()]\
                    [build_info.get_column()].get_edge(build_info.get_edge())
                if self.check_location(location_to_build):
                    return self.build_item(location_to_build)
            elif build_info.get_build_type() == "Settlement/City":
                location_to_build = self.game_state.get_board().get_tile_array()[build_info.get_row()]\
                    [build_info.get_column()].get_vertex(build_info.get_vertex())
                if self.check_location(location_to_build):
                    return self.build_item(location_to_build)
            elif build_info.get_build_type() == "Development Card":
                return self.build_item(location_to_build)
            return False
        return False

    def check_player_inventory(self, build_type):
        """
        The Game_Engine uses this method in order to check if the current_player has the appropriate attributes in order
        to proceed with the build() method that invoked this method.

        Args:
            build_type (str): A string argument that is passed to this method to determine which object the build()
            method is to try and instantiate and check whether or not the current_player has the appropriate attributes
            to actually instantiate the type of object that the build() method is trying to instantiate.
        Returns:
            True (bool): Returns a True boolean value if the current_player has the appropriate attributes to
            instantiate the type of object the build() method is attempting to instantiate.
            False (bool): Returns a False boolean value if the current_player does not have the appropriate attributes
            to instantiate the type of object the build() method is attempting to instantiate.
        """
        if build_type == "Road":
            return self.game_state.get_current_player().get_inventory().has_road()
        elif build_type == "Settlement/City":
            if self.game_state.get_current_player().get_inventory().has_city():
                return True
            elif self.game_state.get_current_player().get_inventory().has_settlement():
                return True
            else:
                return False
        else:
            return self.game_state.get_current_player().get_inventory().has_dev_card()

    def check_location(self, object_to_build_on):
        """
        The Game_Engine uses this method in order to check if the object_to_build_on value is a valid object to proceed
        with the build() method that initially invoked this method.

        Args:
            object_to_build_on (object): An object argument that is passed to this method to determine whether or not
            the object is a valid value that in order to proceed with the build() method that invoked this method.
        Returns:
             True (bool): Returns a True boolean value if the object_to_build_on value is valid in order to proceed with
             the build() method that invoked this method.
             False (bool): Returns a False boolean value if the object_to_build_on value is not a valid value in order
             to proceed with the build() method that invoked this method.
        """
        if type(object_to_build_on) is Edge and object_to_build_on.get_road() is None:
            return True
        elif type(object_to_build_on) is Vertex and object_to_build_on.get_settlement() is None and\
                self.game_state.vertex_check(object_to_build_on):
            return True
        elif type(object_to_build_on) is Vertex and object_to_build_on.get_settlement().get_owner() ==\
                self.game_state.get_current_player():
            return True
        return False

    def build_item(self, object_to_build_on):
        """
        The Game_Engine uses this method in order to instantiate the object that the build() method has determined as
        the valid object to instantiate after previous checks, check_location() and player_inventory() methods, have
        returned a True boolean value.

        Args:
            object_to_build_on (object): An object argument that is passed to this method to determine which object that
            the build() method, that invoked this method, is attempting to instantiate.
        Returns:
             None
        """
        if object_to_build_on is None:
            self.game_state.get_current_player().get_inventory().add_dev_card(Development_Card.Development_Card())
            return True
        elif type(object_to_build_on) is Vertex and object_to_build_on.get_settlement() is None:
            self.game_state.add_invalid_vertices_to_build(object_to_build_on)
            object_to_build_on.settlement = Settlement.Settlement(object_to_build_on)
            self.game_state.get_current_player().get_inventory().add_settlement(object_to_build_on.get_settlement())
            return True
        elif type(object_to_build_on) is Vertex and object_to_build_on.get_settlement().get_owner() ==\
                self.game_state.get_current_player():
            object_to_build_on.settlement = None
            object_to_build_on.city = City.City(object_to_build_on)
            self.game_state.get_current_player().get_inventory().add_city(object_to_build_on.get_city())
            return True
        elif type(object_to_build_on) is Edge:
            object_to_build_on.road = Road.Road(object_to_build_on)
            self.game_state.get_current_player().get_inventory().add_road(object_to_build_on.get_road())
            return True

    def get_game_state(self):
        return self.game_state
