import pygame as pg
from settings import Music_Mixer, loadCustomFont, States, screen

"""This section contains entity states which are separate from game and menu states."""
class Player(States):
    def __init__(self):
        States.__init__(self)
        self.next = ''
        self.health = 100
        self.speed = 2
        self.screen = screen
        self.rect = pg.draw.rect(self.screen, (255, 0, 0), [900,600,20,45])
        self.image = pg.image.load('ArtWIP/Stickman_stand_still.png').convert_alpha()
        
    def draw(self, screen):
        screen.fill((255, 0, 0))
           
    #Moves the player and begins the animation phase.
    def move_player(self, speed):
        pass
            
    #draws the player to the screen.
    def draw_entity(self):
        screen.blit(self.image, self.rect)
