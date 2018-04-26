import pygame as pg
from settings import Music_Mixer, loadCustomFont, States, screen, WIDTH, HEIGHT, GROUND_HEIGHT, PLAYER_FRICTION, PLAYER_ACC, PLAYER_GRAV, PLAYER_JUMP, vec
from time import sleep
 
"""This section contains entity states which are separate from game and menu states."""
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.game = game
        
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
        self.image = pg.Surface((30,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (980,980)
    
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
    
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.keys = pg.key.get_pressed()
        
        if self.keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if self.keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        
        #Equations for motion.
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        #Stop player from leaving the screen.
        if self.pos.x > WIDTH - 10:
            self.pos.x = WIDTH - 1910
        if self.pos.x < WIDTH - 1910:
            self.pos.x = WIDTH - 10
            
        self.rect.midbottom = self.pos
        
    #draws the player to the screen.
    def draw(self):
        screen.blit(self.image, self.rect)
 
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        
        self.image = pg.Surface((w, h))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, self.rect)
