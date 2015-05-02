import math
import pygame
import pdb
import time
import event_manager

import os, pathlib
from sys import platform as _platform
from vector2 import Vector2

'''
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_angle(self):
        return math.degrees(math.atan2(self.x, self.y))
'''


class Player(pygame.sprite.Sprite):
    
    '''
    Playerin initti ottaa parametrin acceleration, jota vastasi aiemman toteutuksen Gui.a, 
    mikä oli 0.1
    
    Täällä myös luodaan playerille oma EventManager instanssi, joka vastaa aiempaa
    Gui luokan event_manager metodia.
    '''
    def __init__( self, acceleration ):
        super().__init__()
        
        '''
        TODO::
        Tähän voisi tehdä if-else kohdan, mikä hakis oikean polun riippuen siitä, 
        että mikä käyttöjärjestelmä on.
        '''
        m_img_path = ""
        s_img_path = ""
        
        if _platform == "linux" or _platform == "linux2":
            m_img_path = str( pathlib.Path('ship_m.png').resolve() )
            s_img_path = str( pathlib.Path('ship_s.png').resolve() )
        else:
            current_path = os.path.dirname( __file__ )
            m_img_path = current_path + '\ship_m.png'
            s_img_path = current_path + '\ship_s.png'
        
        self.image_original_m = pygame.image.load( m_img_path ).convert()
        self.image_original_m.set_colorkey(Gui.BLACK)
        self.image_original_s = pygame.image.load( s_img_path ).convert()
        self.image_original_s.set_colorkey(Gui.BLACK)
        self.image = self.image_original_s
        self.rect = self.image.get_rect()

        self.rect.x = 400
        self.rect.y = 300
        self.v = Vector2(0, 0)
        self.a = Vector2(0, 0)
        
        self.acceleration = acceleration

        self.last_time = time.perf_counter()
        
        self.event_manager = event_manager.EventManager( self )


    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
        

    def update(self):
        if self.a.x != 0 or self.a.y != 0:
            #self.image = self.rot_center(self.image_original_m, self.v.get_angle()+180)
            self.image = self.rot_center( self.image_original_m, self.v.GetAngle()+180 )
        else:
            #self.image = self.rot_center(self.image_original_s, self.v.get_angle()+180)
            self.image = self.rot_center( self.image_original_s, self.v.GetAngle()+180 )

        current_time = time.perf_counter()
        delta_time = (current_time-self.last_time) * 100
        self.last_time = current_time
        
        self.v = self.v + self.a * delta_time
        '''
        self.v.x += self.a.x*delta_time
        self.v.y += self.a.y*delta_time
        '''
        self.rect.x += self.v.x*delta_time
        self.rect.y += self.v.y*delta_time

        if self.rect.x > Gui.WINDOW_SIZE[0]:
            self.rect.x = -1
        if self.rect.x < -1:
            self.rect.x = Gui.WINDOW_SIZE[0]
        if self.rect.y > Gui.WINDOW_SIZE[1]:
            self.rect.y = -1
        if self.rect.y < -1:
            self.rect.y = Gui.WINDOW_SIZE[1]



class Gui:

    WINDOW_SIZE = [800, 600]

    # Colors
    BLACK = (0, 0 ,0)
    WHITE = (255, 255, 255)
    RED = (255, 0 ,0)
    
    '''
    Aiemmin täällä oli muuttuja self.ai, nyt se on korvattu acceleration
    nimisellä muuttujalla, joka annetaan playerille parametrinä.
    '''
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption('Spaceship Simulation')

        acceleration = 0.1
        self.ship = Player( acceleration )
        
        self.fps = 60
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)
        self.clock = pygame.time.Clock()
        self.gui_running = True
        

    def HandleInput(self):
        return self.ship.event_manager.CheckInput()


    def update_logic(self):
        self.ship.update()
        

    def update_grafics(self):
        self.screen.fill(self.BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


    def loop(self):

        while self.gui_running:
            
            self.gui_running = self.HandleInput()
            self.update_logic()
            self.update_grafics()
            self.clock.tick(self.fps)

        pygame.quit()



def main():
    # pdb.set_trace()
    game = Gui()
    game.loop()

if __name__ == '__main__':
    main()





















