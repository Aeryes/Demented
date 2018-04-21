import pygame as pg
from settings import Music_Mixer, loadCustomFont, States, screen, GROUND_HEIGHT
from time import sleep
 
"""This section contains entity states which are separate from game and menu states."""
class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.health = 100
        self.speed = 1
        self.screen = screen
       
        self.pos_x = x
        self.pos_y = y
        self.vel_x = 0
        self.vel_y = 15
       
        self.running_right = False
        self.running_left = False
        self.is_jumping = False
        self.jump_count = 0
        
        self.mass = 3
       
        #List of pictures for animations.
        stick_still = pg.image.load('Images/Animations/PlayerRun/Stickman_stand_still.png').convert_alpha()
        stick_still_2 = pg.image.load('Images/Animations/PlayerRun/Stickman_stand_still_2.png').convert_alpha()
       
        #Right running pictures.
        stick_run_1_right = pg.image.load('Images/Animations/PlayerRun/Stickman_run_1.png').convert_alpha()
        stick_run_2_right = pg.image.load('Images/Animations/PlayerRun/Stickman_run_2.png').convert_alpha()
        stick_run_3_right = pg.image.load('Images/Animations/PlayerRun/Stickman_run_3.png').convert_alpha()
        stick_run_4_right = pg.image.load('Images/Animations/PlayerRun/Stickman_run_4.png').convert_alpha()
        stick_run_5_right = pg.image.load('Images/Animations/PlayerRun/Stickman_run_4.png').convert_alpha()
       
        #Left running pictures.
        stick_run_1_left = pg.image.load('Images/Animations/PlayerRun/Stickman_run_1_left.png').convert_alpha()
        stick_run_2_left = pg.image.load('Images/Animations/PlayerRun/Stickman_run_2_left.png').convert_alpha()
        stick_run_3_left = pg.image.load('Images/Animations/PlayerRun/Stickman_run_3_left.png').convert_alpha()
        stick_run_4_left = pg.image.load('Images/Animations/PlayerRun/Stickman_run_4_left.png').convert_alpha()
        stick_run_5_left = pg.image.load('Images/Animations/PlayerRun/Stickman_run_4_left.png').convert_alpha()
       
        #Lists for animation movement.
        self.STICKMAN_IDLE = [stick_still]
        self.STICKMAN_RUN_RIGHT = [stick_run_1_right, stick_run_2_right, stick_run_5_right, stick_run_3_right, stick_run_4_right]
        self.STICKMAN_RUN_LEFT = [stick_run_1_left, stick_run_2_left, stick_run_5_left, stick_run_3_left, stick_run_4_left]
                       
                       
        self.images = self.STICKMAN_IDLE
        self.image = self.images[0]
       
        self.rect = self.image.get_rect(center=(x, y))
       
        self.anim_index = 0
        self.anim_timer = 0
        self.ms = 0
       
    #Moves the player and begins the animation phase.
    def move_player(self, dt):
        self.pressed = pg.key.get_pressed()
        
        if self.vel_x > 5:
            self.vel_x = 5
        if self.vel_x < -5:
            self.vel_x = -5
       
        if self.pressed[pg.K_a]:
            self.running_left = True
            if self.running_left:
                    if self.vel_x > 0:
                        self.vel_x = 0
                    self.vel_x -= 0.5
                    self.pos_x += self.vel_x  # Move left.
                    self.ms = 0.07
                    self.images = self.STICKMAN_RUN_LEFT  # Change the animation.
        if self.pressed[pg.K_d]:
            self.running_right = True
            if self.running_right:
                    if self.vel_x < 0:
                        self.vel_x = 0
                    self.vel_x += 0.5
                    self.pos_x += self.vel_x  # Move right.
                    self.ms = 0.07
                    self.images = self.STICKMAN_RUN_RIGHT  # Change the animation.
        if not self.pressed[pg.K_d] and not self.pressed[pg.K_a]:
            self.images = self.STICKMAN_IDLE  # Change the animation.
            self.ms = 0.07
        if self.pressed[pg.K_w] and self.jump_count < 6:
            self.jump_count += 1
            self.is_jumping = True
            self.vel_y = -15
            print(self.jump_count)
        elif self.jump_count >= 6:
            print('You cannot jump that much... chill...')
            self.jump_count = 0
            if self.jump_count < 6:
                pass
                   
        # Update the rect because it's used to blit the image.
        self.rect.center = self.pos_x, self.pos_y
   
    #Makes the player jump.
    def jumping(self, dt):
        if self.is_jumping:
            #Calculate force.
            F = (0.5 * self.mass * (self.vel_y))
           
            #Change position.
            self.pos_y = self.pos_y + F
            self.rect.y = self.rect.y + F
           
            #Change velocity.
            self.vel_y = self.vel_y + 1
           
            if self.pos_y >= GROUND_HEIGHT:
                self.pos_y = GROUND_HEIGHT
                self.is_jumping = False
                self.vel_y = 0
   
    #Checks for collision.
    def is_collided_with(self, l):
        for wall in l:
            if self.rect.colliderect(wall.rect):
                if self.vel_x > 0:
                    self.rect.right = wall.rect.left
 
                elif self.vel_x < 0:
                    self.rect.left = wall.rect.right
            self.pos_x = self.rect.center[0]
            self.pos_y = self.rect.center[1]
 
    def is_collided_with2(self, l):
        for wall in l:
            if self.rect.colliderect(wall.rect):
                if self.vel_y > 0:
                    self.rect.bottom = wall.rect.top
                    self.vel_y = 0
 
                elif self.vel_y < 0:
                    self.rect.top = wall.rect.bottom
                    self.vel_y = 0
            self.pos_x = self.rect.center[0]
            self.pos_y = self.rect.center[1]
 
    #Animates the running movement of the player.
    def runAnim(self, dt):
        # Add the delta time to the anim_timer and increment the
        # index after 70 ms.
        self.anim_timer += dt
               
        if self.anim_timer > self.ms:
            self.anim_timer = 0  # Reset the timer.
            self.anim_index += 1  # Increment the index.
            self.anim_index %= len(self.images)  # Modulo to cycle the index.
            self.image = self.images[self.anim_index]  # And switch the image.
 
    #draws the player to the screen.
    def draw_entity(self):
        screen.blit(self.image, self.rect)
 
#Creates platforms that the user can jump onto.
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
       
        self.moving = False
       
        self.image = None
        self.rect = pg.Rect(x, y, 150, 200)
       
    #draws the platform to the screen.
    def draw_plat(self):
        pg.draw.rect(screen, (0,0,0), self.rect)
