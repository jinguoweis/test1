#!/usr/bin/env python
# coding: utf-8
# FILENAME:selfJudge_SAS.py

import tkinter
from tkinter import *
from tkinter import ttk
import pandas as pd
import pymysql
from PIL import Image, ImageTk
import selfJudge as selfJudge
from aiJudge import aiJudge as aj
import time
from scaleDegree import selfSASFunc


# 返回selfJudge
def back2selfJudge():
    selfSAS.destroy()
    selfJudge.selfJudge()

# 插入数据库
def insert(patientid, age, testScore, answer):
    global testType
    testType = 'selfSDS'
    # 时间戳
    now = int(round(time.time() * 1000))
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now/1000))
    # 入库
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='krndb', charset='utf8')
    cursor = connection.cursor()
    cursor.execute("insert into score (patientId, age, testType, testScore, answer, insertTime) values (%s, %s, %s, %s, %s, %s)", (patientid, age, testType, testScore, str(answer), currentTime))
    connection.commit()
    connection.close()
    cursor.close()



def getSelfSASData():


    id = entry_Id.get()
    age = entry_Age.get()

    global answerList
    answerList = []

    if v1.get()==0:
        tkinter.messagebox.showinfo("提示","第1题选项不能为空！")
    elif v2.get()==0:
        tkinter.messagebox.showinfo("提示","第2题选项不能为空！")
    elif v3.get()==0:
        tkinter.messagebox.showinfo("提示","第3题选项不能为空！")
    elif v4.get()==0:
        tkinter.messagebox.showinfo("提示","第4题选项不能为空！")
    elif v5.get()==0:
        tkinter.messagebox.showinfo("提示","第5题选项不能为空！")
    elif v6.get()==0:
        tkinter.messagebox.showinfo("提示","第6题选项不能为空！")
    elif v7.get()==0:
        tkinter.messagebox.showinfo("提示","第7题选项不能为空！")
    elif v8.get()==0:
        tkinter.messagebox.showinfo("提示","第8题选项不能为空！")
    elif v9.get()==0:
        tkinter.messagebox.showinfo("提示","第9题选项不能为空！")
    elif v10.get()==0:
        tkinter.messagebox.showinfo("提示","第10题选项不能为空！")
    elif v11.get()==0:
        tkinter.messagebox.showinfo("提示","第11题选项不能为空！")
    elif v12.get()==0:
        tkinter.messagebox.showinfo("提示","第12题选项不能为空！")
    elif v13.get()==0:
        tkinter.messagebox.showinfo("提示","第13题选项不能为空！")
    elif v14.get()==0:
        tkinter.messagebox.showinfo("提示","第14题选项不能为空！")
    elif v15.get()==0:
        tkinter.messagebox.showinfo("提示","第15题选项不能为空！")
    elif v16.get()==0:
        tkinter.messagebox.showinfo("提示","第16题选项不能为空！")
    elif v17.get()==0:
        tkinter.messagebox.showinfo("提示","第17题选项不能为空！")
    elif v18.get()==0:
        tkinter.messagebox.showinfo("提示","第18题选项不能为空！")
    elif v19.get()==0:
        tkinter.messagebox.showinfo("提示","第19题选项不能为空！")
    elif v20.get()==0:
        tkinter.messagebox.showinfo("提示","第20题选项不能为空！")

    elif id == '' or age == '':
        tkinter.messagebox.showinfo('提示','请输入编号或者年龄')
    else:
        answerList.append(posOptionList[v1.get()-1][0])
        answerList.append(negOptionList[v2.get()-1][0])
        answerList.append(posOptionList[v3.get()-1][0])
        answerList.append(posOptionList[v4.get()-1][0])
        answerList.append(negOptionList[v5.get()-1][0])
        answerList.append(negOptionList[v6.get()-1][0])
        answerList.append(posOptionList[v7.get()-1][0])
        answerList.append(posOptionList[v8.get()-1][0])
        answerList.append(posOptionList[v9.get()-1][0])
        answerList.append(posOptionList[v10.get()-1][0])
        answerList.append(negOptionList[v11.get()-1][0])
        answerList.append(negOptionList[v12.get()-1][0])
        answerList.append(posOptionList[v13.get()-1][0])
        answerList.append(negOptionList[v14.get()-1][0])
        answerList.append(posOptionList[v15.get()-1][0])
        answerList.append(negOptionList[v16.get()-1][0])
        answerList.append(negOptionList[v17.get()-1][0])
        answerList.append(negOptionList[v18.get()-1][0])
        answerList.append(posOptionList[v19.get()-1][0])
        answerList.append(negOptionList[v20.get()-1][0])

        # 计算得分
        global _sdsScore
        _sdsScore = int((v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get() + v7.get() + v8.get() + v9.get() + v10.get() + v11.get() + v12.get() + v13.get() + v14.get() +                     v15.get() + v16.get() + v17.get() + v18.get() + v19.get() + v20.get())*1.25)

        insert(patientid=id, age=age, testScore=_sdsScore, answer=answerList)
        tkinter.messagebox.showinfo('提示', '提交成功，请进行录音检测')
        selfSASDegree = selfSASFunc(_sdsScore)
        selfSAS.destroy()
        aj(ts=_sdsScore, id=id, age=age, type=testType, deg=selfSASDegree)

