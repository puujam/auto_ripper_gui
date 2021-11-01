# Base modules
import time
import os
import multiprocessing

# Non-standard Installed modules
from daemoniker import Daemonizer

# Local modules
import processing
import communication

pid_file_path = "pid_file"
        
def main():
    global processor

    processor = processing.Processor()
    server = communication.ARServer()
    
    processor.start()
    server.start()

if __name__ == "__main__":
    # Check if our pid file already exists and if so, delete it
    if os.path.exists( pid_file_path ):
        os.remove( pid_file_path )

    with Daemonizer() as (is_setup, daemonizer):
        if is_setup:
            # Code before daemonization
            pass

        is_parent = daemonizer( pid_file_path ) # pid_file isn't used

        if is_parent:
            # Code run only in the parent after daemonization
            pass
        
        main()