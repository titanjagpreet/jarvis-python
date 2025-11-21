import os

def system_command(cmd):
    if "shutdown" in cmd:
        os.system("shutdown /s /t 1")
    elif "restart" in cmd:
        os.system("shutdown /r /t 1")
    else:
        return False

    return True
