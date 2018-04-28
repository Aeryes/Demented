import pygame as pg
import sys
from settings import Music_Mixer, loadCustomFont, States, Button, screen

#Subclass of States
class MainMenu(States):
    def __init__(self):
        States.__init__(self)
        self.next = ''
        self.playButton = Button('Play', (900, 640))
        self.quitButton = Button('Quit', (905, 780))
        self.Menu_Music = Music_Mixer('Music/menu.mp3', 0.1, -1)
        pg.mixer.music.play()
        
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
        
#Subclass of States
class GameOver(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'mainmenu'
        self.againButton = Button('Play Again', (900, 800))
        self.menuButton = Button('Main Menu', (900, 650))
        self.Menu_Music = Music_Mixer('Music/menu.mp3', 0.1, -1)
        
    def cleanup(self):
        print('cleaning up GameOver state stuff')
 
    def startup(self):
        print('starting GameOver state stuff')
       
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.againButton.MouseDown(event)
            self.menuButton.MouseDown(event)
        elif event.type == pg.MOUSEBUTTONUP:
            #Switches to 'menu' state
            if self.againButton.buttondown == True:
                self.againButton.buttondown = False
                pg.mixer.music.stop()
                self.next = 'game'
                self.done = True
            if self.menuButton.buttondown == True:
                self.menuButton.buttondown = False
                self.next = 'mainmenu'
                self.done = True
        elif event.type == pg.MOUSEMOTION:
            self.againButton.Update(event)
            self.menuButton.Update(event)
 
    def update(self, screen, dt):
        self.draw(screen)
        self.againButton.Draw(screen)
        self.menuButton.Draw(screen)
        
    def draw_text(self, text, size, color, x, y):
        self.font = loadCustomFont('Fonts/Amatic_SC/amatic_sc.ttf', 72)
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
    
    def draw(self, screen):
        #Background
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Images/Screen_bgs/menu_bg.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        screen.blit(self.image, self.rect)
        self.draw_text('Game Over', 22, (0,0,0), 950, 400)
