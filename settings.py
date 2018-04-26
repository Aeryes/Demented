import pygame as pg
import os

pg.init()

WIDTH = 1920
HEIGHT = 1080

screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
GROUND_HEIGHT = 950
vec = pg.math.Vector2

#Player properties.
PLAYER_ACC = 1
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

#Superclass of all states
#Any data you wish to persist between all states would go in here
#Logic that persists between all states would go in here
class States():
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

#Used to make buttons for menus.
class Button:
    def __init__(self, text, pos, size=(100,125), color=(0,0,200), highlight=(255,255,255)):
        self.normal = color
        self.highlight = highlight
        self.rect = pg.Rect(pos, size)
        self.mouseover = False
        self.text = text
        self.font = loadCustomFont('Fonts/Amatic_SC/amatic_sc.ttf', 72)
        self.text_image = self.font.render(text, 1, (100,100,100))
        w,h = self.font.size(text) # size of font image
        self.text_pos = (pos[0] + size[0] / 2 - w / 2, pos[1] + size[1] / 2 - h / 2) # center text
        self.buttondown = False
 
    def Draw(self, surface):
        if self.mouseover:
            self.text_image = self.font.render(self.text, 1, self.highlight)
        else:
            self.text_image = self.font.render(self.text, 1, (100, 100, 100))
        surface.blit(self.text_image,self.text_pos)
 
    def Update(self, event):
        x,y = event.pos
        px,py,w,h = self.rect
        self.mouseover = False
        if x > px and x < px + w:
            if y > py and y < py + h:
                self.mouseover = True
        if not self.mouseover:
            self.buttondown = False
 
    def MouseDown(self, event):
        if self.mouseover:
            self.buttondown = True
 
    def Click(self, event):
        # let you know when mouse is over button and button was pressed.
        if self.buttondown and self.mouseover:
            self.buttondown = False
 

#Background class.
class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
#Music class.
class Music_Mixer():
    def __init__(self, filename, vol, loops):
        self.filename = pg.mixer.music.load(filename)
        pg.mixer.music.play(loops)
        pg.mixer.music.set_volume(vol)
        print("The music is playing.")
      
#Font function, code taken from reddit post user EricsonWillians modified for use in this game, 
#https://www.reddit.com/r/pygame/comments/278sfa/load_font_which_is_not_a_standard_font/.
def loadCustomFont(filename, size):
    try:
        f = pg.font.Font(filename, size)
        return f
    except:
        print('Cannot load the custom font, does it exist?')
