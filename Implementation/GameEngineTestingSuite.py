"""
This class is the GameEngine_Testing_Suite class. It is a testing suite in order to check and verify or debug possible
issues that may arise in the logic of the methods in GameEngine.
"""

import Player
import GameEngine
import BuildInfo
# import pdb; pdb.set_trace()


player1 = Player.Player("blue", "John Doe")
player2 = Player.Player("red", "Jane Doe")
player3 = Player.Player("white", "Chad Smith")
player4 = Player.Player("green", "Becky Smith")
player_array = []
player_array.append(player1)
player_array.append(player2)
player_array.append(player3)
player_array.append(player4)
game_engine = GameEngine.GameEngine(player_array)

player1.inventory.brick = 1000
player1.inventory.lumber = 1000
player1.inventory.wool = 1000
player1.inventory.grain = 1000
player1.inventory.ore = 1000

#                                               r, c, i, edge,  vert, devc
print(str(game_engine.build(BuildInfo.BuildInfo(0, 0, 0, False, True, False))))
print(str(game_engine.build(BuildInfo.BuildInfo(0, 0, 0, False, True, False))))
print(str(game_engine.build(BuildInfo.BuildInfo(0, 0, 0, True, False, False))))
print(str(game_engine.build(BuildInfo.BuildInfo(0, 0, 0, True, False, False))))
print(str(game_engine.build(BuildInfo.BuildInfo(0, 0, 0, False, False, True))))
