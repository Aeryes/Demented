import pygame as pg
from settings import Music_Mixer, loadCustomFont, States

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
    def draw(self, screen):
        screen.fill((0, 0, 0))
