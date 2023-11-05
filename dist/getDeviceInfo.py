import socket

def getDeviceID():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # print("Tên máy tính:", hostname)
    # print("Địa chỉ IP:", ip_address)
    # join hostname and ip_address to create deviceID
    deviceID = hostname + ip_address
    return deviceID
