import pygame
import vector2


class InputManager( object ):

    # Initti ottaa parametrin physics_component,
    # jotta sen kiihtyvyyttä voitaisiin muuttaa.

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
                    if not self.key_up:
                        self.physics_component.acceleration.y -= self.physics_component.acceleration_factor
                        self.key_up = True
                        
                if event.key == pygame.K_DOWN:
                    if not self.key_down:
                        self.physics_component.acceleration.y += self.physics_component.acceleration_factor
                        self.key_down = True
                        
                if event.key == pygame.K_LEFT:
                    if not self.key_left:
                        self.physics_component.acceleration.x -= self.physics_component.acceleration_factor
                        self.key_left = True
                    
                if event.key == pygame.K_RIGHT:
                    if not self.key_right:
                        self.physics_component.acceleration.x += self.physics_component.acceleration_factor
                        self.key_right = True

                if event.key == pygame.K_q:
                    return False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if self.key_up:
                        self.physics_component.acceleration.y += self.physics_component.acceleration_factor
                        self.key_up = False
                        
                if event.key == pygame.K_DOWN:
                    if self.key_down:
                        self.physics_component.acceleration.y -= self.physics_component.acceleration_factor
                        self.key_down = False
                        
                if event.key == pygame.K_LEFT:
                    if self.key_left:
                        self.physics_component.acceleration.x += self.physics_component.acceleration_factor
                        self.key_left = False
                        
                if event.key == pygame.K_RIGHT:
                    if self.key_right:
                        self.physics_component.acceleration.x -= self.physics_component.acceleration_factor
                        self.key_right = False
        return True