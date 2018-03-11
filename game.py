import sys
import pygame as pg
import main
from settings import Music_Mixer, loadCustomFont

class LevelOne(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'mainmenu'
    def cleanup(self):
        print('cleaning up Game state stuff')
    def startup(self):
        print('starting Game state stuff')
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Game State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            pg.mixer.music.play()
            self.done = True
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0, 0, 0))
