import pygame as pg

'''Player animations and pictures.'''
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
STICKMAN_IDLE = [stick_still]
STICKMAN_RUN_RIGHT = [stick_run_1_right, stick_run_2_right, stick_run_5_right, stick_run_3_right, stick_run_4_right]
STICKMAN_RUN_LEFT = [stick_run_1_left, stick_run_2_left, stick_run_5_left, stick_run_3_left, stick_run_4_left]

'''Platform animations and pictures.'''
platform_one = pg.image.load('Images/Animations/Platforms/platform1.png').convert_alpha()


PLATFORM_STAGE_ONE = [platform_one]
