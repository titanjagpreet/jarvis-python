import os
import subprocess

SEARCH_PATHS = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    r"C:\Users\Dell\AppData\Local",
]

def open_app(name):
    name = name.lower().replace(".exe", "")

    for root in SEARCH_PATHS:
        for dirname, _, files in os.walk(root):
            for file in files:
                if name in file.lower():
                    try:
                        subprocess.Popen(os.path.join(dirname, file))
                        return True
                    except:
                        continue
    return False
