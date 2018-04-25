import pygame as pg
import sys
from settings import Music_Mixer, loadCustomFont, States, Button

#Subclass of States
class MainMenu(States):
    def __init__(self):
        States.__init__(self)
        self.next = ''
        self.playButton = Button('Play', (900, 640))
        self.quitButton = Button('Quit', (905, 780))
        self.Menu_Music = Music_Mixer('Music/menu.mp3', 0.1, -1)
        
    def cleanup(self):
        print('cleaning up Menu state stuff')
 
    def startup(self):
        print('starting Menu state stuff')
       
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.playButton.MouseDown(event)
            self.quitButton.MouseDown(event)
        elif event.type == pg.MOUSEBUTTONUP:
            #Switches to 'game' state
            if self.playButton.buttondown == True:
                self.playButton.buttondown = False
                pg.mixer.music.stop()
                self.next = 'game'
                self.done = True
            #Exits out of game
            elif self.quitButton.buttondown == True:
                self.quitButton.buttondown = False
                sys.exit()
        elif event.type == pg.MOUSEMOTION:
            self.playButton.Update(event)
            self.quitButton.Update(event)
 
    def update(self, screen, dt):
        self.draw(screen)
        self.playButton.Draw(screen)
        self.quitButton.Draw(screen)
       
    def draw(self, screen):
        #Background
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Images/Screen_bgs/menu_bg.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        screen.blit(self.image, self.rect)
        
