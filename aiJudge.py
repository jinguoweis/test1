# FILENAME:aiJudge.py

# -*- coding: cp936 -*-
import time
from tkinter import *
import pyaudio
import threading
import wave
import tkinter
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import predict
import librosa
import os, sys, stat

import progressBar
import selectFunc as selectFunc
import selfJudge as selfJudge
from generateReport import genReport as gr
import win32print
import win32api
from getMfccZrc import getMZ as mz
from utils.plot import waveform as wf
from judgeDegree import judgeDeg as jd
from showReport import printReprot as pr


class Recorder():
    def __init__(self, chunk=1024, channels=1, rate=64000):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self._running = True
        self._frames = []

    def start(self):

        threading._start_new_thread(self.__recording, ())

    def __recording(self):
        self._running = True
        self._frames = []
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        while (self._running):
            data = stream.read(self.CHUNK)
            self._frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()

    def stop(self):
        self._running = False

    # 获取mp3/wav音频文件时长
    def get_duration_mp3_and_wav(self, file_path):
        """
        获取mp3/wav音频文件时长
        :param file_path:
        :return:
        """
        # with open(file_path, 'r+') as fp:
        duration = librosa.get_duration(filename=file_path)
        return duration


    def save(self, filename):
        p = pyaudio.PyAudio()
        if not filename.endswith(".wav"):
            filename = filename + ".wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames))
        wf.close()


def action():

    global rec
    global begin
    rec = Recorder()
    lbStatus['text'] = '正在录音...'
    lbStatus['fg'] = 'green'
    rec.start()


def end():
    rec.stop()
    lbStatus['text'] = '等待录音'
    lbStatus['fg'] = 'red'

    id = Id
    age = Age
    rec.save(r".\aiJudge\{}_{}.wav".format(id, age))
    # 获取时长
    duration = rec.get_duration_mp3_and_wav(file_path=r".\aiJudge\{}_{}.wav".format(id, age))

    # 56s
    if duration < 1:
        os.remove(r".\aiJudge\{}_{}.wav".format(id, age))
        tkinter.messagebox.showwarning("警告", "录制时间较短，请重新录制！")
    else:
        ans = tkinter.messagebox.askokcancel(message='是否使用当前录音')
        if (ans == True):
            flag = os.path.exists(r'.\aiJudge')
            if (flag == False):
                os.makedirs(r'.\aiJudge')
        else:
            os.remove(r".\aiJudge\{}_{}.wav".format(id, age))


