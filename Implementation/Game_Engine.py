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
from Implementation import Development_Card


class Game_Engine:

    def __init__(self):
        self.game_state = Game_State.Game_State()

    def build(self, build_information):
        """
        The Game_Engine uses this method in order to determine which build action to take.

        Args:
            build_information (Build_Info): Object with relevant information to dynamically determine what and where to
            build in the game_state.
        Returns:
            game_state (Game_State): Returns the Game_State that has been modified or not modified since original method
            call of build().
        """
        if self.player_inventory(build_information.get_build_type()):
            location_to_build = None
            if build_information.get_build_type() == "Road":
                location_to_build = self.get_game_state().get_board().get_tile_array()[build_information.get_row()][build_information.get_column()].get_edge_array()[build_information.get_edge()]
                if self.check_location(location_to_build):
                    self.build_item(location_to_build)
            elif build_information.get_build_type() == "Settlement/City":
                location_to_build = self.get_game_state().get_board().get_tile_array()[build_information.get_row()][build_information.get_column()].get_vertex_array()[build_information.get_vertex()]
                if self.check_location(location_to_build):
                    self.build_item(location_to_build)
            elif build_information.get_build_type() == "Development Card":
                self.build_item(location_to_build)
        return self.get_game_state()

    def player_inventory(self, build_type):
        if build_type == "Road":
            return self.get_game_state().get_current_player().get_inventory().has_road()
        elif build_type == "Settlement/City":
            if self.get_game_state().get_current_player().get_inventory().has_city():
                return True
            elif self.get_game_state().get_current_player().get_inventory().has_settlement():
                return True
            else:
                return False
        else:
            return self.get_game_state().get_current_player().get_inventory().has_dev_card()

    def check_location(self, object_to_build_on):
        if type(object_to_build_on) is Edge and object_to_build_on.get_road() is None:
            return True
        elif type(object_to_build_on) is Vertex and object_to_build_on.get_settlement() is None and self.get_game_state().vertex_check(object_to_build_on):
            return True
        elif type(object_to_build_on) is Vertex and object_to_build_on.get_settlement().get_owner() == self.get_game_state().get_current_player():
            return True
        return False

    def build_item(self, object_to_build_on):
        if object_to_build_on is None:
            self.get_game_state().get_current_player().get_inventory().add_dev_card(Development_Card.Development_Card())
        elif type(object_to_build_on) is Vertex and object_to_build_on.get_settlement() is None:
            self.get_game_state().add_invalid_vertices_to_build(object_to_build_on)
            object_to_build_on.settlement = Settlement.Settlement(object_to_build_on)
            self.get_game_state().get_current_player().get_inventory().add_settlement(object_to_build_on.get_settlement())
        elif type(object_to_build_on) is Vertex and object_to_build_on.get_settlement().get_owner() == self.get_game_state().get_current_player():
            object_to_build_on.settlement = None
            object_to_build_on.city = City.City(object_to_build_on)
            self.get_game_state().get_current_player().get_inventory().add_city(object_to_build_on.get_city())
        elif type(object_to_build_on) is Edge:
            object_to_build_on.road = Road.Road(object_to_build_on)
            self.get_game_state().get_current_player().get_inventory().add_road(object_to_build_on.get_road())

    def get_game_state(self) -> Game_State:
        return self.game_state
