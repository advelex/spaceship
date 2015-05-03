
import pygame


# TODO:: PhysicsComponent
class AnimationComponent( object ):
        
    animation_component_list = []
    
        
    def __init__( self, image_path, physics_component ):
        
        self.image = pygame.image.load( image_path ).convert()
        
        self.physics_component = physics_component
        
        AnimationComponent.animation_component_list.append( self )
        
        self.rotated_image = None
        
        
    def SetColorKey( self, color = None ):
    
        if ( color == None ):
            color = [ 255, 0, 255 ]
            
        self.image.set_colorkey( color )
        

    def ListRender( window ):
    
        anim_list = AnimationComponent.animation_component_list
        
        list_size = len( anim_list )
        
        for i in range( list_size ):
            anim_list[ i ].Render( window )
        

    def Render( self, window ):

        w = 30
        h = 30
        
        location_rect = self.physics_component.GetLocationRect()
        window.blit( self.rotated_image, location_rect )
        

    def RotateCenter( self, angle ):
        
        orig_rect = self.image.get_rect()
        rot_image = pygame.transform.rotate( self.image, angle )
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        self.rotated_image = rot_image.subsurface( rot_rect ).copy()
        

















