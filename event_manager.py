import pygame
import vector2


class EventManager( object ):
    
    '''
    Initti ottaa parametrin player, jotta se voisi muuttaa tämän kiihtyvyyttä.
    '''
    def __init__( self, player ):
    
        self.key_up = False
        self.key_down = False
        self.key_left = False
        self.key_right = False
        
        self.player = player
        
    
    def CheckInput( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.key_up:
                        pass
                    else:
                        self.player.a.y -= self.player.acceleration
                        self.key_up = True
                        
                if event.key == pygame.K_DOWN:
                    if self.key_down:
                        pass
                    else:
                        self.player.a.y += self.player.acceleration
                        self.key_down = True
                        
                if event.key == pygame.K_LEFT:
                    if self.key_left:
                        pass
                    else:
                        self.player.a.x -= self.player.acceleration
                        self.key_left = True
                    
                if event.key == pygame.K_RIGHT:
                    if self.key_right:
                        pass
                    else:
                        self.player.a.x += self.player.acceleration
                        self.key_right = True

                if event.key == pygame.K_q:
                    return False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if self.key_up:
                        self.player.a.y += self.player.acceleration
                        self.key_up = False
                    else:
                        pass
                        
                if event.key == pygame.K_DOWN:
                    if self.key_down:
                        self.player.a.y -= self.player.acceleration
                        self.key_down = False
                    else:
                        pass
                        
                if event.key == pygame.K_LEFT:
                    if self.key_left:
                        self.player.a.x += self.player.acceleration
                        self.key_left = False
                    else:
                        pass
                        
                if event.key == pygame.K_RIGHT:
                    if self.key_right:
                        self.player.a.x -= self.player.acceleration
                        self.key_right = False
                    else:
                        pass
        return True
