
import pygame


# TODO:: PhysicsComponent
class AnimationComponent( object ):
        
    animation_component_list = []
    
        
    def __init__( self, image_list, image_description_list ):
    
        self.image_list = []
        self.image_description_list = []
        
        self.current_image_index = 0
        
        for i in range( len( image_list ) ):
            image_path = image_list[ i ]
            img = pygame.image.load( image_path ).convert()
            
            description = image_description_list[ i ]
            
            self.image_list.append( img )
            self.image_description_list.append( description )
        
        self.image_list_size = i + 1
        
        
        AnimationComponent.animation_component_list.append( self )
        
        self.rotated_image = None
        
    
    def SetPhysicsComponent( self, physics_component ):
    
        self.physics_component = physics_component
        
        
    def SetColorKey( self, color = None ):
    
        if ( color == None ):
            color = [ 255, 0, 255 ]
            
        self.image.set_colorkey( color )
        
    
    def ChangeImageTo( self, image_description ):
        
        for i in range( self.image_list_size ):
            if ( self.image_description_list[ i ] == image_description ):
                self.current_image_index = i
        

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
        
        original_image = self.image_list[ self.current_image_index ]
        
        orig_rect = original_image.get_rect()
        rot_image = pygame.transform.rotate( original_image, angle )
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        self.rotated_image = rot_image.subsurface( rot_rect ).copy()
        

def main():
    import gui
    
    game = gui.Gui()
    game.loop()


if __name__ == '__main__':
    main()
        

















