import pygame as pg
from settings import Music_Mixer, loadCustomFont, States, screen, WIDTH, HEIGHT, GROUND_HEIGHT, PLAYER_FRICTION, PLAYER_ACC, PLAYER_GRAV, PLAYER_JUMP, vec
from time import sleep
from os import path
from random import choice
from images import STICKMAN_IDLE, STICKMAN_RUN_LEFT, STICKMAN_RUN_RIGHT, PLATFORM_STAGE_ONE

"""This section contains entity states which are separate from game and menu states."""
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.game = game
        
        self.jumping = False
        
        self.ms = 0
        self.anim_timer = 0
        self.anim_index = 0
        
        self.pos = vec(950, 980)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
        self.images = STICKMAN_IDLE
        self.image = self.images[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (950,980)
    
    def jump(self):
        if self.jumping == False:
            self.game.jump_sound.play()
            self.game.jump_sound.set_volume(0.3)
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        self.jumping = True
        if hits:
            self.vel.y = -PLAYER_JUMP
            self.jumping = False
            
    #Animates the running movement of the player.
    def runAnim(self, dt):
        # Add the delta time to the anim_timer and increment the
        # index after 70 ms.
        self.anim_timer += dt
               
        if self.anim_timer > self.ms:
            self.anim_timer = 0  # Reset the timer.
            self.anim_index += 1  # Increment the index.
            self.anim_index %= len(self.images)  # Modulo to cycle the index.
            self.image = self.images[self.anim_index]  # And switch the image.
    
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.keys = pg.key.get_pressed()
        
        if self.keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
            self.ms = 0.07
            self.images = STICKMAN_RUN_LEFT
            
        if self.keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
            self.ms = 0.07
            self.images = STICKMAN_RUN_RIGHT
            
        #Equations for motion.
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        #Stop player from leaving the screen.
        if self.pos.x > WIDTH - 10:
            self.pos.x = WIDTH - 1910
        if self.pos.x < WIDTH - 1910:
            self.pos.x = WIDTH - 10
        
        if not self.keys[pg.K_d] and not self.keys[pg.K_a]:
            self.ms = 0.07
            self.images = STICKMAN_IDLE 
        
        self.rect.midbottom = self.pos
        
    #draws the player to the screen.
    def draw(self):
        screen.blit(self.image, self.rect)
 
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        
        self.images = PLATFORM_STAGE_ONE
        self.image = PLATFORM_STAGE_ONE[0]
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, self.rect)
