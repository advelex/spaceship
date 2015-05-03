import math
import pygame
import pdb
import time
import os, pathlib

import window
import animations

from sys import platform as _platform

from vector2 import Vector2


class PhysicsComponent():
            
    friction_mult = 0.9995
    
    def __init__( self, location_vector, acceleration_factor = 1.0, max_velocity = 14.0 ):
    
        self.graphics_component = None
        
        self.location = location_vector
        
        self.speed = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        
        self.acceleration_factor = acceleration_factor
        self.max_velocity = max_velocity
        
        self.motors_on = False
        
        
    def SetGraphicsComponent( self, graphics_component ):
    
        self.graphics_component = graphics_component
        
        
    def GetLocation( self ):
    
        return self.location
        
        
    def GetLocationRect( self ):
    
        x = self.location.x
        y = self.location.y
        
        w = 30
        h = 30
        
        return pygame.Rect( x, y, w, h )
        

    def Update( self, delta_time ):
        
        speed = self.speed * PhysicsComponent.friction_mult + ( self.acceleration * delta_time )
        self.speed = speed.ClampMagnitude( self.max_velocity )
        
        self.location = self.location + ( self.speed * delta_time )
        
        # HACK::
        # TODO::
        # README::
        # FIXME::
        # ChangeImageTo() should be in InputManager module untill
        # there's EventManager. PhysicsComponent should not know anything
        # about motors being on or off. These should be changed from
        # EventManager (future implement).
        if self.acceleration.IsZero():
            if self.motors_on is True:
                self.graphics_component.ChangeImageTo( "motors_off" )
                self.motors_on = False
        else:
            if self.motors_on is False:
                self.graphics_component.ChangeImageTo( "motors_on" )
                self.motors_on = True
            
        angle = self.speed.GetAngle() + 180
        self.graphics_component.RotateCenter( angle )
        
        
        if self.location.x > window.Window.size[0]:
            self.location.x = 0
            
        if self.location.x < 0:
            self.location.x = window.Window.size[0]
            
        if self.location.y > window.Window.size[1]:
            self.location.y = 0
            
        if self.location.y < 0:
            self.location.y = window.Window.size[1]
        

def main():
    import gui
    
    game = gui.Gui()
    game.loop()


if __name__ == '__main__':
    main()














