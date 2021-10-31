import wmi

_wmi_handle = None

def get_wmi_handle():
    global _wmi_handle
    if not _wmi_handle:
        _wmi_handle = wmi.WMI()
    
    return _wmi_handle

def list_all_cd_drives():
    wmi_handle = get_wmi_handle()

    return wmi_handle.Win32_CDRomDrive()