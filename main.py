import pygame
import sys
from settings import Settings, Background, Music_Mixer, loadCustomFont

pygame.init() 

game_settings = Settings()
screen_size = game_settings.WIDTH, game_settings.HEIGHT   
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN ) 
clock = pygame.time.Clock()

#Main menu button class. Thank you to Github user ohdqueezy for this code.
#https://gist.github.com/ohsqueezy/2802185 , modified to work for my game.
class Button():

    hovered = False
    
    def __init__(self, text, pos, size):
        self.text = text
        self.pos = pos
        self.size = size
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = loadCustomFont('Fonts/Amatic_SC/amatic_sc.ttf', self.size).render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

#Loading game music.
Menu_Music = Music_Mixer('Music/menu.mp3', 0.2, -1)

#Loading Main Menu Background Images and stuff.
menu_options_quit = Button("Quit", (900, 900), 72)
menu_options_settings = Button('Settings', (865, 800), 72)
menu_options_play = Button('Play', (900, 700), 72)

Menu_Background = Background('Images/Screen_bgs/menu_bg.jpg', (0,0))
Menu_Title_Screen = Background('Images/Screen_bgs/menu_title.png',(700,200))

def menuloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
 
        #Logic for quit button.
        if menu_options_quit.rect.collidepoint(pygame.mouse.get_pos()):
            menu_options_quit.hovered = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sys.exit()
        else:
            menu_options_quit.hovered = False
        
        
        #Logic for play button.
        if menu_options_play.rect.collidepoint(pygame.mouse.get_pos()):
            menu_options_play.hovered = True
        else:
            menu_options_play.hovered = False
            
        #Settings button logic
        if menu_options_settings.rect.collidepoint(pygame.mouse.get_pos()):
            menu_options_settings.hovered = True
        else:
            menu_options_settings.hovered = False
            
        #Draw to the screen.
        menu_options_quit.draw()
        menu_options_play.draw()
        menu_options_settings.draw()
        
        pygame.display.update()
        screen.fill([255, 255, 255])
        screen.blit(Menu_Background.image, Menu_Background.rect)
        screen.blit(Menu_Title_Screen.image, Menu_Title_Screen.rect)
        
        clock.tick(24)

menuloop()
