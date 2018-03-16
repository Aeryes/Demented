import pygame
import os

pygame.init()

"""These are classes that inialize things in the game"""

#Superclass of all states
#Any data you wish to persist between all states would go in here
#Logic that persists between all states would go in here
class States():
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

#Background class.
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
#Music class.
class Music_Mixer():
    def __init__(self, filename, vol, loops):
        self.filename = pygame.mixer.music.load(filename)
        pygame.mixer.music.play(loops)
        pygame.mixer.music.set_volume(vol)
    
"""These are all functions that make the game work well."""   
#Font functions, code taken from reddit post user EricsonWillians, 
#https://www.reddit.com/r/pygame/comments/278sfa/load_font_which_is_not_a_standard_font/.
def loadDefaultFont(size):
    """
    A function to load the default system font (Good for cross-platform games).
    """
    try:
        f = pygame.font.Font(None,size)
    except:
        print("Cannot load the default font")
        raise SystemExit
    return f

def loadCustomFont(filename, size):
    """
    A function to load a custom font from a file.
    """
    f = pygame.font.Font(filename,size)
    return f

def loadSystemFont(name, size):
    """
    A function to load a specific system font (Not good for cross-platform games).
    """
    try:
        f = pygame.font.SysFont(name,size)
    except:
        print("Cannot load font: ", name)
        raise SystemExit
    return f

def getSystemFonts():
    return font.get_fonts()
