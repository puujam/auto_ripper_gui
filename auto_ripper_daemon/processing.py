import wmi_drives
import time
import threading

class Processor( threading.Thread ):
    def __init__( self ):
        self.drives = list()
        
        threading.Thread.__init__( self )
    
    def run( self ):
        while True:
            self.drives = drives.list_all_cd_drives()
            
            time.sleep( 5 )