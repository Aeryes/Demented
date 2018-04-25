import pygame as pg
from settings import Music_Mixer, loadCustomFont, States, screen, GROUND_HEIGHT
from time import sleep
 
"""This section contains entity states which are separate from game and menu states."""
class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.vel_x = 0
        self.vel_y = 15
        self.pos_x = x
        self.pos_y = y
        
        self.mass = 3
        self.jump = False
        self.rect = pg.Rect(x, y, 50, 50)
        
    def movement(self, dt):
        self.pressed = pg.key.get_pressed()
        
        if self.vel_x > 5:
            self.vel_x = 5
        if self.vel_x < -5:
            self.vel_x = -5
       
        if self.pressed[pg.K_a]:
            if self.vel_x > 0:
                self.vel_x = 0
            self.vel_x -= 0.5
            self.pos_x += self.vel_x  # Move left.

        if self.pressed[pg.K_d]:
            if self.vel_x < 0:
                self.vel_x = 0
            self.vel_x += 0.5
            self.pos_x += self.vel_x  # Move right.
        
        if self.pressed[pg.K_w]:
            self.jump = True
            self.vel_y = -15
        
        # Update the rect because it's used to blit the image.
        self.rect.center = self.pos_x, self.pos_y
    
    def jumping(self, dt):
        if self.jump:
            #Calculate force.
            F = (0.5 * self.mass * (self.vel_y))
           
            #Change position.
            self.pos_y = self.pos_y + F
            self.rect.y = self.rect.y + F
           
            #Change velocity.
            self.vel_y = self.vel_y + 1
           
        if self.pos_y >= GROUND_HEIGHT:
            self.pos_y = GROUND_HEIGHT
            self.vel_y = 0
    
    #draws the player to the screen.
    def draw_entity(self):
        pg.draw.rect(screen, (255,255,255), self.rect)
 
#Creates platforms that the user can jump onto.
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
       
        self.moving = False
       
        self.image = None
        self.rect = pg.Rect(x, y, 150, 200)
       
    #draws the platform to the screen.
    def draw_plat(self):
        pg.draw.rect(screen, (0,0,0), self.rect)
