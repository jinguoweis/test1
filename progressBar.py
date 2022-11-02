# FILENAME:progressBar.py
import time
import tkinter
import tkinter.ttk


def showProgressBar():
    # 进度值最大值
    progressBarSubWin['maximum'] = ed
    # 进度值初始值
    progressBarSubWin['value'] = beg
    for i in range(int(ed-beg)):
        time.sleep(0.5)
        progressBarSubWin['value'] += 1
        bar.update()

def progressBarSubWin(begin, end):
    global beg, ed
    beg = begin
    ed = end
    global bar
    bar = tkinter.Toplevel()
    bar.geometry('150x120')

    progressbarOne = tkinter.ttk.Progressbar(bar)
    progressbarOne.pack(side=tkinter.TOP)

    confirm_button=tkinter.Button(bar,text="确定",command=showProgressBar)
    confirm_button.pack(side=tkinter.TOP)
    bar.mainloop()

