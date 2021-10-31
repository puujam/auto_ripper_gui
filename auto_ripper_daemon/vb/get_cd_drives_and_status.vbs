' Code contstructed from examples from https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-tasks--disks-and-file-systems

strComputer = "."
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set wmiServices  = GetObject ( _
    "winmgmts:{impersonationLevel=Impersonate}!//" & strComputer )

' Get CD drives
Set colItems = objWMIService.ExecQuery( "Select * from Win32_CDROMDrive")
For Each objItem in colItems

    Wscript.Echo "Name: " & objItem.Name
    Wscript.Echo "Device ID: " & objItem.DeviceID
    Wscript.Echo "Drive: " & objItem.Drive
    Wscript.Echo "Media Loaded: " & objItem.MediaLoaded
Next