# 鼠标滚动
def processWheel(event):
    a= int(-(event.delta)/60)
    canvas.yview_scroll(a,'units')


def resize(w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
    w, h = pil_image.size  # 获取图像的原始大小
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


def click():
    fontsize = 15  # 题卡内容字号
    width = 30  # 题卡按钮宽度
    gap = 0.035 # 题卡间距
    i = 0.8
    j = 0.02
    Label(text="题卡:", font=('black', 20), bg='white').place(width=70,height=30, relx=i,rely=j)
    j += 0.04
    if v1.get()==0:
        Label(text="1.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="1.", font=('black', fontsize)).place(width=width,height=30,relx=i,rely=j)

    i += gap
    if v2.get()==0:
        Label(text="2.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="2.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v3.get()==0:
        Label(text="3.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="3.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v4.get()==0:
        Label(text="4.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="4.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)

    j += 0.05
    i = 0.8
    if v5.get()==0:
        Label(text="5.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="5.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v6.get()==0:
        Label(text="6.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="6.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i+= gap
    if v7.get()==0:
        Label(text="7.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="7.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v8.get()==0:
        Label(text="8.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="8.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)


    i = 0.8
    j += 0.05
    if v9.get()==0:
        Label(text="9.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="9.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i +=gap
    if v10.get()==0:
        Label(text="10.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="10.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v11.get()==0:
        Label(text="11.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="11.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v12.get()==0:
        Label(text="12.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="12.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)


    i = 0.8
    j += 0.05
    if v13.get()==0:
        Label(text="13.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="13.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v14.get()==0:
        Label(text="14.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="14.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v15.get()==0:
        Label(text="15.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="15.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v16.get()==0:
        Label(text="16.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="16.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)

    i = 0.8
    j += 0.05
    if v17.get()==0:
        Label(text="17.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="17.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i+=gap
    if v18.get()==0:
        Label(text="18.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="18.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v19.get()==0:
        Label(text="19.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="19.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
    i += gap
    if v20.get()==0:
        Label(text="20.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
    else:
        Label(text="20.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)

def selfJudgeSAS():

    global selfSAS
    selfSAS = tkinter.Tk()  # tkinter窗口

    # 获取屏幕分辨率
    screenWidth = selfSAS.winfo_screenwidth()
    screenHeight = selfSAS.winfo_screenheight()

    screenWidth = int(screenWidth)
    screenHeight = int(screenHeight)



    # 设置窗口全屏显示
    selfSAS.geometry("%sx%s" % (screenWidth, screenHeight))

    # 设置窗口宽高固定
    selfSAS.resizable(0, 0)

    selfSAS.title("焦虑自评量表")
    selfSAS.configure(bg='white')

    # 焦虑自评表标题
    lbStatus = tkinter.Label(selfSAS, text= '焦虑自评量表', font=('black',40), fg='black', bg='white')
    lbStatus.place(relx=0.40, rely=0.005)


    global entry_Id
    # 患者编号
    tkinter.Label(selfSAS, text='编号：', font=('Arial', 15), fg='black', bg='white').place(relx=0.36, rely=0.08)
    entry_Id = tkinter.Entry(selfSAS, highlightcolor='red', highlightthickness=1)
    entry_Id.place(width=100, height=30, relx=0.40, rely=0.08)

    # 患者年龄
    tkinter.Label(selfSAS, text='年龄：', font=('Arial', 15), fg='black', bg='white').place(relx=0.50, rely=0.08)
    global entry_Age
    entry_Age = tkinter.Entry(selfSAS, highlightcolor='red', highlightthickness=1)
    entry_Age.place(width=100, height=30, relx=0.53, rely=0.08)

    Label(selfSAS, text="选择最适合的答案:（1.没有或很少时间2.小部分时间3.相当多时间4.绝大部分或全部时间）", bg='white').place(relx=0.35, rely=0.12)
    tkinter.Button(selfSAS, text='提交', font=('Arial', 15), width=10, height=2, command=getSelfSASData, bg='white',
                   fg='black',relief=RIDGE,
                   borderwidth=1).place(relx=0.45, rely=0.85, relwidth=0.07, relheight=0.07)

    # 返回selfJudge按钮
    tkinter.Button(selfSAS, text='<返回“自评量表选择', font=('Arial', 15), width=14, height=2, command=back2selfJudge, bg='white',
                   fg='black',relief=RIDGE,
                   borderwidth=1).place(relx=0.05, rely=0.05, relwidth=0.10, relheight=0.05)

    # SDS自评题目
    textList = []  # 存储题库题目
    df = pd.read_excel('./questionBank/selfSAS.xlsx')
    for i in range(len(df['questions'].values)):
        textList.append(df['questions'].values[i])

    #正向问题
    global posOptionList
    posOptionList = [("1.没有或很少时间", 1),
                  ("2.小部分时间", 2),
                  ("3.相当多时间", 3),
                  ("4.绝大部分或全部时间", 4)]

    #反向问题
    global negOptionList
    negOptionList = [("1.没有或很少时间", 4),
                  ("2.小部分时间", 3),
                  ("3.相当多时间", 2),
                  ("4.绝大部分或全部时间", 1)]


    # Canvas,Scrollbar放置在主窗口上
    global canvas
    canvas = Canvas(master=selfSAS,width=880, height=800, bg='white', borderwidth=0)
    # 取消canvas边界
    canvas.config(highlightthickness=0)
    canvas.pack(anchor='center', pady=170)
    scro = Scrollbar(master=selfSAS)
    scro.pack(side='right',fill='y')

    # Frame作为容器放置组件
    frame = Frame(selfSAS, width=310, height=310, highlightbackground="black", highlightcolor="black",
                  highlightthickness=1, borderwidth=4, bg='white')
    frame.place(x=1500, y=10)

    # Frame作为容器放置组件
    frame1 = Frame(canvas, bg='white')
    frame1.pack()
    # 将Frame添加至Canvas上
    canvas.create_window((0, 0), window=frame1, anchor="nw")
    # 添加内容，以grid布局
    i = 0


    # Label(frame1, text="选择最适合的答案:（1.没有或很少时间2.小部分时间3.相当多时间4.绝大部分或全部时间）", bg='white').grid(row=i + 5, columnspan=6)
    global v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20
    i += 7

    # 第一个
    Label(frame1, text=textList[0], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)

    v1 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v1, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1

    # 第二个
    i += 1
    Label(frame1, text=textList[1], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v2 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v2, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1

    # 第三个
    i += 1
    Label(frame1, text=textList[2], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v3 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v3, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[3], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v4 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v4, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[4], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v5 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v5, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[5], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v6 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v6, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[6], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v7 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v7, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[7], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v8 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v8, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[8], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v9 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v9, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[9], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v10 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v10, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[10], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v11 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v11, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[11], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v12 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v12, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[12], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v13 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v13, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[13], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v14 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v14, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[14], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v15 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v15, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[15], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v16 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v16, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[16], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v17 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v17, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[17], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v18 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v18, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[18], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v19 = IntVar()
    i += 1
    j = 0
    for num, check in posOptionList:
        Radiobutton(frame1, text=num, variable=v19, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1
    i += 1
    Label(frame1, text=textList[19], bg='whitesmoke',font=('black',10)).grid(row=i, columnspan=5, sticky=N+S+W+E)
    v20 = IntVar()
    i += 1
    j = 0
    for num, check in negOptionList:
        Radiobutton(frame1, text=num, variable=v20, value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipadx=50, ipady=10)
        j += 1

    # 更新Frame大小，不然没有滚动效果
    frame1.update()
    # 将滚动按钮绑定只Canvas上
    canvas.configure(yscrollcommand=scro.set, scrollregion=canvas.bbox("all"))
    scro.config(command=canvas.yview)

    frame1.bind("<MouseWheel>",processWheel)
    canvas.bind("<MouseWheel>",processWheel)
    selfSAS.bind("<MouseWheel>",processWheel)

    click()
    mainloop()


