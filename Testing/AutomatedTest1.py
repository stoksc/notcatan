import os
import sys

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

'''
Test to make sure everything builds.
'''

# test board structures
edge = Edge.Edge()
vertex = Vertex.Vertex()
tile = Tile.Tile()
print('board structures built')

# test Board
board = Board.Board()
print('board builds')

# test Structures
road = Road.Road(edge)
settlement = Settlement.Settlement(vertex)
city = City.City(vertex)
print('structures build')

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

# test BuildInfo
buildinfo1 = BuildInfo.BuildInfo(0, 0, 0, True, False, False)
buildinfo2 = BuildInfo.BuildInfo(0, 0, 0, False, True, False)
print('build info builds')

# test building a road
gameengine.build(buildinfo1)
print('roads build')

# test building a settlement
gameengine.build(buildinfo2)
print('settlements build')