def resize(w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
    w, h = pil_image.size  # 获取图像的原始大小
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


# def click(check):
#     cmd = 'matchbox-keyboard'
#     os.system(cmd)

# 关闭按钮失效
def callback():
    pass


def resize2(w, h, w_box, h_box, pil_image):
    '''
        resize a pil_image object so it will fit into
        a box of size w_box times h_box, but retain aspect ratio
        对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
    '''
    f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


# 生成预测结果
def showReport():

    # 情绪分析前检测是否存储录音文件
    audio_path = r'.\aiJudge'
    flag = os.path.exists(r'./aiJudge/{}_{}.wav'.format(Id, Age))  # 用户是否录音，未录音则提示

    if (flag == False):
        tkinter.messagebox.showwarning("警告", "请先录音！")
    else:
        id = Id
        age = Age
        global maxClass
        maxClass, secClass, prob, secondProb = predict.preMain()  # 预测标签
        # 计算程度
        degree = jd(prob=prob)
        secDegree = jd(prob=secondProb)
        # 计算过零率、mfcc
        zcr, mfcc = mz(tarFile=audio_path + r"\{}_{}.wav".format(id, age))
        # 绘制波形图
        wf(file_path=r".\aiJudge\{}_{}.wav".format(id, age), id=id, age=age)
        # 保存为pdf
        gr(id=id, age=age, zr=zcr, mfcc=mfcc, maxDeg=degree, secDeg=secDegree, selfSASc=selfSasSc,
           file=r'./genReport/{}_{}.pdf'.format(id,age), preclass=maxClass, secPreClass=secClass, type=testType, degree=Deg, maxprob=prob, secprob=secondProb)
        # 展示报告
        pr(id=id, age=age, score=selfSasSc, mfcc=mfcc, zcr=zcr, label=maxClass, deg=degree, img=r'./waveImg/{}_{}.jpg'.format(id, age), type=testType, degree=Deg)


def back2SelectFunc():
    judge.destroy()
    selectFunc.selectFunc()


def nextPic():
    canvas = tkinter.Canvas(judge, height=600, width=800, bg='white')
    canvas.create_image(1, 1, anchor='nw', image=tk_image2)
    canvas.place(relx=0.29, rely=0)
    canvas.config(highlightthickness=0)


def prePic():
    canvas = tkinter.Canvas(judge, height=600, width=800, bg='white')
    canvas.create_image(1, 1, anchor='nw', image=tk_image1)
    canvas.place(relx=0.29, rely=0)
    canvas.config(highlightthickness=0)


def aiJudge(ts, id, age, type, deg):
    global judge
    judge = tkinter.Tk()  # tkinter窗口

    global selfSasSc, Id, Age, testType, Deg
    selfSasSc = ts  # 量表得分
    Id = id  # 患者ID
    Age = age  # 年龄
    testType = type  # 录音类型
    Deg = deg  # 程度
    # 获取屏幕分辨率
    screenWidth = judge.winfo_screenwidth()
    screenHeight = judge.winfo_screenheight()

    screenWidth = int(screenWidth)
    screenHeight = int(screenHeight)



    # 设置窗口全屏显示
    judge.geometry("%sx%s" % (screenWidth, screenHeight))
    # judge.geometry("1440x900")
    # 设置窗口宽高固定
    judge.resizable(0, 0)

    judge.title("心理检测")
    judge.configure(bg='white')


    # page1
    global tk_image1
    # pil_image1 = Image.open(publicPath + r'\statics\chapter\page1.jpg')
    pil_image1 = Image.open(r'.\statics\chapter\page1.jpg')
    w, h = pil_image1.size
    pil_image_resized = resize2(w=w, h=h, w_box=800, h_box=600, pil_image=pil_image1)
    tk_image1 = ImageTk.PhotoImage(pil_image_resized)

    # page2
    global tk_image2
    # pil_image2 = Image.open(publicPath + r'\statics\chapter\page2.jpg')
    pil_image2 = Image.open(r'.\statics\chapter\page2.jpg')
    w, h = pil_image2.size
    pil_image_resized = resize2(w=w, h=h, w_box=800, h_box=600, pil_image=pil_image2)
    tk_image2 = ImageTk.PhotoImage(pil_image_resized)

    # 展示
    pil_image_resized4show = resize2(w=w, h=h, w_box=800, h_box=600, pil_image=pil_image1)
    tk_image4show = ImageTk.PhotoImage(pil_image_resized4show)
    canvas = tkinter.Canvas(judge, height=600, width=800, bg='white', borderwidth=0)
    canvas.create_image(1, 1, anchor='nw', image=tk_image4show)
    canvas.config(highlightthickness=0)
    canvas.place(relx=0.29, rely=0)

    # 换页按钮
    tkinter.Button(judge, text='上一页', width=10, height=3, command=prePic, borderwidth=2, relief=GROOVE).place(
        relx=0.05, rely=0.33)
    tkinter.Button(judge, text='下一页', width=10, height=3, command=nextPic, borderwidth=2, relief=GROOVE).place(
        relx=0.88, rely=0.33)


    # 开始、结束按键
    tkinter.Button(judge, text='开始', font=('Arial', 15), width=10, height=2, command=action, bg='green', fg='#ffffff',
                   borderwidth=5).place(relx=0.20, rely=0.78, relwidth=0.1, relheight=0.1)
    tkinter.Button(judge, text='结束', font=('Arial', 15), width=10, height=2, command=end, bg='red', fg='#ffffff',
                   borderwidth=5).place(relx=0.70, rely=0.78, relwidth=0.1, relheight=0.1)


    # 预览诊断报告按键
    tkinter.Button(judge, text='预览诊断报告', font=('Arial', 10), width=15, height=2, command=showReport).place(
        relx=0.70, rely=0.68)  # relwidth=0.1, relheight=0.1

    # 返回mainPage按钮
    tkinter.Button(judge, text='<返回', font=('Arial', 15), width=10, height=2, command=back2SelectFunc, bg='white',
                   fg='black',relief=RIDGE,
                   borderwidth=1).place(relx=0.05, rely=0.05, relwidth=0.07, relheight=0.07)

    global lbStatus
    lbStatus = tkinter.Label(judge, text='等待录音', font=('black', 40), fg='red', bg='white')  # 显示绿色状态字
    lbStatus.place(relx=0.43, rely=0.80)
    # window.protocol("WM_DELETE_WINDOW",callback)

    tkinter.messagebox.showinfo(title="提示", message="点击”开始“录音，点击”结束“，关闭录音")

    judge.mainloop()

