# import tkinter
# import numpy as np
# import pandas as pd
# import tkinter
# from tkinter import *
# from tkinter import ttk
# import pymysql
# from PIL import Image, ImageTk
# #from aiJudge import aiJudge as aj
# # import otherJudge as otherJudge
# import time
# from scaleDegree import otherSDSFunc
#
#
#
# # # 返回otherJudge
# # def back2otherJudge():
# #     osds.destroy()
# #     otherJudge.otherJudge()
#
# # 插入数据库
# def insert(patientid, age, testScore, answer):
#     global testType
#     testType = 'otherSDS'
#     # 时间戳
#     now = int(round(time.time() * 1000))
#     currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now/1000))
#     # 入库
#     connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='krndb', charset='utf8')
#     cursor = connection.cursor()
#     cursor.execute("insert into score (patientId, age, testType, testScore, answer, insertTime) values (%s, %s, %s, %s, %s, %s)", (patientid, age, testType, testScore, str(answer), currentTime))
#     connection.commit()
#     connection.close()
#     cursor.close()
#
# # 鼠标滚动
# def processWheel(event):
#     a= int(-(event.delta)/60)
#     canvas.yview_scroll(a,'units')
#
# def _submit():
#     id = entry_Id.get()
#     age = entry_Age.get()
#     global answerList
#     answerList = []
#
#     if v1.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第1题选项不能为空！")
#     elif v2.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第2题选项不能为空！")
#     elif v3.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第3题选项不能为空！")
#     elif v4.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第4题选项不能为空！")
#     elif v5.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第5题选项不能为空！")
#     elif v6.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第6题选项不能为空！")
#     elif v7.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第7题选项不能为空！")
#     elif v8.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第8题选项不能为空！")
#     elif v9.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第9题选项不能为空！")
#     elif v10.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第10题选项不能为空！")
#     elif v11.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第11题选项不能为空！")
#     elif v12.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第12题选项不能为空！")
#     elif v13.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第13题选项不能为空！")
#     elif v14.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第14题选项不能为空！")
#     elif v15.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第15题选项不能为空！")
#     elif v16.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第16题选项不能为空！")
#     elif v17.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第17题选项不能为空！")
#     elif v18.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第18题选项不能为空！")
#     elif v19.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第19题选项不能为空！")
#     elif v20.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第20题选项不能为空！")
#     elif v21.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第21题选项不能为空！")
#     elif v22.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第22题选项不能为空！")
#     elif v23.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第23题选项不能为空！")
#     elif v24.get() == 0:
#         tkinter.messagebox.showinfo("提示", "第24题选项不能为空！")
#
#     elif id == '' or age == '':
#         tkinter.messagebox.showinfo('提示', '请输入编号或者年龄')
#     else:
#         answerList.append(optionLists[0][v1.get()-1][0])
#         answerList.append(optionLists[1][v2.get()-1][0])
#         answerList.append(optionLists[2][v3.get()-1][0])
#         answerList.append(optionLists[3][v4.get()-1][0])
#         answerList.append(optionLists[4][v5.get()-1][0])
#         answerList.append(optionLists[5][v6.get()-1][0])
#         answerList.append(optionLists[6][v7.get()-1][0])
#         answerList.append(optionLists[7][v8.get()-1][0])
#         answerList.append(optionLists[8][v9.get()-1][0])
#         answerList.append(optionLists[9][v10.get()-1][0])
#         answerList.append(optionLists[10][v11.get()-1][0])
#         answerList.append(optionLists[11][v12.get()-1][0])
#         answerList.append(optionLists[12][v13.get()-1][0])
#         answerList.append(optionLists[13][v14.get()-1][0])
#         answerList.append(optionLists[14][v15.get()-1][0])
#         answerList.append(optionLists[15][v16.get()-1][0])
#         answerList.append(optionLists[16][v17.get()-1][0])
#         answerList.append(optionLists[17][v18.get()-1][0])
#         answerList.append(optionLists[18][v19.get()-1][0])
#         answerList.append(optionLists[19][v20.get()-1][0])
#         answerList.append(optionLists[20][v21.get()-1][0])
#         answerList.append(optionLists[21][v22.get()-1][0])
#         answerList.append(optionLists[22][v23.get()-1][0])
#         answerList.append(optionLists[23][v24.get()-1][0])
#
#         # 计算得分
#         _sdsScore = v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get() + v7.get() + v8.get() + v9.get() + v10.get() + v11.get() + v12.get() + v13.get() + v14.get() + \
#                     v15.get() + v16.get() + v17.get() + v18.get() + v19.get() + v20.get() + v21.get() + v22.get() + v23.get() + v24.get()-24
#
#         # insert(patientid=id, age=age, testScore=_sdsScore, answer=answerList)
#         # tkinter.messagebox.showinfo('提示', '提交成功，请进行录音检测')
#         # # 程度
#         # otherSDSDegree = otherSDSFunc(_sdsScore)
#         # osds.destroy()
#         # aj(ts=_sdsScore, id=id, age=age, type=testType, deg=otherSDSDegree)
#
#
#
#
# def click():
#     fontsize = 15  # 题卡内容字号
#     width = 30  # 题卡按钮宽度
#     gap = 0.035  # 题卡间距
#
#     i = 0.835  # 左边框距离
#     j = 0.02
#     Label(text="题卡:", font=('black', 20), bg='white').place(width=70, height=30, relx=i, rely=j)
#     j += 0.05
#     if v1.get() == 0:
#         Label(text="1.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="1.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#
#     i += gap
#     if v2.get() == 0:
#         Label(text="2.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="2.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v3.get() == 0:
#         Label(text="3.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="3.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v4.get() == 0:
#         Label(text="4.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="4.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#
#
#     i = 0.835
#     j += 0.042
#     if v5.get() == 0:
#         Label(text="5.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="5.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v6.get() == 0:
#         Label(text="6.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="6.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v7.get() == 0:
#         Label(text="7.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="7.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v8.get() == 0:
#         Label(text="8.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="8.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#
#
#     i = 0.835
#     j += 0.042
#     if v9.get() == 0:
#         Label(text="9.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="9.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v10.get() == 0:
#         Label(text="10.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="10.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v11.get() == 0:
#         Label(text="11.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="11.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v12.get() == 0:
#         Label(text="12.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="12.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#
#     i = 0.835
#     j += 0.042
#     if v13.get() == 0:
#         Label(text="13.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="13.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v14.get() == 0:
#         Label(text="14.", font=('black', fontsize), bg='red').place(width=width, height=30, relx=i, rely=j)
#     else:
#         Label(text="14.", font=('black', fontsize)).place(width=width, height=30, relx=i, rely=j)
#     i += gap
#     if v15.get()==0:
#         Label(text="15.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="15.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#     i += gap
#     if v16.get()==0:
#         Label(text="16.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="16.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#
#
#     i = 0.835
#     j += 0.042
#     if v17.get()==0:
#         Label(text="17.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="17.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#     i+=gap
#     if v18.get()==0:
#         Label(text="18.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="18.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#     i += gap
#     if v19.get()==0:
#         Label(text="19.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="19.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#     i += gap
#     if v20.get()==0:
#         Label(text="20.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="20.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#
# ######
#     i = 0.835
#     j += 0.042
#     if v21.get()==0:
#         Label(text="21.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="21.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#     i+=gap
#     if v22.get()==0:
#         Label(text="22.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="22.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#     i += gap
#     if v23.get()==0:
#         Label(text="23.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="23.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#     i += gap
#     if v24.get()==0:
#         Label(text="24.", font=('black', fontsize), bg='red').place(width=width,height=30, relx=i,rely=j)
#     else:
#         Label(text="24.", font=('black', fontsize)).place(width=width,height=30, relx=i,rely=j)
#
# def otherJudgeSDS():
#
#     global osds
#     osds = tkinter.Tk()  # tkinter窗口
#
#
#     # 获取屏幕分辨率
#     screenWidth = osds.winfo_screenwidth()
#     screenHeight = osds.winfo_screenheight()
#
#     screenWidth = int(screenWidth)
#     screenHeight = int(screenHeight)
#
#
#     # 设置窗口全屏显示
#     osds.geometry("%sx%s" % (screenWidth, screenHeight))
#
#     # 设置窗口宽高固定
#     osds.resizable(0, 0)
#
#     osds.title("汉密顿抑郁量表")
#     osds.configure(bg='white')
#
#     # 焦虑自评表标题
#     lbStatus = tkinter.Label(osds, text= '汉密顿抑郁量表', font=('black',40), fg='black', bg='white')
#     lbStatus.place(relx=0.40, rely=0.0005)
#     global entry_Id
#     # 患者编号
#     tkinter.Label(osds, text='编号：', font=('Arial', 15), fg='black', bg='white').place(relx=0.36, rely=0.08)
#     entry_Id = tkinter.Entry(osds, highlightcolor='red', highlightthickness=1)
#     entry_Id.place(width=100, height=30, relx=0.40, rely=0.08)
#
#     # 患者年龄
#     tkinter.Label(osds, text='年龄：', font=('Arial', 15), fg='black', bg='white').place(relx=0.50, rely=0.08)
#     global entry_Age
#     entry_Age = tkinter.Entry(osds, highlightcolor='red', highlightthickness=1)
#     entry_Age.place(width=100, height=30, relx=0.53, rely=0.08)
#
#     global textList
#     # 题目
#     textList = [] # 存储题库题目
#     df = pd.read_excel('./questionBank/otherSDSquestion.xlsx')
#     for i in range(len(df['questions'].values)):
#         textList.append(df['questions'].values[i])
#
#
#     #选项
#     options = pd.read_excel('./questionBank/otherSDSanswer.xlsx')
#     global optionLists
#     optionLists = []
#     for index in range(len(textList)):
#
#         question = textList[index]
#         optionList = []
#         for j in range(len(options[question].values)):
#             option = options[question].values[j]
#             if option != "*":
#                 optionList.append((option,j+1))
#         optionLists.append(optionList)
#
#
#
#     # # Canvas,Scrollbar放置在主窗口上
#     global canvas
#     canvas = Canvas(master=osds,width=1230, height=900, bg='blue')
#
#     # 取消canvas边界
#     canvas.config(highlightthickness=0)
#
#     scro = Scrollbar(master=osds)
#     scro.pack(side='right',fill='y')
#     canvas.pack(pady=170)
#
#     # Frame作为边框
#     frame = Frame(width=330, height=330, highlightbackground="black", highlightcolor="black",
#                   highlightthickness=1, borderwidth=4, bg='white')
#     frame.place(x=1566, y=8)
#
#
#     # Frame作为容器放置组件
#     frame1 = Frame(canvas, bg='white')
#     frame1.pack()
#     # 将Frame添加至Canvas上
#     canvas.create_window((0,0),window=frame1,anchor="nw")
#     # 添加内容，以grid布局
#     i=0
#
#
#
#     global v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24
#
#     i += 7
#
#
#     # 设置左对齐
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=W)
#     # Label(frame1,text=textList[0], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#
#     # 第一个
#     Label(frame1, text=textList[0], bg='whitesmoke',font=('black',11)).grid(row=i, columnspan=5, sticky=W)
#
#     v1 = IntVar()
#     i +=1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[0]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v1,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v1,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     #第二个
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[1], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v2 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[1]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v2,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v2,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     #第三个
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[2], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v3 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[2]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v3,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v3,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[3], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v4 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[3]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v4,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v4,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[4], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v5 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[4]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v5,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v5,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[5], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v6 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[5]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v6,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v6,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[6], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v7 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[6]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v7,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v7,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[7], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v8 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[7]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v8,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v8,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[8], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v9 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[8]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v9,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v9,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[9], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v10 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[9]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v10,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v10,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     # Label(frame1, bg='whitesmoke').grid(row=i, columnspan=5, sticky=N + S + W + E)
#     Label(frame1,text=textList[10], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v11 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[10]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v11,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v11,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[11], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v12 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[11]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v12,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v12,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[12], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v13 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[12]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v13,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v13,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[13], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v14 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[13]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v14,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v14,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[14], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v15 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[14]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v15,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v15,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[15], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v16 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[15]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v16,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v16,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[16], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v17 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[16]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v17,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v17,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[17], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v18 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[17]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v18,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v18,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[18], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v19 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[18]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v19,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v19,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[19], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v20 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[19]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v20,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v20,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[20], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v21 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[20]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v21,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v21,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[21], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v22 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[21]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v22,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v22,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[22], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v23 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[22]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v23,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v23,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#     ####
#     i += 1
#     Label(frame1,text=textList[23], bg='whitesmoke',font=('black',11)).grid(row=i,columnspan=5,sticky=W)
#     v24 = IntVar()
#     i += 1
#     j = 0
#
#     l = 0
#     k = 0
#     for num, check in optionLists[23]:
#         if k < 3:
#             Radiobutton(frame1, text=num, variable=v24,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=j, sticky=W, ipady=5)
#             j += 1
#         else:
#             if l == 0:
#                 i+=1
#             Radiobutton(frame1, text=num, variable=v24,value=check, bg='white', font=('black',10),command = click).grid(row=i, column=l, sticky=W, ipady=5)
#             l += 1
#         k += 1
#
#
#
#     # # 返回otherJudge按钮
#     # tkinter.Button(osds, text='<返回“他评量表选择”', font=('Arial', 15), width=14, height=2, bg='white',
#     #                fg='black',relief=RIDGE, command=back2otherJudge,
#     #                borderwidth=1).place(relx=0.05, rely=0.05, relwidth=0.10, relheight=0.05)
#
#     #提交按钮
#     Button(osds,text="提交", font=('Arial', 15), width=10, height=2, bg='white',
#                    fg='black',relief=RIDGE, command=_submit,
#                    borderwidth=1).place(relx=0.45, rely=0.85, relwidth=0.07, relheight=0.07)  # 底部按钮
#         # .place(relx=0.05, rely=0.12, relwidth=0.09, relheight=0.05)  # 顶部左侧按钮
#
#     # 更新Frame大小，不然没有滚动效果
#     frame1.update()
#     # 将滚动按钮绑定只Canvas上
#     canvas.configure(yscrollcommand=scro.set, scrollregion=canvas.bbox("all"))
#     scro.config(command=canvas.yview)
#
#     frame1.bind("<MouseWheel>",processWheel)
#     canvas.bind("<MouseWheel>",processWheel)
#     osds.bind("<MouseWheel>",processWheel)
#
#     click()
#     mainloop()
#
# ###########录音
# def resize2(w, h, w_box, h_box, pil_image):
#     '''
#         resize a pil_image object so it will fit into
#         a box of size w_box times h_box, but retain aspect ratio
#         对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
#     '''
#     f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
#     f2 = 1.0 * h_box / h
#     factor = min([f1, f2])
#     width = int(w * factor)
#     height = int(h * factor)
#     return pil_image.resize((width, height), Image.ANTIALIAS)
#
#
# def nextPic():
#     canvas = tkinter.Canvas(judge, height=600, width=800, bg='white')
#     canvas.create_image(1, 1, anchor='nw', image=tk_image2)
#     canvas.place(relx=0.29, rely=0)
#     canvas.config(highlightthickness=0)
#
# def prePic():
#     canvas = tkinter.Canvas(judge, height=600, width=800, bg='white')
#     canvas.create_image(1, 1, anchor='nw', image=tk_image1)
#     canvas.place(relx=0.29, rely=0)
#     canvas.config(highlightthickness=0)
#
# def aiJudge(ts, id, age, type, deg):
#     global judge
#     judge = tkinter.Tk()  # tkinter窗口
#
#     global selfSasSc, Id, Age, testType, Deg
#     selfSasSc = ts  # 量表得分
#     Id = id  # 患者ID
#     Age = age  # 年龄
#     testType = type  # 录音类型
#     Deg = deg  # 程度
#     # 获取屏幕分辨率
#     screenWidth = judge.winfo_screenwidth()
#     screenHeight = judge.winfo_screenheight()
#
#     screenWidth = int(screenWidth)
#     screenHeight = int(screenHeight)
#
#
#
#     # 设置窗口全屏显示
#     judge.geometry("%sx%s" % (screenWidth, screenHeight))
#     # judge.geometry("1440x900")
#     # 设置窗口宽高固定
#     judge.resizable(0, 0)
#
#     judge.title("心理检测")
#     judge.configure(bg='white')
#
#
#     # page1
#     global tk_image1
#     # pil_image1 = Image.open(publicPath + r'\statics\chapter\page1.jpg')
#     pil_image1 = Image.open(r'.\statics\chapter\page1.jpg')
#     w, h = pil_image1.size
#     pil_image_resized = resize2(w=w, h=h, w_box=800, h_box=600, pil_image=pil_image1)
#     tk_image1 = ImageTk.PhotoImage(pil_image_resized)
#
#     # page2
#     global tk_image2
#     # pil_image2 = Image.open(publicPath + r'\statics\chapter\page2.jpg')
#     pil_image2 = Image.open(r'.\statics\chapter\page2.jpg')
#     w, h = pil_image2.size
#     pil_image_resized = resize2(w=w, h=h, w_box=800, h_box=600, pil_image=pil_image2)
#     tk_image2 = ImageTk.PhotoImage(pil_image_resized)
#
#     # 展示
#     pil_image_resized4show = resize2(w=w, h=h, w_box=800, h_box=600, pil_image=pil_image1)
#     tk_image4show = ImageTk.PhotoImage(pil_image_resized4show)
#     canvas = tkinter.Canvas(judge, height=600, width=800, bg='white', borderwidth=0)
#     canvas.create_image(1, 1, anchor='nw', image=tk_image4show)
#     canvas.config(highlightthickness=0)
#     canvas.place(relx=0.29, rely=0)
#
#     # 换页按钮
#     tkinter.Button(judge, text='上一页', width=10, height=3, command=prePic, borderwidth=2, relief=GROOVE).place(
#         relx=0.05, rely=0.33)
#     tkinter.Button(judge, text='下一页', width=10, height=3, command=nextPic, borderwidth=2, relief=GROOVE).place(
#         relx=0.88, rely=0.33)
#
#
#     # # 开始、结束按键
#     # tkinter.Button(judge, text='开始', font=('Arial', 15), width=10, height=2, command=action, bg='green', fg='#ffffff',
#     #                borderwidth=5).place(relx=0.20, rely=0.78, relwidth=0.1, relheight=0.1)
#     # tkinter.Button(judge, text='结束', font=('Arial', 15), width=10, height=2, command=end, bg='red', fg='#ffffff',
#     #                borderwidth=5).place(relx=0.70, rely=0.78, relwidth=0.1, relheight=0.1)
#
#
#     # # 预览诊断报告按键
#     # tkinter.Button(judge, text='预览诊断报告', font=('Arial', 10), width=15, height=2, command=showReport).place(
#     #     relx=0.70, rely=0.68)  # relwidth=0.1, relheight=0.1
#     #
#     # # 返回mainPage按钮
#     # tkinter.Button(judge, text='<返回', font=('Arial', 15), width=10, height=2, command=back2SelectFunc, bg='white',
#     #                fg='black',relief=RIDGE
#     #                borderwidth=1).place(relx=0.05, rely=0.05, relwidth=0.07, relheight=0.07)
#
#     global lbStatus
#     lbStatus = tkinter.Label(judge, text='等待录音', font=('black', 40), fg='red', bg='white')  # 显示绿色状态字
#     lbStatus.place(relx=0.43, rely=0.80)
#     # window.protocol("WM_DELETE_WINDOW",callback)
#
#     # tkinter.messagebox.showinfo(title="提示", message="点击”开始“录音，点击”结束“，关闭录音")
#
#     judge.mainloop()
#
# aiJudge(1,1,1,1,1)
# #otherJudgeSDS()
