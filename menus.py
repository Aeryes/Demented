import pygame
 
# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WIDTH = 800
HEIGHT = 800
 
 
class Menu():
    """ Base menu object """
 
    def __init__(self, screen, title, title_color, menu_font_type, bg_color):
        self.screen = screen
        self.title = title
        self.title_color = title_color
        self.font_type = menu_font_type
        self.bg_color = bg_color
        self.title_font_size = int(HEIGHT / 10)
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        self.buttons = []
 
    def add_button(self, action, width, height, bg_color, text, text_color, center_x, center_y):
        """ Add a button to the menu """
        new_button = Button(self, action, width, height, bg_color,
                            text, self.font_type, text_color, center_x, center_y)
        self.buttons.append(new_button)
 
    def is_button_clicked(self, mouse_pos):
        for button in self.buttons:
            if button.is_hovered(mouse_pos[0], mouse_pos[1]):
                return button.get_action()
        action = "None"
        return action
 
    def draw(self):
        """ Draw the menu surface and then blit to screen """
        # Fill menu surface with background color
        self.surface.fill(self.bg_color)
        # Draw menu title
        font = pygame.font.SysFont(self.font_type, self.title_font_size)
        title = font.render(self.title, 1, self.title_color)
        render_size = font.size(self.title)
        x_offset = render_size[0] / 2
        y_offset = render_size[1] / 2
        title_center_x = WIDTH / 2 - x_offset
        title_center_y = HEIGHT / 8 - y_offset
        self.surface.blit(title, (title_center_x, title_center_y))
 
        # get mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Draw all menu buttons
        for button in self.buttons:
            # Call is_hovered function to check for hover
            # which will change button color if true
            button.is_hovered(mouse_pos[0], mouse_pos[1])
            # Draw button
            button.draw()
 
        # Blit menu surface to screen
        self.screen.blit(self.surface, (0, 0))
 
 
class Button():
    """ Base button object """
 
    def __init__(self, menu, action, width, height, bg_color, text, font_type, text_color, center_x, center_y):
        self.menu = menu
        self.action = action
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text = text
        self.text_color = text_color
        # set the font size to 1/2 the button height
        self.font_size = int(height / 2)
        self.font = pygame.font.SysFont(font_type, self.font_size)
        self.center_x = center_x
        self.center_y = center_y
        self.surface = pygame.Surface((width, height))
        self.draw()
 
    def get_action(self):
        return self.action
 
    def insert_text(self):
        """ Insert text onto button surface """
        text_render = self.font.render(self.text, 1, self.text_color)
        text_render_size = self.font.size(self.text)
        x_offset = text_render_size[0] / 2
        y_offset = text_render_size[1] / 2
        self.surface.blit(text_render, (self.surface.get_width(
        ) / 2 - x_offset, self.surface.get_height() / 2 - y_offset))
 
    def is_hovered(self, mx, my):
        if (mx > self.center_x - self.width / 2 and mx < self.center_x + self.width / 2):
            if (my > self.center_y - self.height / 2 and my < self.center_y + self.height / 2):
                self.bg_color = GREEN
                return True
        self.bg_color = WHITE
        return False
 
    def draw(self):
        self.surface.fill(self.bg_color)
        self.insert_text()
        self.menu.surface.blit(
            self.surface, (self.center_x - self.width / 2, self.center_y - self.height / 2))
 
 
def main():
    """ Main function for the game. """
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")
    done = False
    clock = pygame.time.Clock()
 
    ### Menu Creation ###
    main_menu = Menu(screen, "Main Menu", WHITE, "tahoma", BLACK)
 
    main_menu.add_button("Settings", 200, 100, WHITE, str(
        "Settings"), BLACK, WIDTH / 2, (2 * HEIGHT / 4))
 
    main_menu.add_button("Quit", 200, 100, WHITE, str(
        "Quit"), BLACK, WIDTH / 2, (3 * HEIGHT / 4))
 
    settings_menu = Menu(screen, "Settings", WHITE, "tahoma", BLACK)
 
    settings_menu.add_button("Main Menu", 300, 100, WHITE, str(
        "Main Menu"), BLACK, WIDTH / 2, HEIGHT / 2)
 
    # Assign starting menu
    menu = main_menu # NOTE: set to None for no starting menu
 
    ### Main Game Loop ###
    while not done:
        # Update mouse location
        mouse_pos = pygame.mouse.get_pos()
 
        ### Event Loop  ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # window is closed
                done = True
 
            elif event.type == pygame.KEYDOWN:
                # press esc key to return to main menu
                if event.key == pygame.K_ESCAPE:
                    if menu == main_menu:
                        menu = None
                    else:
                        menu = main_menu
            elif event.type == pygame.MOUSEBUTTONUP and menu:
                action = menu.is_button_clicked(mouse_pos)
                if action == "Quit":
                    done = True
                elif action == "Settings":
                    menu = settings_menu
                elif action == "Main Menu":
                    menu = main_menu
 
        ### Update Game ###
        if not menu:  
            #---- game update code ----#
            pass # NOTE: remove line once update code added
 
        ### Draw  Game ###
        screen.fill(WHITE)  # clear screen
 
        # check if there is currently a menu selected
        if menu:
            menu.draw()
        else:
            #---- game draw code ----#
            pass # NOTE: remove line once draw code added
 
        # display the screen
        pygame.display.flip()
 
        # delay in miliseconds until next frame
        clock.tick(24)
 
 
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    main()
    pygame.font.quit()
    pygame.quit()
