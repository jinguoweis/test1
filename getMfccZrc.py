# FILENAME:getMfccZrc.py

import librosa.display
from random import shuffle
import numpy as np

def getMZ(tarFile):

    X, sample_rate = librosa.load(tarFile, sr=None)  # 信号值（波形），采样率


    # 产生信号的总时间长度t = dt*采样数 = 采样数/fs
    # 产生信号的周期数 = 总时间长度/T = 总时间长度信号频率 = 采样数/采样频率信号频率
    max_ = X.shape[0] / sample_rate
    if True:   # 是否填充
        length = (max_ * sample_rate) - X.shape[0]
        X = np.pad(X, (0, int(length)), 'constant')  # ‘constant’——表示连续填充相同的值

    zerocr = np.mean(librosa.feature.zero_crossing_rate(X))

    # 使用系数为50的MFCC特征
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=50).T, axis=0)
    mfccsstd = np.std(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=50).T, axis=0)

    mfcc = np.concatenate((mfccs,mfccsstd))
    return zerocr, mfcc