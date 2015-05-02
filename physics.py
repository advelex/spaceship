import math
import pygame
import pdb
import time
import os, pathlib

import window
import animations

#Tällä saadaan tietää mikä käyttöjärjestelmä on tällä hetkellä.
from sys import platform as _platform

from vector2 import Vector2


class PhysicsComponent():

    
    def __init__( self, location_vector = None, acceleration_factor = 1.0 ):
    
        self.graphics_component = None
        
        self.location = location_vector
        
        if ( location_vector == None ):
            self.location = Vector2( 150, 150 )
        
        self.speed = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        
        self.acceleration_factor = acceleration_factor
        
        
    def SetGraphicsComponent( self, graphics_component ):
    
        self.graphics_component = graphics_component
        
        
    def GetLocation( self ):
    
        return self.location
        
        
    def GetLocationRect( self ):
    
        x = self.location.x
        y = self.location.y
        
        w = 30
        h = 30
        
        rect = pygame.Rect( x, y, w, h )
        return rect
        

    def Update( self, delta_time ):
    
        # if self.acceleration.x != 0 or self.acceleration.y != 0:
            # self.graphics_component.RotateCenter( self.speed.GetAngle()+180 )
        # else:
            # self.graphics_component.RotateCenter( self.speed.GetAngle()+180 )
        
        self.graphics_component.RotateCenter( self.speed.GetAngle() + 180 )
        
        self.speed = self.speed + self.acceleration * delta_time
        
        self.location = self.location + self.speed * delta_time

        if self.location.x > window.Window.size[0]:
            self.location.x = -1
        if self.location.x < -1:
            self.location.x = window.Window.size[0]
        if self.location.y > window.Window.size[1]:
            self.location.y = -1
        if self.location.y < -1:
            self.location.y = window.Window.size[1]
        



def main():
    pass

if __name__ == '__main__':
    main()





















