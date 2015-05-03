import pygame
import os
import pathlib
import sys

from window import Window
from animations import AnimationComponent
from physics import PhysicsComponent
from input_manager import InputManager
from vector2 import Vector2


class Player( object ):
    
    def __init__( self, acceleration_factor = None, max_speed = None ):
    
        super().__init__()
        
        m_img_path = ""
        s_img_path = ""
        
        if sys.platform == "linux" or sys.platform == "linux2":
            m_img_path = str( pathlib.Path('ship_m.png').resolve() )
            s_img_path = str( pathlib.Path('ship_s.png').resolve() )
        else:
            current_path = os.path.dirname( __file__ )
            m_img_path = current_path + '\ship_m.png'
            s_img_path = current_path + '\ship_s.png'
            
            
        start_pos = Vector2( 150, 150 )
        
        self.physics_component = PhysicsComponent( start_pos, acceleration_factor, max_speed )
        
        image_path = m_img_path
        self.graphics = AnimationComponent( image_path, self.physics_component )
        
        self.physics_component.SetGraphicsComponent( self.graphics )
        
        self.input_manager = InputManager( self.physics_component )


class Gui( object ):

    def __init__(self):

        pygame.init()
                
        self.window_size = [ 1800, 950 ]
        self.window = Window( self.window_size )

        acceleration_factor = 7.5
        max_speed = 24.0
        self.ship = Player( acceleration_factor, max_speed )
        
        self.fps = 60
        
        self.clock = pygame.time.Clock()
        self.gui_running = True
        

    def HandleInput(self):
    
        return self.ship.input_manager.CheckInput()


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





















