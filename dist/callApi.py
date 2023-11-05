import requests
import json
import getDeviceInfo
import getWebHistory
import getKeyboardLog
from tkinter import messagebox
import webbrowser

def apiAddDevice(accessToken):
        deviceID = getDeviceInfo.getDeviceID()
        url = "http://127.0.0.1:5000/v1/childs/add-device"
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
            messagebox.showinfo('Success', data.get("message"))
            return ''
        return ''

def apiSendWebHistory(accessToken):
    url = "http://127.0.0.1:5000/v1/childs/web-history"
    # Set the headers to specify that you are sending JSON data
    headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
    deviceID = getDeviceInfo.getDeviceID()
    histories = getWebHistory.getWebHistory()
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
        messagebox.showinfo('Success', data.get("message"))
        return ''
    return ''

def apiSendKeyboardLog(accessToken):
    url = "http://127.0.0.1:5000/v1/childs/keyboard-log"
    # Set the headers to specify that you are sending JSON data
    headers = {'Content-Type': 'application/json','Authorization':'Bearer '+accessToken}
    deviceID = getDeviceInfo.getDeviceID()
    keyboardLogs = getKeyboardLog.getKeyboardLog()
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
        messagebox.showinfo('Success', data.get("message"))
        return ''
    return ''

def apiUserInfo(accessToken):
    url = "http://127.0.0.1:5000/v1/user-profile"
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
    webbrowser.open_new('https://www.google.com')
    return ''