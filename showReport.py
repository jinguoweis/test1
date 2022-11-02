# FILENAME:showReport.py
from tkinter import *
import tkinter
import tkinter.font as tkFont
import os, sys, stat
import win32print
import win32api
import tkinter as tk
import tkinter.filedialog
from PIL import Image,ImageTk



def print_start():
    audio_path = r'.\aiJudge'
    imgPath = r'.\waveImg'

    # 文件目录前缀
    prefix = os.getcwd()
    file_path= prefix +  r"\genReport\{}_{}.pdf".format(srId,srAge)

    open(file_path,'r')
    win32api.ShellExecute(
        0,
        "print",
        file_path,
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    tkinter.messagebox.showinfo("提示", "打印成功！")

    # 删除文件
    os.remove(audio_path + r"\{}_{}.wav".format(srId, srAge))
    os.remove(imgPath + r'\{}_{}.jpg'.format(srId, srAge))
    report.destroy()
    tkinter.messagebox.showinfo('提示', '打印成功')

# 主循环
def printReprot(id, age, score, mfcc, zcr, label, deg, img, type, degree):
    global srId
    global srAge
    global Deg

    srId = id
    srAge = age
    Deg = degree
    global report
    report = tkinter.Toplevel()  # 创建弹窗
    report.geometry("700x980+600+50")
    report.configure(bg='white')
    report.title("心理诊疗检测报告")


    # 标题
    fm1 = Frame(report, bg='white')
    fm1.pack(side=TOP, pady=15, fill=BOTH, expand=YES)
    Label(fm1, text="心理诊疗检测报告", font=tkFont.Font(size=15), bg='white').pack(side='top')

    # 基本信息
    fm2 = Frame(report, bg='white')
    fm2.pack(pady=10, padx=80, fill=BOTH, expand=YES)
    Label(fm2, text="编号：{}".format(id), bg='white').pack(side='left')
    Label(fm2, text="年龄：{}".format(age), bg='white').pack(side='left', padx=50)

    Label(report, text="—————————————————————————————————————", bg='white').pack()

    # mfcc
    mf = Frame(report, bg='white')
    mf.pack(pady=10, padx=80, fill=BOTH, expand=YES)
    Label(mf, text="Mel-Frequency Cipstal Coefficients(MFCC):\n{}".format(mfcc), bg='white').pack(side='left')

    #量表类型
    tableType = Frame(report, bg='white')
    tableType.pack(pady=10, padx=80, fill=BOTH, expand=YES)
    Label(tableType, text="Diagnosis type: {}".format(type), bg='white').pack(side='left')

    # 量表分数
    fm3 = Frame(report, bg='white')
    fm3.pack(pady=10, padx=80, fill=BOTH, expand=YES)
    Label(fm3, text="Assessment Scale Score: {}_{}".format(score, Deg), bg='white').pack(side='left')

    # 展示过零率
    fm4 = Frame(report, bg='white')
    fm4.pack(padx=80, fill=BOTH, expand=YES)
    Label(fm4, text="Zero-Crossing Rate(ZCR): {:.7f}".format(zcr), bg='white').pack(side='left')

    # 展示波形图
    photo = Image.open(img)
    photo = photo.resize((600, 200))
    img_png = ImageTk.PhotoImage(photo)
    label_img = tk.Label(report, image=img_png, bg='white')
    label_img.pack()

    # 信息
    fm8 = Frame(report, bg='white')
    fm8.pack(pady=10, padx=80, fill=BOTH, expand=YES)
    Label(fm8, text="Predict Class: {}_{}".format(label, deg), bg='white').pack(side='left')

    # 创建一个按钮,并把上面那个函数绑定过来
    button = tkinter.Button(master=report, text="打印报告", command=print_start)
    # 按钮放在下边
    button.pack(side=tkinter.BOTTOM)

    report.mainloop()

