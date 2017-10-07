"""
This class is the Game_Engine_Testing_Suite class. It is a testing suite in order to check and verify or debug possible
issues that may arise in the logic of the methods in Game_Engine.
"""
from __future__ import print_function

from Implementation import Player
from Implementation import Game_Engine
from Implementation import Build_Info


class Game_Engine_Testing_Suite:

    if __name__ == "__main__":
        player1 = Player.Player("blue", "John Doe")
        player2 = Player.Player("red", "Jane Doe")
        player3 = Player.Player("white", "Chad Smith")
        player4 = Player.Player("green", "Becky Smith")
        player_array = []
        player_array.append(player1)
        player_array.append(player2)
        player_array.append(player3)
        player_array.append(player4)
        game_engine = Game_Engine.Game_Engine(player_array)

        test_sett_build_row = 0
        test_sett_build_column = 0
        test_sett_build_edge = None
        test_sett_build_vertex = "v4"
        test_sett_build_dev_card = False

        test_build_info = Build_Info.Build_Info(test_sett_build_row, test_sett_build_column, test_sett_build_edge,\
                               test_sett_build_vertex, test_sett_build_dev_card)

        print(str(game_engine.build(test_build_info)))
