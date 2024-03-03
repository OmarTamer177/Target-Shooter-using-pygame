#######################################################################
# Introduction to Sprites:
# A class that combines a surface, rectangle, animation, sound,.....
# We can target multiple sprites via groups
#
# As a practice for sprites, we will implement a target shooting game
# where a crosshair shoots targets
#######################################################################

import pygame, sys

#First we implement the crosshair class, which inherits the Sprite class
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

pygame.init()

screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

crosshair = Crosshair(50, 50, 100, 100, (255, 255, 255))

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    crosshair_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
