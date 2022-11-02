# FILENAME:selectFunc.py

import tkinter
from tkinter import *
from selfJudge import selfJudge as sj
from otherJudge import otherJudge as oj


# 跳转“他评量表”界面
def changePage2Other():
    window.destroy()
    oj()

# 跳转“自评量表”界面
def changePage2Self():
    window.destroy()
    sj()



def selectFunc():


    global window
    window = tkinter.Tk()

    # 获取屏幕分辨率
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    screenWidth = int(screenWidth)
    screenHeight = int(screenHeight)

    # 设置窗口全屏显示
    window.geometry("%sx%s" % (screenWidth, screenHeight))
    # 更换界面图标
    window.iconphoto(True, tkinter.PhotoImage(file=r'.\statics\icon.ico'))
    # 设置窗口宽高固定·
    window.resizable(0, 0)

    # tkinter窗口
    window.title("心理测评")
    window.configure(bg='white')
    # 图标
    # window.iconbitmap("./icon/multi-storey.ico")



    # 标志
    global lbStatus
    lbStatus = tkinter.Label(window, text='科睿纳AI精神心理辅助诊断系统', font=('black',40), fg='red', bg='white')
    lbStatus.place(relx=0.33, rely=0.20)

    # 他评表按钮
    tkinter.Button(window, text='他评量表', font=('Arial', 15),width=10, height=2, bg='white',
                   fg='black', relief=RIDGE ,borderwidth=1, command=changePage2Other).place(relx=0.32,
                                                                         rely=0.78, relwidth=0.1, relheight=0.1)

    # 自评表按钮
    tkinter.Button(window, text='自评量表', font=('Arial', 15), width=10, height=2, bg='white',
                   fg='black',relief=RIDGE, borderwidth=1, command=changePage2Self).place(relx=0.57,
                                                                            rely=0.78, relwidth=0.1, relheight=0.1)



    window.mainloop()

