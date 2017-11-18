import Player
import GameEngine
from BuildInfo import BuildInfo
import HostControl
# import pdb; pdb.set_trace()

host = HostControl.HostControl(('localhost', 8000))
player_addrs = host.get_conns()

player_array = []
netid = player_addrs[0][1][0] + '.' + str(player_addrs[0][1][1])
player1 = Player.Player(netid, "blue", "blue")
player_addrs[1][1][0] + '.' + str(player_addrs[1][1][1])
player2 = Player.Player(netid, "red", "red")
# player_addrs[2][1][0] + '.' + str(player_addrs[2][1][1])
# player3 = Player.Player(netid, "white", "Chad Smith")
# player_addrs[3][1][0] + '.' + str(player_addrs[3][1][1])
# player4 = Player.Player(netid, "green", "Becky Smith")
player_array.append(player1)
player_array.append(player2)
# player_array.append(player3)
# player_array.append(player4)
game_engine = GameEngine.GameEngine(player_array)


def make_build_info(request):
    if request[:4] == 'road':
        return BuildInfo(int(request[4]), int(request[5]), int(request[6]), True, False, False)
    elif request[:4] == 'sett':
        return BuildInfo(int(request[4]), int(request[5]), int(request[6]), False, True, False)
    elif request[:4] == 'devc':
        return BuildInfo(0, 0, 0, False, False, True)
    elif request[:4] == 'pass':
        return None
    else:
        # TODO: raise a damn error
        pass

player1.inventory.brick = 1000
player1.inventory.lumber = 1000
player1.inventory.wool = 1000
player1.inventory.grain = 1000
player1.inventory.ore = 1000

while True:
    if not host.requests.empty():
        current_request = host.requests.get()
        requester_netid = current_request[0][1][0] + '.' + str(current_request[0][1][1])
        if requester_netid == game_engine.game_state.current_player.netid:
            print('success')
            print(current_request[1])
            print(game_engine.game_state.current_player.netid, requester_netid)
            build_info = make_build_info(current_request[1])
            if build_info is not None:
                game_engine.build(build_info)
            else:
                game_engine.next_player()

#                                               r, c, i, edge,  vert, devc
print(str(game_engine.build(BuildInfo(0, 0, 0, False, True, False))))
print(str(game_engine.build(BuildInfo(0, 0, 0, False, True, False))))
print(str(game_engine.build(BuildInfo(0, 0, 0, True, False, False))))
print(str(game_engine.build(BuildInfo(0, 0, 0, True, False, False))))
