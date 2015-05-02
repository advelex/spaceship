
import sys, pygame, os, random

from project.boid_ai import BoidAI
from project.window import Window
from project.event import EventManager
from project.vector2 import Vector2
from project.graphics_component import GraphicsComponent
from project.window import WindowUpdater
from project.boid_ai import BoidAIUpdater

from project.ai_evade import Evade
from project.ai_cohesion import Cohesion
from project.ai_alignment import Alignment

from project.gui_object import ( GUI, Button, Slider )


class App( object ):

        window = None
        
                
        def __init__( self ):
        
                self.Init()
                
                self.GenerateGUI()
                
                # Generate flock
                self.GenerateFlock()
                
                
        def Init( self ):
        
                self.bContinue = True
                
                pygame.init()
                
                self.window_size = [ 800, 600 ]
                self.window_size = [ 1000, 750 ]
                self.window = Window( self.window_size )
                
                fps = 1.0 / 30.0
                
                EventManager.Init()
                
                EventManager.RegisterListener( self.Quit )
                EventManager.RegisterListener( self.Restart )
                EventManager.RegisterListener( Evade.GetEvent )
                EventManager.RegisterListener( Cohesion.GetEvent )
                EventManager.RegisterListener( Alignment.GetEvent )
                
                self.file_path = os.path.dirname( __file__ )
                
                # Threads
                self.windowThread = WindowUpdater( self.window, fps )
                #self.boidGraphicsThread = BoidGraphicsUpdater( fps )
                
        
        def GenerateGUI( self ):
        
                # Exit button
                img_path = "/assets/button_exit.png"
                
                size = [ 159, 39 ]
                loc = [ 0, self.window_size[ 1 ] - ( size[ 1 ] * 1.0 ) ]
                
                event_type = EventManager.EventQuit
                
                self.CreateButton( img_path, size, loc, event_type )
                
                
                # Restart button
                img_path = "/assets/button_restart.png"
                
                loc = [ 159, self.window_size[ 1 ] - ( size[ 1 ] * 1.0 ) ]
                
                event_type = EventManager.EventRestart
                
                self.CreateButton( img_path, size, loc, event_type )
                
                
                # Alignment slider
                img_path_list = [ "/assets/slider_bg.png", "/assets/slider_slider.png" ]
                
                size = [ 206, 40 ]
                
                loc = [ self.window_size[ 0 ] - size[ 0 ], self.window_size[ 1 ] - ( size[ 1 ] * 3.0 ) ]
                
                event_type = EventManager.EventChangeAlignmentFactor
                
                self.CreateSlider( img_path_list, size, loc, event_type )
                
                
                # Evade slider
                loc = [ self.window_size[ 0 ] - size[ 0 ], self.window_size[ 1 ] - ( size[ 1 ] * 2.0 ) ]
                
                event_type = EventManager.EventChangeEvadeFactor
                
                self.CreateSlider( img_path_list, size, loc, event_type )
                
                
                # Cohesion slider
                loc = [ self.window_size[ 0 ] - size[ 0 ], self.window_size[ 1 ] - ( size[ 1 ] * 1.0 ) ]
                
                event_type = EventManager.EventChangeCohesionFactor
                
                self.CreateSlider( img_path_list, size, loc, event_type )
                
        
        def CreateButton( self, img_path, size, loc, event_type ):
        
                img_path = self.file_path + img_path
                
                location = pygame.Rect( loc, size )
                
                collision_x = loc[ 0 ]
                collision_y = loc[ 1 ]
                collision_w = size[ 0 ] - 11
                collision_h = size[ 1 ]
                collision_rect = pygame.Rect( collision_x, collision_y, collision_w, collision_h )
                
                button = Button( img_path, location, collision_rect )
                
                button.SetEventType( event_type )
        
        
        def CreateSlider( self, img_path_list, size, loc, event_type ):
        
                img_path_bg = self.file_path + img_path_list[ 0 ]
                img_path_slider = self.file_path + img_path_list[ 1 ]
                
                location = pygame.Rect( loc, size )
                
                collision_x = loc[ 0 ]
                collision_y = loc[ 1 ]
                collision_w = size[ 0 ] - 11
                collision_h = size[ 1 ]
                collision_rect = pygame.Rect( collision_x, collision_y, collision_w, collision_h )
                
                slider = Slider( [ img_path_bg, img_path_slider ], location, collision_rect )
                
                slider.SetEventType( event_type )
                
                
        def GenerateFlock( self ):
        
                location_min_x = self.window_size[ 0 ] * 0.2
                location_max_x = self.window_size[ 0 ] * 0.8
                
                location_min_y = self.window_size[ 1 ] * 0.2
                location_max_y = self.window_size[ 1 ] * 0.8
                        
                speed_min = -5.0
                speed_max = 5.0
                
                # max 50
                for i in range( 30 ):
                        loc_x = random.uniform( location_min_x, location_max_x )
                        loc_y = random.uniform( location_min_y, location_max_y )
                        
                        speed_x = random.uniform( speed_min, speed_max )
                        speed_y = random.uniform( speed_min, speed_max )
                        
                        boid_location = Vector2( loc_x, loc_y )
                        boid_speed = Vector2( speed_x, speed_y )
                        
                        image_path = self.file_path + "/assets/boid0" + str( random.randint( 1, 4 ) ) + ".png"
                        
                        BoidAI( boid_location, boid_speed, image_path )
                

        def Loop( self ):
        
                self.windowThread.start()
                #self.boidGraphicsThread.start()
                
                self.windowThread.fps = 0.0
                self.windowThread.fps = 0.0
                #self.boidGraphicsThread.fps = 0.0
                
                fps = 1.0 / 60.0
                BoidAI.InitFPS( fps )
                
                self.windowThread.fps = fps
                
                '''
                from event import EventUpdater
                eventThread = EventUpdater()
                
                eventThread.start()
                '''
                
                while ( self.bContinue ):
                        EventManager.Update()
                        GUI.Update()
                        
                        BoidAI.UpdatePhysics()
                        
                        
        def Restart( self, event ):
        
                bRestart = event[ 0 ] is EventManager.EventRestart
                
                if ( bRestart ):
                        BoidAI.Stop()
                        GUI.Reset()
                        self.GenerateGUI()
                        self.GenerateFlock()
                        

        def Quit( self, event ):
        
                bQuit = event[ 0 ] is EventManager.EventQuit
                
                if ( bQuit ):
                        #self.boidGraphicsThread.Stop()
                        BoidAI.Stop()
                        GUI.Reset()
                        
                        self.windowThread.Stop()
                        
                        self.bContinue = False
                        
                        sys.exit()

        
        
        
        
        
        
        
        
        
        