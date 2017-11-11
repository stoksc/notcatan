import pygame

class GUI_road(pygame.sprite.Sprite):

    width = 50
    height = 29

    # Will put these lists in game launcher.
    image_list = ['stock_r.png', 'p1_r0.png', 'p1_r1.png', 'p1_r2.png', 'p1_r3.png', 'p1_r4.png', 'p1_r5.png',
                  'p2_r0.png', 'p2_r1.png', 'p2_r2.png', 'p2_r3.png', 'p2_r4.png', 'p2_r5.png',
                  'p3_r0.png', 'p3_r1.png', 'p3_r2.png', 'p3_r3.png', 'p3_r4.png', 'p3_r5.png',
                  'p4_r0.png', 'p4_r1.png', 'p4_r2.png', 'p4_r3.png', 'p4_r4.png', 'p4_r5.png', ]

    def __init__(self, img, top_left_x, top_left_y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(top_left_x, top_left_y))