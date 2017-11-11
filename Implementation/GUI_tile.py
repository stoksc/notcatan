import pygame

class GUI_tile(pygame.sprite.Sprite):
    vlist = []
    elist = []

    width = 100
    height = 116

    # Will put these lists in game launcher.
    bg_list = ['forest.png', 'pasture.png', 'fields.png', 'hills.png', 'mountain.png', 'desert.png']
    freq_list = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png',
                 '9.png', '10.png', '11.png', '12.png']

    def __init__(self, img, top_left_x, top_left_y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(top_left_x, top_left_y))

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

    # Returns the coord tuple and index of vertex closest to mouse position.
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
    # Returns the coord tuple and index of edge midpoint closest to mouse position.
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
