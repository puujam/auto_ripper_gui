# Base modules
import time

# Non-standard Installed modules
from daemoniker import Daemonizer

# Local modules
import drives
        
def main():
    while True:
        removable_drives = drives.list_all_removable_drives()

        for removable_drive in removable_drives:
            print( removable_drive.Caption )
        
        time.sleep( 5 )

if __name__ == "__main__":
    with Daemonizer() as (is_setup, daemonizer):
        if is_setup:
            # Code before daemonization
            pass

        is_parent = daemonizer( "pid_file" ) # pid_file isn't used, an alternative communications channel will be opened between the daemon and the GUI

        if is_parent:
            # Code run only in the parent after daemonization
            pass

    main()