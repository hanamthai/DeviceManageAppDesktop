from tkinter import *
from tkinter import messagebox
import requests
import json
import callApi

root=Tk()
root.title('Manage Device')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)
img = PhotoImage(file='./Image/login.png')
HOST = "https://hanamthai.alwaysdata.net"
# HOST = "http://127.0.0.1:5000"

win2=Frame(root, width=925,height=500,bg="white") # define to support when click button logout

accessToken = ""

def loginWindow(win2):
    def apiLogin(Win1):
        username = user.get()
        password = code.get()
        if username == 'Username':
            messagebox.showwarning('Invalid', "Please input username!!")
            return ''
        if password == 'Password':
            messagebox.showwarning('Invalid', "Please input password!!")
            return ''
        # validate
        if username == '' or password == '':
            messagebox.showwarning('Invalid',"Please input username and password!!")
            return ''

        url = HOST + "/v1/logins"
        # Set the headers to specify that you are sending JSON data
        headers = {'Content-Type': 'application/json'}
        data = {"email": username,"password": password}
        # Convert the data dictionary to JSON
        json_data = json.dumps(data)
        response = requests.post(url, data=json_data, headers=headers)
        # Phân tích dữ liệu JSON
        data = json.loads(response.text)
        if response.status_code != 200:
            messagebox.showerror('Invalid', data.get("message"))
            return ''
        access_token = data.get("access_token")
        global accessToken
        accessToken = access_token
        fullName = callApi.apiUserInfo(accessToken)['fullName']
        homeWindow(Win1,fullName)

    # def check():
    #     global accessToken
    #     messagebox.showinfo('token', accessToken)

    global img, accessToken
    label = Label(root,image=img,bg='white').place(x=50,y=50)
    # when click logout then destroy homepage and clear token
    win2.destroy()
    accessToken = ""

    win1=Frame(root, width=350,height=350,bg="white")
    win1.place(x=480,y=70) 

    heading=Label(win1,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    ###------------------------
    def on_enter(e):
        if user.get() == 'Username':
            user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(win1,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11)) 
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(win1, width=295,height=2,bg="black").place(x=25,y=107)
    ###------------------------
    def on_enter(e):
        if code.get() == 'Password':
            code.delete(0, 'end')

    def on_leave(e):
        name=code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(win1,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11),show='*') 
    code.place(x=30,y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(win1, width=295,height=2,bg="black").place(x=25,y=177)
    ###------------------------
    Button(win1, width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',cursor='hand2',border=0,command=lambda:apiLogin(win1)).place(x=35,y=204)
    label=Label(win1, text="Don't have an account",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place (x=75,y=270)

    sign_up=Button(win1,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg="#57a1f8",command=callApi.open_chrome)
    sign_up.place(x=215,y=270)

    # checkToken=Button(win1,width=6,text='Check',border=0,bg='white',fg="#57a1f8", command=check)
    # checkToken.place(x=215,y=300)

def homeWindow(win1,fullName):
    win1.destroy()  # Đóng cửa sổ đăng nhập
    win2=Frame(root, width=925,height=500,bg="white") # Tạo cửa sổ home
    win2.pack()
    heading=Label(win2,text='WELCOME TO APP MANAGE DEVICE',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=170,y=5)
    ###------------------------
    userName = Label(win2,text='Hi '+fullName+'!',fg='black',bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
    userName.place(x=675,y=50)
    Frame(win2, width=300,height=2,bg="#57a1f8").place(x=667,y=80)
    ###-----------------------
    addDevice=Button(win2,width=15,height=2,text='Add Device',border=0,bg='#00ec00',fg='white',cursor='hand2', font=('Microsoft YaHei UI Light',15,'bold'),command=lambda:callApi.apiAddDevice(accessToken))
    addDevice.place(x=375,y=100)
    ###------------------------
    sendHistory=Button(win2,width=17,height=2,text='Send Web History',border=0,bg='#00ec00',fg='white',cursor='hand2', font=('Microsoft YaHei UI Light',15,'bold'),command=lambda:callApi.apiSendWebHistory(accessToken))
    sendHistory.place(x=255,y=250)

    sendBlockWebsite=Button(win2,width=17,height=2,text='Send Keyboard Log',border=0,bg='#00ec00',fg='white',cursor='hand2', font=('Microsoft YaHei UI Light',15,'bold'),command=lambda:callApi.apiSendKeyboardLog(accessToken))
    sendBlockWebsite.place(x=550,y=250)
    ###------------------------
    logout=Button(win2,width=20,text='Logout',border=0,bg='#57a1f8',fg='white',cursor='hand2', command=lambda:loginWindow(win2))
    logout.place(x=750,y=460)

loginWindow(win2)

root.mainloop()
