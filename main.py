#######################################################################
# Introduction to Sprites:
# A class that combines a surface, rectangle, animation, sound,.....
# We can target multiple sprites via groups
#
# As a practice for sprites, we will implement a target shooting game
# where a crosshair shoots targets
#######################################################################

import pygame, sys, random

#First we implement the crosshair class, which inherits the Sprite class
class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/crosshair.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.gun_sound = pygame.mixer.Sound('Assets/gun-shot.mp3')
    
    def shoot(self):
        self.gun_sound.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
        pos = (random.randint(200, Width), random.randint(200, Height))
        new_target = Target(pos)
        target_group.add(new_target)
    
    def update_position(self):
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.update_position()

# Implementing target sprite
class Target(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('Assets/Target.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=pos)


pygame.init()
pygame.mixer.pre_init(44100, -16, 1, 512)

# display.Info() is used to get various info about the screen
MyWindow = pygame.display.Info()
#Win_size = (MyWindow.current_w, MyWindow.current_h)
Width = 1100
Height = 700
Win_size = (Width, Height)

# ############ screen ###################
screen = pygame.display.set_mode(Win_size)
clock = pygame.time.Clock()

#background
background = pygame.image.load('Assets/Background_blurred.jpg')
background = pygame.transform.scale(background, Win_size)
pygame.mouse.set_visible(False)

# ############ crosshair #################
#Add the crosshair as a group single, 
#as to use sprites functions on a single crosshair
crosshair = Crosshair()
crosshair_group = pygame.sprite.GroupSingle()
crosshair_group.add(crosshair)

# ############ Targets ###################
# add 10 target to a Group of objects to be used together,
#and as the player shoots a target, it gets deleted and
#a new target appears in a different position
target_group = pygame.sprite.Group()
for i in range(10):
    pos = (random.randint(200, Width), random.randint(200, Height))
    new_target = Target(pos)
    target_group.add(new_target)

# ########### Game loop #################
while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Handle the shooting mechanic
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    #update targets and crosshair
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    
    pygame.display.update()
    clock.tick(240)