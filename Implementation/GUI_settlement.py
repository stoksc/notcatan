import pygame

class GUI_settlement(pygame.sprite.Sprite):

    width = 50
    height = 53

    # Will put these lists in game launcher.
    image_list = ['stock_s.png', 'p1_s.png', 'p2_s.png', 'p3_s.png', 'p4_s.png',
                  'stock_c.png', 'p1_c.png', 'p2_c.png', 'p3_c.png', 'p4_c.png']

    def __init__(self, img, top_left_x, top_left_y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(top_left_x, top_left_y))

