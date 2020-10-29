import sys
import subprocess
import bluetooth  


class fileTransfer:

    def getIP(self):
        subprocess.run(["hostname","-I"])

    #getIP()
    
    target = "DESKTOP-1CQVEDS"
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    #file_Sent = "/media/usb/files/hw4_soln.pdf"
    for device in nearby_devices:
        print(device)

    #/gitrepo/Design/APIcode