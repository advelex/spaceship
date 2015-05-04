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
            
        string_to_return = ""
        
        if StringToDirectory.current_os == StringToDirectory.LINUX:
            string_to_return = str( pathlib.Path( string_to_dir ).resolve() )
            
        elif StringToDirectory.current_os == StringToDirectory.OTHER:
            string_to_return = os.path.dirname( __file__ ) + "/" + string_to_dir
            
        else:
            raise Exception( "os:{} is unrecognized." .format( StringToDirectory.current_os ) )
            
        print( string_to_return )
        return string_to_return



















