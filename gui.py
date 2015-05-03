import pygame

from window import Window
from graphics import GraphicsComponent
from physics import PhysicsComponent
from input_manager import InputManager
from vector2 import Vector2
from string_to_directory import StringToDirectory


class Player( object ):
    
    def __init__( self, acceleration_factor = None, max_speed = None ):
    
        super().__init__()
        
        
        start_pos = Vector2( 150, 150 )
        self.physics_component = PhysicsComponent( start_pos, acceleration_factor, max_speed )
        
        self.graphics_component = GraphicsComponent()
        
        self.graphics_component.SetPhysicsComponent( self.physics_component )
        self.physics_component.SetGraphicsComponent( self.graphics_component )
        
        
        self.input_manager = InputManager( self.physics_component )
        
            
        image_list_motors_off = []
        
        image_list_motors_off.append( StringToDirectory.Get( "ship_motors_off.png" ) )
        
        image_description_motors_off = "motors_off"
        
        self.graphics_component.AddAnimation( image_list_motors_off, image_description_motors_off )
        
        
        image_list_motors_on = []
        
        for i in range( 3 ):
            path_name = "ship_motors_on_" + str( i ) + ".png"
            image_list_motors_on.append( StringToDirectory.Get( path_name ) )
            
        image_description_motors_on = "motors_on"
        
        self.graphics_component.AddAnimation( image_list_motors_on, image_description_motors_on )


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





















