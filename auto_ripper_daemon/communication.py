import zmq
import threading

class ARServer( threading.Thread ):
    def __init__( self ):
        self.context = zmq.Context()
        self.socket = self.context.socket( zmq.ROUTER )
        self.socket.connect( "tcp://localhost:5570" )
        
        threading.Thread.__init__( self )
    
    def run( self ):
        while True:
            # Wait for a request
            request = self.socket.recv()

            # Branch based on the request then reply
            if request == "drives":
                self.reply_drives()
    
    def reply_drives():
        global processor

        for drive in processor.drives:
            self.socket.send_string( drive.drive )