# FILENAME:otherJudge.py


import tkinter
from tkinter import *
import selectFunc as selectFunc
from otherJudge_SAS import otherJudgeSAS as osa
from otherJudge_SDS import otherJudgeSDS as osd


# 返回selectFunc
def back2selectFunc():
    window.destroy()
    selectFunc.selectFunc()



# 跳转“他评焦虑”界面
def changePage2SAS():
    window.destroy()
    osa()


# 跳转“他评抑郁”界面
def changePage2SDS():
    window.destroy()
    osd()


def otherJudge():
    # 窗体
    global window
    window = tkinter.Tk()

    # 获取屏幕分辨率
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    screenWidth = int(screenWidth)
    screenHeight = int(screenHeight)

    # 设置窗口全屏显示
    window.geometry("%sx%s" % (screenWidth, screenHeight))
    # window.geometry("1440x900")
    # 设置窗口宽高固定
    window.resizable(0, 0)

    # tkinter窗口
    window.title("心理测评")
    window.configure(bg='white')
    # 图标
    # window.iconbitmap("./icon/multi-storey.ico")



    # 标志
    global lbStatus
    lbStatus = tkinter.Label(window, text='他评量表选择', font=('black',40), fg='red', bg='white')   # 显示绿色状态字
    lbStatus.place(relx=0.38, rely=0.20)

    # 焦虑
    tkinter.Button(window, text='焦虑他评', font=('Arial', 15), width=10, height=2,
                   command=changePage2SAS, borderwidth=5).place(relx=0.32,rely=0.78, relwidth=0.1, relheight=0.1)

    # 抑郁
    tkinter.Button(window, text='抑郁他评', font=('Arial', 15), width=10, height=2,
                   command=changePage2SDS, borderwidth=5).place(relx=0.57,rely=0.78, relwidth=0.1, relheight=0.1)


    # 返回selectFunc按钮
    tkinter.Button(window, text='<返回', font=('Arial', 15), width=10, height=2, command=back2selectFunc, bg='white',
                   fg='black', relief=RIDGE,
                   borderwidth=1).place(relx=0.05, rely=0.05, relwidth=0.07, relheight=0.07)


    window.mainloop()

