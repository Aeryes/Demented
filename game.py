import pygame as pg
import random
from settings import Music_Mixer, loadCustomFont, States, screen, WIDTH, HEIGHT
from entities import Player, Platform
 
#Subclass of States
#Can make subclasses of the subclass
#Used to load game assets and do runtime stuff.
 
#Level One of the game.
class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'gameover'
        self.player = Player(self)
        self.platforms = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.player)
        self.PLATFORM_LIST = [Platform(0, HEIGHT - 40, WIDTH, 40), Platform(950, 850, 100, 10), Platform(950, 650, 100, 10), 
                 Platform(950, 450, 100, 10), Platform(950, 250, 100, 10), Platform(950, 50, 100, 10)]
        self.create_plat()
        self.score = 0
        
    def cleanup(self):
        print('cleaning up Game Level One state stuff')
       
    def startup(self):
        print('starting Game Level One state stuff')
       
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Game Level One State keydown')
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.mixer.music.play()
            self.done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.player.jump()
               
    def update(self, screen, dt):
        self.draw(screen)
        self.player.update()
        
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
    
        #Scrolling functionality.
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10
        
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        
        if len(self.platforms) == 0:
            self.done = True
                
        #Spawn new platforms.
        while len(self.platforms) < 10:
            width = random.randrange(50, 150)
            p = Platform(random.randrange(0, WIDTH-width), random.randrange(-75, -30), width, 10)
            self.platforms.add(p)
            self.all_sprites.add(p)
                
   
    def create_plat(self):
        for platform in self.PLATFORM_LIST:
            self.platforms.add(platform)
            self.all_sprites.add(platform)
    
    def draw_text(self, text, size, color, x, y):
        self.font = loadCustomFont('Fonts/Amatic_SC/amatic_sc.ttf', 72)
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
    
    def draw(self, screen):
        screen.fill((255, 255, 0))
       
        #Move and draw the player.
        self.player.draw()
       
        #Draw the test platform.
        for plat in self.platforms:
            plat.draw()
            
        self.draw_text(str(self.score), 12, (0,0,0), 50, 10)
