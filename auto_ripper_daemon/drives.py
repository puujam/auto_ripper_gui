import wmi

_wmi_handle = None

def get_wmi_handle():
    global _wmi_handle
    if not _wmi_handle:
        _wmi_handle = wmi.WMI()
    
    return _wmi_handle

def list_all_removable_drives():
    results = list()
    wmi_handle = get_wmi_handle()

    for drive in wmi_handle.Win32_LogicalDisk():
        if drive.DriveType == 2: # 2 is Removable Disk apparently
            results.append( drive )
    
    return results