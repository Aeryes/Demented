import pygame as pg
import game
import sys
from settings import Music_Mixer, loadCustomFont
 
#Superclass of all states
#Any data you wish to persist between all states would go in here
#Logic that persists between all states would go in here
class States():
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
 
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
            if self.settingsButton.buttondown == True:
                self.settingsButton.buttondown = False
                self.next = 'settings'
                self.done = True
            if self.quitButton.buttondown == True:
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
            print('Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.videoButton.MouseDown(event)
            self.audioButton.MouseDown(event)
            self.backButton.MouseDown(event)
        elif event.type == pg.MOUSEBUTTONUP:
            #Switches to 'game' state
            if self.backButton.buttondown == True:
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
        
class Button:
    def __init__(self,text,pos,size=(100,125),color=(0,0,200),highlight=(255,255,255)):
        self.normal = color
        self.highlight = highlight
        self.rect = pg.Rect(pos,size)
        self.mouseover = False
        self.text = text
        self.font = loadCustomFont('Fonts/Amatic_SC/amatic_sc.ttf', 72)
        self.text_image = self.font.render(text,1,(100,100,100))
        w,h = self.font.size(text) # size of font image
        self.text_pos = (pos[0] + size[0] / 2 - w / 2,pos[1] + size[1] / 2 - h / 2) # center text
        self.buttondown = False
 
    def Draw(self,surface):
        if self.mouseover:
            self.text_image = self.font.render(self.text, 1, self.highlight)
        else:
            self.text_image = self.font.render(self.text, 1, (100, 100, 100))
        surface.blit(self.text_image,self.text_pos)
 
    def Update(self,event):
        x,y = event.pos
        px,py,w,h = self.rect
        self.mouseover = False
        if x > px and x < px + w:
            if y > py and y < py + h:
                self.mouseover = True
        if not self.mouseover:
            self.buttondown = False
 
    def MouseDown(self,event):
        if self.mouseover:
            self.buttondown = True
 
    def Click(self,event):
        # let you know when mouse is over button and button was push.
        if self.buttondown and self.mouseover:
            self.buttondown = False
 
#Subclass of States
#Can make subclasses of the subclass
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
            pg.mixer.music.play()
            self.done = True
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((255, 0, 0))

'''
Does not have to be a class
Could be global scope
Never more than one Control Class
Has main game loop
Has main update
Has main event loop
Switches between states
'''
class Control:
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pg.display.set_mode(self.size, pg.FULLSCREEN)
        self.clock = pg.time.Clock()
       
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
 
    def flip_state(self):
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
 
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)
 
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)
 
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps)/1000
            self.event_loop()
            self.update(delta_time)
            pg.display.update()
 
#Program starts here by creating dictionary of settings
settings = {'size':(1920, 1080),
            'fps' :60,
            'FULLSCREEN' : True}
 
#Settings from above dictionary get passed into Control class
#Control creates app object.
#Then, each state (Menu & Game) object get assigned to a dicitonary.
#This allows control to be able to switch to and from any state as needed.
app = Control(**settings)
 
#State Dictionary. Include all state classes here.
state_dict = {'mainmenu': MainMenu(),
              'game': Game() ,
              'settings' : Settings(),
              'levelone' : LevelOne()}
 
#Setup State is called and sets the initial state of the program
app.setup_states(state_dict, 'mainmenu')
 
#Call main game loop that runs whole program
app.main_game_loop()
 
pg.quit()
sys.exit()
