import pygame as pg
from settings import Music_Mixer, loadCustomFont, States, screen
from entities import Player, Platform

#Subclass of States
#Can make subclasses of the subclass
#Used to load game assets and do runtime stuff.
class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'levelone'
        
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
        
    def draw(self, screen):
        screen.fill((255, 0, 0))

#Level One of the game.
class LevelOne(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'mainmenu'
        self.player_one = Player(950, 950)
        self.platform_one = Platform(1200,950)

        self.platforms = pg.sprite.Group()
        self.platforms.add(self.platform_one)
        
    def cleanup(self):
        print('cleaning up Game Level One state stuff')
        
    def startup(self):
        print('starting Game Level One state stuff')
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Game Level One State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            pg.mixer.music.play()
            self.done = True
        
    def update(self, screen, dt):
        self.draw(screen)
        self.player_one.move_player(1, dt)
        self.player_one.runAnim(dt)
        self.player_one.jumping(dt)
        self.player_one.is_collided_with(self.platforms)
        
    def draw_level(self):
            pass
    
    def create_plat(self, x, y):
        plat = Platform(x, y)
        self.platforms.add(plat)
        return plat
    
    def draw(self, screen):
        screen.fill((255, 255, 0))
        
        #Move and draw the player.
        self.player_one.draw_entity()
        
        #Draw the test platform.
        for plat in self.platforms:
            plat.draw_plat()
