import pygame
import time

class GraphicsComponent( object ):
        
    animation_component_list = []
    
        
    def __init__( self, image_path_list, description ):
    
        self.animation = Animation( image_path_list, description )
        
        GraphicsComponent.animation_component_list.append( self )
        
        self.rotated_image = None
        
        
    
    def SetPhysicsComponent( self, physics_component ):
    
        self.physics_component = physics_component
        
        
    def SetColorKey( self, color = None ):
    
        if ( color == None ):
            color = [ 255, 0, 255 ]
            
        return
        # FIXME
        #self.image.set_colorkey( color )
        
    
    def ChangeImageTo( self, image_description ):
        
        # FIXME
        return
        
        for i in range( self.image_list_size ):
            if ( self.image_description_list[ i ] == image_description ):
                self.current_image_index = i
        

    def ListRender( window ):
    
        anim_list = GraphicsComponent.animation_component_list
        
        list_size = len( anim_list )
        
        for i in range( list_size ):
            anim_list[ i ].Render( window )
        

    def Render( self, window ):
    
        location_rect = self.physics_component.GetLocationRect()
        # FIXME
        self.animation.Render( location_rect, window )
        

    def RotateCenter( self, angle ):
    
        self.animation.RotateCenter( angle )
        

class Animation( object ):
    
    def __init__( self, image_path_list, description = "none", s_per_frame = 0.1 ):
    
        self.image_list = []
        self.description = str( description )
        self.s_per_frame = s_per_frame
        self.current_image_index = 0
        self.rotated_current_images = []
        self.last_time = 0
        
        list_size = len( image_path_list )
        
        for i in range( list_size ):
        
            image_path = image_path_list[ i ]
            img = pygame.image.load( image_path ).convert()
            self.image_list.append( img )
        
        self.max_index = i
        
    
    def Render( self, location_rect, window ):
        
        self.CheckCorrectFrame()
        
        img = self.rotated_current_images[ self.current_image_index ]
        window.blit( img, location_rect )
        
        
    def CheckCorrectFrame( self ):
        current_time = time.time()
        
        difference = current_time - self.last_time
        
        if ( difference > self.s_per_frame ):
        
            # Set new self.last_time
            self.last_time = current_time
            
            # Increment image index
            self.current_image_index += 1
            
            if ( self.current_image_index > self.max_index ):
                self.current_image_index = 0

        
    def RotateCenter( self, angle ):
    
        # Rotates all images in self.image_list to this angle and puts
        # them to self.rotated_current_images list.
    
        list_size = len( self.image_list )
        
        self.rotated_current_images = []
        
        for i in range( list_size ):
        
            original_image = self.image_list[ i ]
            
            orig_rect = original_image.get_rect()
            rot_image = pygame.transform.rotate( original_image, angle )
            rot_rect = orig_rect.copy()
            rot_rect.center = rot_image.get_rect().center
            rotated_image = rot_image.subsurface( rot_rect ).copy()
            
            self.rotated_current_images.append( rotated_image )
        
        
def main():
    import gui
    
    game = gui.Gui()
    game.loop()


if __name__ == '__main__':
    main()
        

















