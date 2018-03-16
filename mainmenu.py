import pygame as pg
from game import LevelOne
from settings import Music_Mixer, loadCustomFont, States, Button

#Subclass of States
class MainMenu(States):
    def __init__(self):
        States.__init__(self)
        self.next = ''
        self.playButton = Button('Play', (900, 640))
        self.settingsButton = Button('Settings', (905, 780))
        self.quitButton = Button('Quit', (900, 920))
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
            self.settingsButton.MouseDown(event)
            self.quitButton.MouseDown(event)
        elif event.type == pg.MOUSEBUTTONUP:
            #Switches to 'game' state
            if self.playButton.buttondown == True:
                self.playButton.buttondown = False
                pg.mixer.music.stop()
                self.next = 'game'
                self.done = True
            #Exits out of game
            #Switches to 'settings' state.
            elif self.settingsButton.buttondown == True:
                self.settingsButton.buttondown = False
                self.next = 'settings'
                self.done = True
            elif self.quitButton.buttondown == True:
                self.quitButton.buttondown = False
                sys.exit()
        elif event.type == pg.MOUSEMOTION:
            self.playButton.Update(event)
            self.settingsButton.Update(event)
            self.quitButton.Update(event)
 
    def update(self, screen, dt):
        self.draw(screen)
        self.playButton.Draw(screen)
        self.settingsButton.Draw(screen)
        self.quitButton.Draw(screen)
       
    def draw(self, screen):
        #Background
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Images/Screen_bgs/menu_bg.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        screen.blit(self.image, self.rect)
        
#Subclass of states.
#General settings menu. 
class Settings(States):
    def __init__(self):
        States.__init__(self)
        self.next = ''
        self.videoButton = Button('Video', (900, 650))
        self.audioButton = Button('Audio', (900, 770))
        self.backButton = Button('Back', (900, 890))
        self.Menu_Music = Music_Mixer('Music/menu.mp3', 0.1, -1)
        
    def cleanup(self):
        print('cleaning up Settings Menu state stuff')
 
    def startup(self):
        print('starting Settings Menu state stuff')
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Setttings Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.videoButton.MouseDown(event)
            self.audioButton.MouseDown(event)
            self.backButton.MouseDown(event)
        elif event.type == pg.MOUSEBUTTONUP:
            #Goes to audio menu.
            if self.audioButton.buttondown == True:
                self.audioButton.buttondown = False
                self.next = 'audio'
                self.done = True
            #Goes to video menu.
            elif self.videoButton.buttondown == True:
                self.videoButton.buttondown = False
                self.next = 'video'
                self.done = True
            #Switches to 'game' state
            elif self.backButton.buttondown == True:
                self.backButton.buttondown = False
                self.next = 'mainmenu'
                self.done = True
            #Exits out of game
        elif event.type == pg.MOUSEMOTION:
            self.videoButton.Update(event)
            self.audioButton.Update(event)
            self.backButton.Update(event)
 
    def update(self, screen, dt):
        self.draw(screen)
        self.videoButton.Draw(screen)
        self.audioButton.Draw(screen)
        self.backButton.Draw(screen)
       
    def draw(self, screen):
        #Background
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Images/Screen_bgs/menu_bg.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        screen.blit(self.image, self.rect)

#Subclass of states.
#Menu for audio configuration. 
class Audio(States):
    def __init__(self):
        States.__init__(self)
        self.next = ''
        self.audioButton = Button('Audio', (900, 650))
        self.backButton = Button('Back', (900, 890))
        self.Menu_Music = Music_Mixer('Music/menu.mp3', 0.1, -1)
        
    def cleanup(self):
        print('cleaning up Audio Settings Menu state stuff')
 
    def startup(self):
        print('starting Audio Settings Menu state stuff')
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Audio Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.audioButton.MouseDown(event)
            self.backButton.MouseDown(event)
        elif event.type == pg.MOUSEBUTTONUP:
            #Switches to 'game' state
            if self.backButton.buttondown == True:
                self.backButton.buttondown = False
                self.next = 'settings'
                self.done = True
            #Exits out of game
        elif event.type == pg.MOUSEMOTION:
            self.audioButton.Update(event)
            self.backButton.Update(event)
 
    def update(self, screen, dt):
        self.draw(screen)
        self.audioButton.Draw(screen)
        self.backButton.Draw(screen)
       
    def draw(self, screen):
        #Background
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Images/Screen_bgs/menu_bg.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        screen.blit(self.image, self.rect)

class Video(States):
    def __init__(self):
        States.__init__(self)
        self.next = ''
        self.videoButton = Button('Video', (900, 650))
        self.backButton = Button('Back', (900, 890))
        self.Menu_Music = Music_Mixer('Music/menu.mp3', 0.1, -1)
        
    def cleanup(self):
        print('cleaning up Video Settings Menu state stuff')
 
    def startup(self):
        print('starting Video Settings Menu state stuff')
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Video Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.videoButton.MouseDown(event)
            self.backButton.MouseDown(event)
        elif event.type == pg.MOUSEBUTTONUP:
            #Switches to 'game' state
            if self.backButton.buttondown == True:
                self.backButton.buttondown = False
                self.next = 'settings'
                self.done = True
            #Exits out of game
        elif event.type == pg.MOUSEMOTION:
            self.videoButton.Update(event)
            self.backButton.Update(event)
 
    def update(self, screen, dt):
        self.draw(screen)
        self.videoButton.Draw(screen)
        self.backButton.Draw(screen)
       
    def draw(self, screen):
        #Background
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Images/Screen_bgs/menu_bg.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)
        screen.blit(self.image, self.rect)
