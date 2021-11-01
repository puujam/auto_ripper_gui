# Base imports
import time

# Local modules
import client

def main():
    client_instance = client.ARClient()

    while True:
        drives = client_instance.request_drives()

        if not drives:
            print( "No drives connected." )
        else:
            for drive in drives:
                print( "{}: {}".format( drive.drive, drive.status ) )

        time.sleep( 5 )

if __name__ == "__main__":
    main()