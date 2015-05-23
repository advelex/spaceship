import pygame
import os
import sys

from window import Window
from animations import AnimationComponent
from physics import PhysicsComponent
from input_manager import InputManager
from vector2 import Vector2


class Player( object ):
    
    def __init__( self, acceleration_factor = None, max_speed = None ):
    
        super().__init__()
        
        image_motors_on_path = ""
        image_motors_off_path = ""
        current_path = os.path.dirname( __file__ )

        if sys.platform == "linux" or sys.platform == "linux2":
            directory_separator = '/'
        else:
            directory_separator = '\\'
            
        image_motors_on_path = current_path + directory_separator + 'ship_motors_on.png'
        image_motors_off_path = current_path + directory_separator + 'ship_motors_off.png'
            
        start_pos = Vector2( 150, 150 )
        self.physics_component = PhysicsComponent( start_pos, acceleration_factor, max_speed )
        
        image_list = [ image_motors_on_path, image_motors_off_path ]
        image_description_list = [ "motors_on", "motors_off" ]
        self.graphics_component = AnimationComponent( image_list, image_description_list )
        
        self.graphics_component.SetPhysicsComponent( self.physics_component )
        self.physics_component.SetGraphicsComponent( self.graphics_component )
        
        self.input_manager = InputManager( self.physics_component )


class Gui( object ):

    def __init__(self):

        pygame.init()
                
        self.window_size = [ 1750, 900 ]
        self.window = Window( self.window_size )

        acceleration_factor = 10.0
        max_speed = 50.0
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





















