import pygame
import sys
from settings import Settings, Background, Music_Mixer, loadCustomFont

game_settings = Settings()
screen = pygame.display.set_mode((game_settings.WIDTH, game_settings.HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Demented')
clock = pygame.time.Clock()

#This class deals with the creation of game menus.
class Menu():
    def __init__(self, screen):
        self.screen = screen
        pos = pygame.mouse.get_pos()
        self.buttons = []
        
    """Draws the background image of the menu"""
    def draw_bg(self, bg_image, bg_loc):
        Menu_BG = Background(bg_image, bg_loc)
        self.screen.blit(Menu_BG.image, Menu_BG.rect )
        
    """Adds buttons to the menu."""
    def add_button(self, text, pos, size):
        new_button = Button(text, pos, size)
        self.buttons.append(new_button)

    """Tells if a button is pressed and completes actions."""
    def is_pressed(self):
        for button in self.buttons:
            if button.is_hovered():
                pass
                
    """Draws the menu buttons etc."""
    def draw(self):
        for button in self.buttons:
            button.draw()

#Main menu button class. Thank you to Github user ohdqueezy for this code.
#https://gist.github.com/ohsqueezy/2802185 , modified to work for my game.
class Button():
    
    hovered = False
    
    def __init__(self, text, pos, size):
        self.screen = screen
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
        self.rect.topleft = (self.pos)
        
    def is_hovered(self):
            self.hovered = True
        
def mainloop():
    """ Main functions for the game. """
    done = False
    
    #Constants.
    WIDTH = game_settings.WIDTH
    HEIGHT = game_settings.HEIGHT
    
    #Loading game music.
    Menu_Music = Music_Mixer('Music/menu.mp3', 0.1, -1)
    
    #Creating the menus for the game.
    main_menu = Menu(screen)
    settings_menu = Menu(screen)
    
    #Assigning the starting menu.
    menu = main_menu
    
    """Main event loop."""
    while not done:
        
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True
                
        #Main menu code.
        if menu == main_menu:
            main_menu.draw_bg('Images/Screen_bgs/menu_bg.jpg', (0,0))
            main_menu.add_button('Play', (900,700), 72)
            main_menu.add_button('Settings', (865,800), 72)
            main_menu.add_button("Quit", (900,900), 72)
            
            #Hovering logic.
            if main_menu.buttons[0].rect.collidepoint(pygame.mouse.get_pos()):
                main_menu.buttons[0].hovered = True
                main_menu.buttons[0].draw()
            elif main_menu.buttons[1].rect.collidepoint(pygame.mouse.get_pos()):
                main_menu.buttons[1].hovered = True
                main_menu.buttons[1].draw()
            elif main_menu.buttons[2].rect.collidepoint(pygame.mouse.get_pos()):             
                main_menu.buttons[2].hovered = True
                main_menu.buttons[2].draw()
                
        #Settings menu code.
        elif menu == settings_menu:
            settings_menu.draw_bg('Images/Screen_bgs/menu_bg.jpg', (0,0))
            settings_menu.add_button('Video', (900,700), 72)
            
        # display the screen
        pygame.display.flip()
        
        #Clock object.
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    mainloop()
