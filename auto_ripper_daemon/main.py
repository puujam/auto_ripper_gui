# Base modules
import time
import os

# Non-standard Installed modules
from daemoniker import Daemonizer

# Local modules
import drives

pid_file_path = "pid_file"
        
def main():
    while True:
        cd_drives = drives.list_all_cd_drives()

        for cd_drive in cd_drives:
            if cd_drive.MediaLoaded:
                print( "Media detected in drive {}".format( cd_drive.Drive ) )
            else:
                print( "No media in drive {}".format( cd_drive.Drive ) )
        
        time.sleep( 5 )

if __name__ == "__main__":
    # Check if our pid file already exists and if so, delete it
    if os.path.exists( pid_file_path ):
        os.remove( pid_file_path )

    with Daemonizer() as (is_setup, daemonizer):
        if is_setup:
            # Code before daemonization
            pass

        is_parent = daemonizer( pid_file_path ) # pid_file isn't used, an alternative communications channel will be opened between the daemon and the GUI

        if is_parent:
            # Code run only in the parent after daemonization
            pass
        

        main()