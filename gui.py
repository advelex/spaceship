import math
import pygame
import pdb
import time
import os, pathlib

import window
import animations

from physics import PhysicsComponent

#Tällä saadaan tietää mikä käyttöjärjestelmä on tällä hetkellä.
from sys import platform as _platform

from vector2 import Vector2


class EventManager( object ):

    def __init__( self, physics_component ):
    
        self.key_up = False
        self.key_down = False
        self.key_left = False
        self.key_right = False
        
        self.physics_component = physics_component
    
    def CheckInput( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.key_up:
                        pass
                    else:
                        self.physics_component.acceleration.y -= self.physics_component.acceleration_factor
                        self.key_up = True
                        
                if event.key == pygame.K_DOWN:
                    if self.key_down:
                        pass
                    else:
                        self.physics_component.acceleration.y += self.physics_component.acceleration_factor
                        self.key_down = True
                        
                if event.key == pygame.K_LEFT:
                    if self.key_left:
                        pass
                    else:
                        self.physics_component.acceleration.x -= self.physics_component.acceleration_factor
                        self.key_left = True
                    
                if event.key == pygame.K_RIGHT:
                    if self.key_right:
                        pass
                    else:
                        self.physics_component.acceleration.x += self.physics_component.acceleration_factor
                        self.key_right = True

                if event.key == pygame.K_q:
                    return False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if self.key_up:
                        self.physics_component.acceleration.y += self.physics_component.acceleration_factor
                        self.key_up = False
                    else:
                        pass
                        
                if event.key == pygame.K_DOWN:
                    if self.key_down:
                        self.physics_component.acceleration.y -= self.physics_component.acceleration_factor
                        self.key_down = False
                    else:
                        pass
                        
                if event.key == pygame.K_LEFT:
                    if self.key_left:
                        self.physics_component.acceleration.x += self.physics_component.acceleration_factor
                        self.key_left = False
                    else:
                        pass
                        
                if event.key == pygame.K_RIGHT:
                    if self.key_right:
                        self.physics_component.acceleration.x -= self.physics_component.acceleration_factor
                        self.key_right = False
                    else:
                        pass
        return True


class Player():

    
    def __init__( self, acceleration_factor ):
    
        super().__init__()
        
        m_img_path = ""
        s_img_path = ""
        
        if _platform == "linux" or _platform == "linux2":
            m_img_path = str( pathlib.Path('ship_m.png').resolve() )
            s_img_path = str( pathlib.Path('ship_s.png').resolve() )
        else:
            current_path = os.path.dirname( __file__ )
            m_img_path = current_path + '\ship_m.png'
            s_img_path = current_path + '\ship_s.png'
            
            
        start_pos = Vector2( 150, 150 )
        
        self.physics_component = PhysicsComponent( start_pos, acceleration_factor )
        
        image_path = m_img_path
        self.graphics = animations.AnimationComponent( image_path, self.physics_component )
        
        self.physics_component.SetGraphicsComponent( self.graphics )
        
        self.event_manager = EventManager( self.physics_component )



class Gui:


    def __init__(self):

        pygame.init()
                
        self.window_size = [ 1000, 750 ]
        self.window = window.Window( self.window_size )

        acceleration_factor = 0.5
        self.ship = Player( acceleration_factor )
        
        self.fps = 60
        
        self.clock = pygame.time.Clock()
        self.gui_running = True
        

    def HandleInput(self):
    
        return self.ship.event_manager.CheckInput()


    def loop(self):

        while self.gui_running:
            
            self.gui_running = self.HandleInput()
            
            self.ship.physics_component.Update( 1.0 / self.fps )
            
            self.window.RenderAll()
            
            #self.clock.tick( 60*1000 )

        pygame.quit()



def main():

    # pdb.set_trace()
    game = Gui()
    game.loop()
    

if __name__ == '__main__':
    main()





















