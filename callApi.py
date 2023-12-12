import requests
import json
import getDeviceInfo
import getWebHistory
import getKeyboardLog
from tkinter import messagebox
import webbrowser

HOST = "https://hanamthai.alwaysdata.net"
# HOST = "http://127.0.0.1:5000"

def apiAddDevice(accessToken):
        deviceID = getDeviceInfo.getDeviceID()
        url = HOST + "/v1/childs/add-device"
        # Set the headers to specify that you are sending JSON data
        headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
        data = {"deviceName":deviceID}
        # Convert the data dictionary to JSON
        json_data = json.dumps(data)
        response = requests.post(url, data=json_data, headers=headers)
        # Phân tích dữ liệu JSON
        data = json.loads(response.text)
        if response.status_code != 200:
            messagebox.showerror('Invalid', data.get("message"))
            return ''
        elif response.status_code == 200:
            # messagebox.showinfo('Success', data.get("message"))
            return ''
        return ''

def apiSendWebHistory(accessToken):
    if accessToken == "":
        return ''
    url = HOST + "/v1/childs/web-history"
    # Set the headers to specify that you are sending JSON data
    headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
    deviceID = getDeviceInfo.getDeviceID()
    latestTimestamp = getLatestWebKitTimestamp(deviceID, accessToken)
    histories = getWebHistory.getWebHistory(latestTimestamp)
    historiesInput = [{'url':i[0],'totalVisit':i[1],'createdAt':i[2]}for i in histories]
    data = {'deviceName':deviceID,'histories':historiesInput}
    # Convert the data dictionary to JSON
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data, headers=headers)
    # Phân tích dữ liệu JSON
    data = json.loads(response.text)
    if response.status_code != 200:
        messagebox.showerror('Invalid', data.get("message"))
        return ''
    elif response.status_code == 200:
        print("Send Web history success!")
        # messagebox.showinfo('Success', data.get("message"))
        return ''
    return ''

def apiSendKeyboardLog(accessToken):
    if accessToken == "":
        return ''
    url = HOST + "/v1/childs/keyboard-log"
    # Set the headers to specify that you are sending JSON data
    headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
    deviceID = getDeviceInfo.getDeviceID()
    latestTimestamp = getLatestWebKitTimestampKeyBoard(deviceID, accessToken)
    keyboardLogs = getKeyboardLog.getKeyboardLog(latestTimestamp)
    keyboardLogsInput = [{'keyStroke':i[0],'totalVisit':i[1],'createdAt':i[2]}for i in keyboardLogs]
    data = {'deviceName':deviceID,'keyboardLogs':keyboardLogsInput}
    # Convert the data dictionary to JSON
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data, headers=headers)
    # Phân tích dữ liệu JSON
    data = json.loads(response.text)
    if response.status_code != 200:
        messagebox.showerror('Invalid', data.get("message"))
        return ''
    elif response.status_code == 200:
        print("Send Keyboard log success!")
        # messagebox.showinfo('Success', data.get("message"))
        return ''
    return ''

def apiUserInfo(accessToken):
    url = HOST + "/v1/user-profile"
    # Set the headers to specify that you are sending JSON data
    headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
    # Convert the data dictionary to JSON
    response = requests.get(url, headers=headers)
    # Phân tích dữ liệu JSON
    data = json.loads(response.text)
    if response.status_code != 200:
        messagebox.showerror('Invalid', data.get("message"))
        return ''
    elif response.status_code == 200:
        resp = data.get('data')
        return resp
    return ''

def open_chrome():
    # url = "https://www.google.com"  # Đổi URL thành trang web bạn muốn mở
    # webbrowser.get("edge").open(url)  # Sử dụng trình duyệt Chrome
    webbrowser.open_new('http://localhost:3000/login')
    return ''

def getLatestWebKitTimestamp(deviceID, accessToken):
    url = HOST + '/v1/childs/web-history/latest-time/%s' % (deviceID)
    # Set the headers to specify that you are sending JSON data
    headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
    # Convert the data dictionary to JSON
    response = requests.get(url, headers=headers)
    # Phân tích dữ liệu JSON
    data = json.loads(response.text)
    if response.status_code != 200:
        messagebox.showerror('Invalid', data.get("message"))
        return ''
    elif response.status_code == 200:
        resp = data.get('data')
        return resp
    return ''

def getLatestWebKitTimestampKeyBoard(deviceID, accessToken):
    url = HOST + '/v1/childs/keyboard-log/latest-time/%s' % (deviceID)
    # Set the headers to specify that you are sending JSON data
    headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
    # Convert the data dictionary to JSON
    response = requests.get(url, headers=headers)
    # Phân tích dữ liệu JSON
    data = json.loads(response.text)
    if response.status_code != 200:
        messagebox.showerror('Invalid', data.get("message"))
        return ''
    elif response.status_code == 200:
        resp = data.get('data')
        return resp
    return ''

def isRegisterDevice(accessToken):
    deviceID = getDeviceInfo.getDeviceID()
    url = HOST + '/v1/childs/check-register-device/%s' % (deviceID)
    headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
    # Convert the data dictionary to JSON
    response = requests.get(url, headers=headers)
    # Phân tích dữ liệu JSON
    data = json.loads(response.text)
    if response.status_code != 200:
        messagebox.showerror('Invalid', data.get("message"))
        return ''
    elif response.status_code == 200:
        resp = data.get('data')
        return resp
    return ''