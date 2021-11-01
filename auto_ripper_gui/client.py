import zmq
import re

class ARClient():
    def __init__( self ):
        self.context = zmq.Context()
        self.socket = self.context.socket( zmq.REQ )
        self.socket.bind( "tcp://*:5555" )

        threading.Thread.__init__( self )
    
    def request_drives( self ):
        self.socket.send_string( "drives" )
        complete_message = socket.recv() # TODO: Timeout? Exception handling?
        
        drives = list()
        
        for single_drive_message in complete_message.split( "," ):
            drives.append( ARDrive( single_drive_message ) )
            
        return drives
        
class ARDrive():
    message_re = re.compile(  )

    def __init__( self, message ):
        match = ARDrive.message_re.match( message )
        
        self.drive = match.group(1)
        self.status = match.group(2)