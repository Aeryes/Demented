import pygame as pg
from mainmenu import MainMenu, GameOver
from game import Game
from settings import Music_Mixer, loadCustomFont, States, screen
import sys

screen_size = screen
        
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
    def __init__(self):
        self.done = False
        self.clock = pg.time.Clock()
        self.screen = screen_size
        
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
            delta_time = self.clock.tick(60)/1000
            self.event_loop()
            self.update(delta_time)
            pg.display.update()
 
#Settings from above dictionary get passed into Control class
#Control creates app object.
#Then, each state (Menu & Game) object get assigned to a dicitonary.
#This allows control to be able to switch to and from any state as needed.
app = Control()
 
#State Dictionary. Include all state classes here.
state_dict = {'mainmenu': MainMenu(),
              'game': Game(),
              'gameover' : GameOver()}
 
#Setup State is called and sets the initial state of the program
app.setup_states(state_dict, 'mainmenu')
 
#Call main game loop that runs whole program
app.main_game_loop()
 
pg.quit()
sys.exit()
