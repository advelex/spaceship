import os
import pathlib
import sys


class StringToDirectory( object ):

    LINUX = 10
    OTHER = 20
    
    is_set = False
    
    current_os = 0
    
        
    def Get( string_to_dir ):
    
        if ( not StringToDirectory.is_set ):
        
            if sys.platform == "linux" or sys.platform == "linux2":
                StringToDirectory.current_os = StringToDirectory.LINUX
            else:
                StringToDirectory.current_os = StringToDirectory.OTHER
            
            StringToDirectory.is_set = True
            
        if StringToDirectory.current_os == StringToDirectory.LINUX:
            print( str( pathlib.Path( string_to_dir ).resolve() ) )
            return str( pathlib.Path( string_to_dir ).resolve() )
            
        elif StringToDirectory.current_os == StringToDirectory.OTHER:
            print( os.path.dirname( __file__ ) + "/" + string_to_dir )
            return os.path.dirname( __file__ ) + "/" + string_to_dir
        else:
            raise Exception( "os:{} is unrecognized." .format( StringToDirectory.current_os ) )



















