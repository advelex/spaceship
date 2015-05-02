 
from math import ( hypot, degrees, atan2 )


'''
Vector2 class
'''
class Vector2( object ):

        def __init__( self, x = None, y = None ):
                
                self.x = x
                self.y = y
                
                
        def GetAngle( self ):
        
                return degrees( atan2( self.x, self.y ) )


        def Magnitude( self ):
        
                return hypot( self.x, self.y )
                
                
        def Normalize( self ):
                if ( self.x == 0 or self.y == 0 ):
                        return Vector2( 0, 0 )
                
                return Vector2( self.x, self.y ) * ( 1.0 / self.Magnitude() )
                
                
        def Clamp( self, min, max ):
        
                x = 0
                y = 0
                
                if ( min is not None ):
                        x = float( Clamp( self.x, min, None ) )
                        y = float( Clamp( self.y, min, None ) )
                if ( max is not None ):
                        x = float( Clamp( self.x, None, max ) )
                        y = float( Clamp( self.y, None, max ) )
                
                return Vector2( x, y )
                
                
        def ClampMagnitude( self, max_magnitude ):
        
                mag = self.Magnitude()
                
                if ( mag > max_magnitude ):
                        return self.Normalize() * max_magnitude
                        
                return self
                
                        
        def __str__( self ):
        
                return "<" + str( self.x ) + ", " + str( self.y ) + ">"


        # Returns a new Vector2
        def __sub__( self, other ):
        
                if ( other is None ):
                        raise Exception("\nparameter is None\n")
                
                try:
                        x = float( self.x - other.x )
                        y = float( self.y - other.y )
                        
                        return Vector2( x, y )
                        
                except TypeError:
                        raise TypeError
                        
        
        # Returns a new Vector2
        def __add__( self, other ):
        
                if ( other is None ):
                        raise Exception("\nparameter is None\n")
                
                try:
                        x = float( self.x + other.x )
                        y = float( self.y + other.y )
                        
                        return Vector2( x, y )
                        
                except TypeError:
                        raise TypeError
                        
                
        # Returns a new Vector2    
        def __mul__( self, other ):
        
                if ( other is None ):
                        raise Exception("\nparameter is None\n")
                
                try:
                        x = self.x * other
                        y = self.y * other
                        
                        return Vector2( x, y )
                        
                except TypeError:
                        raise TypeError
                        
                        
                        
              
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        