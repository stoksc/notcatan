import pygame, sys, math, ClientControl

WIDTH = 1000 #original 1250
HEIGHT = 704

RED = (255, 0, 0)
BLUE = (28, 107, 160)
# Hex dimensions.
t_width = 100
t_height = 116
# Settlement dimensions.
s_width = 37
s_height = 39
# Road dimensions
r_width = 37
r_height = 21

# top left coordinates for first tile
initial_x = 550
initial_y = 75


current_x = initial_x
current_y = initial_y

gui_tile_list = []
tile_rect_list = []
tile_coords = []

#def build_piece(obj, )
# Gets the left-top pixel coordinates of next hex during initial board creation.
def get_tile_pos(t_count):
    global current_x
    global current_y
    if t_count == 0:
        return (initial_x, initial_y)
    elif t_count == 3:
        current_y += 10 + (t_height//3) * 2
        current_x = initial_x - (t_width // 2) * 3
    elif t_count == 7:
        current_y += 10 + (t_height//3) * 2
        current_x = initial_x - t_width * 2
    elif t_count == 12:
        current_y += 10 + (t_height//3) * 2
        current_x = initial_x - (t_width // 2)*3
    elif t_count == 16:
        current_y += 10 + (t_height//3) * 2
        current_x = initial_x - t_width
    current_x += t_width
    return (current_x, current_y)

# Converts from 2D array to 1D.
def to_1D(num1, num2):
    if num1 == 0:
        return num2
    elif num1 == 1:
        return num2 + 3
    elif num1 == 2:
        return num2 + 7
    elif num1 == 3:
        return num2 + 12
    else:
        return num2 + 16

# Converts from 1D array to 1D.
def to_2D(num):
    if i < 3:
        return "0" + str(i)
    elif i < 7:
        return "1" + str(i - 3)
    elif i < 12:
        return "2" + str(i - 7)
    elif i < 16:
        return "3" + str(i - 12)
    else:
        return "4" + str(i - 16)

# Sprite groups for drawing().
to_render = pygame.sprite.Group()
to_derender = pygame.sprite.Group()
settlement_sprites = pygame.sprite.Group()
held_piece = pygame.sprite.Group()


# Sprite classes for assets that need to be refreshed by draw().
class Sett_Sprite(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.width = 37
        self.height = 39
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos)

    def draw(self, window):
        window.blit(self.image, self.rect)

class Road_Sprite(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.width = 37
        self.height = 21
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos)

    def draw(self, window):
        window.blit(self.image, self.rect)

class City_Sprite(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.width = 37
        self.height = 39
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos)

    def draw(self, window):
        window.blit(self.image, self.rect)



# Formulas work for all regular hexagons.
class GuiTile:
    vlist = []
    elist = []
    def __init__(self, top_left_x, top_left_y):
        self.center_x = top_left_x + t_width // 2
        self.center_y = top_left_y + t_height // 2
        self.vlist = [(self.center_x, self.center_y - t_height // 2),
                      (self.center_x + t_width // 2, self.center_y - t_height // 4),
                      (self.center_x + t_width // 2, self.center_y + t_height // 4),
                      (self.center_x, self.center_y + t_height // 2),
                      (self.center_x - t_width // 2, self.center_y + t_height // 4),
                      (self.center_x - t_width // 2, self.center_y - t_height // 4)]
        long_ratio = round(math.sqrt(pow(t_width/2, 2) - pow(t_width/4, 2)), 0)
        self.elist = [(self.center_x + t_width // 4, self.center_y - long_ratio),
                      (self.center_x + t_width // 2, self.center_y),
                      (self.center_x + t_width // 4, self.center_y + long_ratio),
                      (self.center_x - t_width // 4, self.center_y + long_ratio),
                      (self.center_x - t_width // 2, self.center_y),
                      (self.center_x - t_width // 4, self.center_y - long_ratio)]
    # Returns the coord tuple of vertex closest to mouse position.
    def closest_v(self, mouse_x, mouse_y):
        closest_index = 0
        smallest_distance = t_width
        for i in range(6):
            temp_coord = self.vlist[i]
            distance = round(math.hypot(mouse_x - temp_coord[0], mouse_y - temp_coord[1]), 0)
            if distance < smallest_distance:
                smallest_distance = distance
                closest_index = i
        return [self.vlist[closest_index], closest_index]
    # Returns the coord tuple of edge midpoint closest to mouse position.
    def closest_e(self, mouse_x, mouse_y):
        closest_index = 0
        smallest_distance = t_width
        for i in range(6):
            temp_coord = self.elist[i]
            distance = math.hypot(mouse_x - temp_coord[0], mouse_y - temp_coord[1])
            if distance < smallest_distance:
                smallest_distance = distance
                closest_index = i
        return [self.elist[closest_index], closest_index]

# Returns the closest 1D array tile to mouse_pos.
def closest_t(mouse_x, mouse_y):
    closest_index = 0
    smallest_distance = t_width * 5
    for i in range(19):
        temp_coord = tile_coords[i]
        distance = round(math.hypot(mouse_x - temp_coord[0], mouse_y - temp_coord[1]), 0)
        if distance < smallest_distance:
            smallest_distance = distance
            closest_index = i
    return closest_index

# Unused interface
def draggable(rect, mouse_pos, event):
    if (event == pygame.MOUSEBUTTONDOWN and in_region(rect, mouse_pos)):
        return True
    else:
        return False

# Checks if mouse position falls within rectangle coordinates.
def in_region(rect, mouse_pos):
    if (rect.left < mouse_pos[0] < rect.right and
                    rect.top < mouse_pos[1] < rect.bottom):
        return True
    else:
        return False

######## window instantiation
    
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Settlers of Notcatan")
clock = pygame.time.Clock()
game_end = False
window.fill(BLUE)

# loading images #####
road_stack = pygame.image.load('assets\\RoadP0-5.png').convert_alpha()
settlement_stack = pygame.image.load('assets\\SettlementP0.png').convert_alpha()
city_stack = pygame.image.load('assets\\CityP0.png').convert_alpha()

resource_bar = pygame.image.load('assets\\ResourceBar.png').convert_alpha()
dice_icon = pygame.image.load('assets\\DiceIcon.png').convert_alpha()
skip_button = pygame.image.load('assets\\SkipButton.png').convert_alpha()

# Creates sprite group array for each player, for refreshing draw() based on turn.
sprite_pieces_list = []
for i in range(4):
    sg = pygame.sprite.Group()
    sg.add(Sett_Sprite('assets\\SettlementP' + str(i) + '.png', (630, 634)))
    sg.add(Road_Sprite('assets\\RoadP' + str(i) + "-" + str(5) + ".png", (690, 634)))
    sg.add(City_Sprite('assets\\CityP' + str(i) + ".png", (770, 634)))
    sprite_pieces_list.append(sg)

temp_tile = pygame.image.load('assets\\placeholder_tile.png').convert_alpha()

# Draws the board. (Generates rectangle, gui tile object and appends to respective lists.)
for i in range(19):
    tile_file = "assets\\Tile" + to_2D(i) + ".png"

    temp_tile = pygame.image.load(tile_file).convert_alpha()
    new_pos = get_tile_pos(i)
    tile_coords.append((new_pos[0] + t_width // 2, new_pos[1] + t_height // 2))
    window.blit(temp_tile, (new_pos[0], new_pos[1]))
    temp_tile_rect = temp_tile.get_rect(topleft=(new_pos[0], new_pos[1]))
    temp_tile_guiTile = GuiTile(new_pos[0], new_pos[1])

    tile_rect_list.append(temp_tile_rect)
    gui_tile_list.append(temp_tile_guiTile)

# Updates window to display resource assets.
window.blit(resource_bar, (0, 634))
window.blit(dice_icon, (320,634))

window.blit(skip_button, (940, 646))
skip_button_rect = skip_button.get_rect(topleft=(940, 646))

window.blit(settlement_stack, (630, 634))
settlement_stack_rect = settlement_stack.get_rect(topleft=(630, 634))

window.blit(road_stack, (690, 634))
road_stack_rect = road_stack.get_rect(topleft=(690, 634))

window.blit(city_stack, (770, 634))
city_stack_rect = settlement_stack.get_rect(topleft=(770, 634))

# Booleans for settlement and city "dragging".
dragging_s = False
dragging_c = False

# Not rendering properly - Meant for refreshing "dragged" object.
h_s = pygame.sprite.Sprite()
h_s.image = pygame.image.load('assets\\placeholder_settlement.png').convert_alpha()
placed_settlement = pygame.image.load('assets\\placeholder_settlement.png').convert_alpha()


held_settlement = placed_settlement.get_rect(topleft=(800,600))
dragging_r = False

# loads images for assets that can only be instantiated at pygame.init()
placed_road = pygame.image.load('assets\\placeholder_road.png').convert_alpha()
held_road = placed_road.get_rect(topleft=(800,600))
window_text = pygame.font.SysFont('Georgia', 20)
resource_bg = pygame.image.load('assets\\resourceBG.png')
dice_bg = pygame.image.load('assets\\DiceBG.png')
vp_bg = pygame.image.load('assets\\DiceBG.png')



pygame.display.update()
turn = False

# Creates client control object for interactions with host.
client = ClientControl.ClientControl()
while not game_end:
    while not client.requests.empty():
         current_requests = client.requests.get().split('|')

         # Reads requests, and updates the board assets to reflect the current gamestate.
         for req in current_requests:
             if req == '':
                 pass
             elif req == 'strt':
                 turn = True
             elif req == 'endt':
                 turn = False

             # Settlement request.
             elif req[0:4] == 'sett':
                 row, col, vertex, p_id = int(req[4]), int(req[5]), int(req[6]), req[7]
                 index = to_1D(row, col)

                 s_sprite = Sett_Sprite('assets\\SettlementP' + p_id + '.png',
                (gui_tile_list[index].vlist[vertex][0] - s_width // 2, gui_tile_list[index].vlist[vertex][1] - s_height // 2))
                 settlement_sprites.add(s_sprite)
                 settlement_sprites.draw(window)

             # Road request.
             elif req[0:4] == 'road':
                 row, col, edge, p_id = int(req[4]), int(req[5]), int(req[6]), req[7]
                 index = to_1D(row, col)
                 r_sprite = Sett_Sprite('assets\\RoadP' + p_id + '-' + str(edge) + '.png',
                                        (gui_tile_list[index].elist[edge][0] - r_width // 2, gui_tile_list[index].elist[edge][1] - r_height // 2))
                 to_render.add(r_sprite)
                 to_render.draw(window)
                 settlement_sprites.draw(window)

             # City request.
             elif req[0:4] == 'city':
                 print('here')
                 row, col, vertex, p_id = int(req[4]), int(req[5]), int(req[6]), req[7]
                 index = to_1D(row, col)

                 c_sprite = City_Sprite('assets\\CityP' + p_id + '.png',
                                        (gui_tile_list[index].vlist[vertex][0] - s_width // 2,
                                         gui_tile_list[index].vlist[vertex][1] - s_height // 2))
                 for sprite in settlement_sprites:
                     if pygame.sprite.collide_rect(c_sprite, sprite):
                         sprite.kill()
                 to_render.add(c_sprite)
                 to_render.draw(window)
                 settlement_sprites.draw(window)

             # Turn request to redraw current player's "pieces stacks".
             elif req[0:4] == 'turn':
                 p_id = int(req[4])
                 sprite_pieces_list[p_id].draw(window)

             # Resource request to update resource display according to player.
             elif req[0:4] == 'rsrc':
                 r_list = req[4::].split(' ')
                 brick, grain, lumber, ore, wool = r_list[0], r_list[1], r_list[2], r_list[3], r_list[4]
                 resource_display = window_text.render(brick + "    " + lumber +"    " +
                                                       grain + "     " + wool + "     " + ore, False, (0, 0, 0))
                 window.blit(resource_bg, (0, 575))
                 window.blit(resource_display, (20, 600))

             # Roll request to update dice roll display.
             elif req[0:4] == 'roll':
                 dice = req[4::]
                 dice_display = window_text.render(dice, False, (0, 0, 0))
                 window.blit(dice_bg, (320, 575))
                 window.blit(dice_display, (340, 600))

             # VP request for updating current player's victory points.
             elif req[0:4] == 'pvps':
                 if turn:
                     vp = req[4::]
                     vp_display = window_text.render("VP: " + vp, False, (0, 0 , 0))
                     window.blit(vp_bg, (0, 0))
                     window.blit(vp_display, (0, 20))

             # For all unintentional behavior.
             elif req[0:4] == 'errr':
                 #TO DO: Print error message in a log
                 print("Build Attempt Failed")

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        m_x = mouse_pos[0]
        m_y = mouse_pos[1]
        click = pygame.mouse.get_pressed()[1]

        if event.type == pygame.QUIT:
            game_end = True
        #### Vertex Logic
        if turn:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if skip_button_rect.collidepoint(event.pos):
                        client.send_build_obj('pass')
                    elif settlement_stack_rect.collidepoint(event.pos):
                        dragging_s = True
                    elif city_stack_rect.collidepoint(event.pos):
                        dragging_c = True
            # If a settlement is dragged and dropped:
            elif event.type == pygame.MOUSEBUTTONUP and dragging_s:
                # Find tile closest to cursor, then find vertex of tile closest to cursor.
                index = closest_t(m_x, m_y)
                closest_tile = gui_tile_list[index]
                target = closest_tile.closest_v(m_x, m_y)[0]
                target_i = closest_tile.closest_v(m_x, m_y)[1]

                # Changes tile address from 1D array to 2D array.

                if index < 3:
                    message = "sett0" + str(index) + str(target_i)
                elif index < 7:
                    message = "sett1" + str(index-3) + str(target_i)
                elif index < 12:
                    message = "sett2" + str(index-7) + str(target_i)
                elif index < 16:
                    message = "sett3" + str(index-12) + str(target_i)
                else:
                    message = "sett4" + str(index-16) + str(target_i)

                client.send_build_obj(message)

                print(message)
                dragging_s = False
            elif event.type == pygame.MOUSEBUTTONUP and dragging_c:
                # Find tile closest to cursor, then find vertex of tile closest to cursor.
                index = closest_t(m_x, m_y)
                closest_tile = gui_tile_list[index]
                target = closest_tile.closest_v(m_x, m_y)[0]
                target_i = closest_tile.closest_v(m_x, m_y)[1]

                # Changes tile address from 1D array to 2D array.
                # message = "city" + to_2D(index) + str(target_i)

                if index < 3:
                    message = "city0" + str(index) + str(target_i)
                elif index < 7:
                    message = "city1" + str(index-3) + str(target_i)
                elif index < 12:
                    message = "city2" + str(index-7) + str(target_i)
                elif index < 16:
                    message = "city3" + str(index-12) + str(target_i)
                else:
                    message = "city4" + str(index-16) + str(target_i)

                client.send_build_obj(message)

                print(message)
                dragging_c = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging_s:
                    dragx, dragy = event.pos
                    h_s.x = dragx - s_width // 2
                    h_s.y = dragy + s_height // 2

         #### Edge Logic
            if (event.type == pygame.MOUSEBUTTONDOWN and
                in_region(road_stack_rect, mouse_pos)):
                dragging_r = True
                placed_road = pygame.image.load('assets\\placeholder_road.png').convert_alpha()
                held_road = placed_road.get_rect(topleft=(300,600))
                #window.blit(placed_settlement, (m_x - s_width //2 , m_y - s_height // 2))
            elif event.type == pygame.MOUSEMOTION and dragging_r:
                held_road.move_ip(m_x - r_width // 2, m_y + r_height // 2)
                pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and dragging_r:
                # TO DO: This section here for gamestate checking etc:
                index = closest_t(m_x, m_y)
                closest_tile = gui_tile_list[index]
                target = closest_tile.closest_e(m_x, m_y)[0]
                target_i = closest_tile.closest_e(m_x, m_y)[1]

                # message = "road" + to_2D(index) + str(target_i)

                if index < 3:
                    message = "road0" + str(index) + str(target_i)
                elif index < 7:
                    message = "road1" + str(index - 3) + str(target_i)
                elif index < 12:
                    message = "road2" + str(index - 7) + str(target_i)
                elif index < 16:
                    message = "road3" + str(index - 12) + str(target_i)
                else:
                    message = "road4" + str(index - 16) + str(target_i)

                client.send_build_obj(message)
                dragging_r = False
        else:
            # not turn stuff
            pass
    pygame.sprite.RenderUpdates
    pygame.display.update()
    clock.tick(30)

pygame.quit()
