import pygame as pg
from settings import Music_Mixer, loadCustomFont, States, screen
from entities import Player, Platform

class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'mainmenu'
        self.platform = Platform(900, 600)
        self.player = Player(900, 700)
        
    def cleanup(self):
        print('cleaning up Game state stuff')
       
    def startup(self):
        print('starting Game state stuff')
       
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Game State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            pg.mixer.music.stop()
            self.done = True
    def update(self, screen, dt):
        self.draw(screen)
        
        self.player.movement(dt)
        self.player.jumping(dt)
        
    def draw(self, screen):
        screen.fill((255, 0, 0))
        
        self.platform.draw_plat()
        self.player.draw_entity()
