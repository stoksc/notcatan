import Player
import GameEngine
from BuildInfo import BuildInfo
import HostControl
# import pdb; pdb.set_trace()

# get player connections
host = HostControl.HostControl(('localhost', 8000))
player_addrs = host.get_conns()

# initialize players
player_array = []
netid = player_addrs[0]
player1 = Player.Player(netid, 'blue', 'blue')
netid = player_addrs[1]
player2 = Player.Player(netid, 'red', 'red')
player_array.append(player1)
player_array.append(player2)
for player in player_array:
    player.inventory.lumber += 4
    player.inventory.brick += 4
    player.inventory.wool += 2
    player.inventory.grain += 2

# initialize game
game_engine = GameEngine.GameEngine(player_array)

# build initial 'beginner' setup
game_engine.build(BuildInfo(0, 0, 3, False, True, False))
game_engine.build(BuildInfo(3, 2, 2, False, True, False))
game_engine.build(BuildInfo(0, 0, 2, True, False, False))
game_engine.build(BuildInfo(3, 2, 2, True, False, False))
game_engine.next_player()

game_engine.build(BuildInfo(1, 1, 2, False, True, False))
game_engine.build(BuildInfo(2, 2, 2, False, True, False))
game_engine.build(BuildInfo(1, 1, 1, True, False, False))
game_engine.build(BuildInfo(2, 2, 2, True, False, False))
game_engine.next_player()

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
        return None

def broadcast_message(message):
    for player in game_engine.game_state.player_array:
        host.send_data(player.netid[0], message)

# start first player's turn and roll first dice
host.send_data(game_engine.game_state.current_player.netid[0], 'start')
game_engine.dice_roll()

# game loop
while True:
    if not host.requests.empty():
        current_request = host.requests.get()
        requester_netid = current_request[0]
        if requester_netid == game_engine.game_state.current_player.netid:
            build_info = make_build_info(current_request[1])
            if build_info is not None:
                print(current_request)
                if game_engine.build(build_info):
                    print('sending success')
                    broadcast_message(current_request[1])
                else:
                    host.send_data(current_request[0][0], 'err')
            else:
                host.send_data(current_request[0][0], 'end')
                game_engine.next_player()
                game_engine.dice_roll()
                for player in game_engine.game_state.player_array:
                    host.send_data(player.netid[0], ' '.join([str(player.inventory.brick),
                                                              str(player.inventory.lumber),
                                                              str(player.inventory.wool),
                                                              str(player.inventory.grain),
                                                              str(player.inventory.ore)]))
                host.send_data(game_engine.game_state.current_player.netid[0], 'start')
