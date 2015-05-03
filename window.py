
#import sys, time, pygame
import pygame

from animations import AnimationComponent


class Window( object ):

        size = [ 0, 0 ]
        background_color = [ 255, 0, 255 ]
        
                
        def __init__( self, newSize = None ):
        
                if ( newSize is None ):
                        newSize = [ 640, 480 ]
                        
                Window.size = newSize
        
                self.window = pygame.display.set_mode( Window.size )
                
                pygame.display.set_caption( "Spaceship Simulation" )
                
                self.black = [ 0, 0, 0 ]

                
        def RenderAll( self ):
        
                self.window.fill( self.black )
                
                AnimationComponent.ListRender( self.window )
                        
                pygame.display.flip()
        
        
        
        
        
        
        
        
        