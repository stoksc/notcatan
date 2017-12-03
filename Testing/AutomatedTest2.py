import os
import sys
import random

# set path to the Implementation folder
sys.path.insert(0, '\\'.join((os.getcwd().split('\\')[0:-1]))+'\\Implementation')

import Board
import BuildInfo
import City
import ClientControl
import Constants
import Edge
import GameEngine
import GameState
import GUI_road
import GUI_settlement
import GUI_tile
import HostControl
import Inventory
import Player
import Road
import Settlement
import Tile
import Vertex

# test players
player1 = Player.Player(None, 'red', 'red')
player2 = Player.Player(None, 'blue', 'blue')
player1.inventory.brick += 10000
player1.inventory.grain += 10000
player1.inventory.lumber += 10000
player1.inventory.ore += 10000
player1.inventory.wool += 10000
players = [player1, player2]
print('players build')

# test game state
gamestate = GameState.GameState(players)
print('game state builds')

# test game engine
gameengine = GameEngine.GameEngine(players)
print('game engine builds')

b1 = Board.Board()

for _ in range(1000):
    i = random.randint(0,4)
    j = random.randint(0,4)
    if b1.is_valid_coordinate(i, j):
        k = random.randint(0,5)
        print('building road on {}, {} edge {}'.format(i, j, k))
        gameengine.build(BuildInfo.BuildInfo(i, j, k, True, False, False))

for _ in range(1000):
    i = random.randint(0,4)
    j = random.randint(0,4)
    if b1.is_valid_coordinate(i, j):
        k = random.randint(0,5)
        print('building settlement on {}, {} edge {}'.format(i, j, k))
        gameengine.build(BuildInfo.BuildInfo(i, j, k, False, True, False))
