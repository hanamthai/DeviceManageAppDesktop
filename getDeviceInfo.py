import socket

def getDeviceID():
    hostname = socket.gethostname()
    return hostname
