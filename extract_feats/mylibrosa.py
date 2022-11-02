import os
import re
import sys
import time
import librosa
import librosa.display
from random import shuffle
import numpy as np
from typing import Tuple, Union
import pickle
import pandas as pd
# from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
import joblib



def features(X, sample_rate: float) -> np.ndarray:
    # 基频特征
    stft = np.abs(librosa.stft(X))

    # fmin 和 fmax 对应于人类语音的最小最大基本频率
    pitches, magnitudes = librosa.piptrack(X, sr=sample_rate, S=stft, fmin=70, fmax=400)
    pitch = []
    for i in range(magnitudes.shape[1]):
        index = magnitudes[:, 1].argmax()
        pitch.append(pitches[index, i])

    pitch_tuning_offset = librosa.pitch_tuning(pitches)
    pitchmean = np.mean(pitch)
    pitchstd = np.std(pitch)
    pitchmax = np.max(pitch)
    pitchmin = np.min(pitch)

    # 频谱质心
    cent = librosa.feature.spectral_centroid(y=X, sr=sample_rate)
    cent = cent / np.sum(cent)
    meancent = np.mean(cent)
    stdcent = np.std(cent)
    maxcent = np.max(cent)

    # 谱平面
    flatness = np.mean(librosa.feature.spectral_flatness(y=X))

    # 使用系数为50的MFCC特征
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=50).T, axis=0)
    mfccsstd = np.std(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=50).T, axis=0)
    mfccmax = np.max(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=50).T, axis=0)

    # 色谱图(色度频率)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)

    # 梅尔频谱
    melsep = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0)

    # ottava对比（频谱对比、谱对比度）
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)

    # 过零率
    zerocr = np.mean(librosa.feature.zero_crossing_rate(X))

    S, phase = librosa.magphase(stft)
    meanMagnitude = np.mean(S)
    stdMagnitude = np.std(S)
    maxMagnitude = np.max(S)

    # 均方根能量
    rmse = librosa.feature.rmse(S=S)[0]
    meanrms = np.mean(rmse)
    stdrms = np.std(rmse)
    maxrms = np.max(rmse)

    ext_features = np.array([
        flatness, zerocr, meanMagnitude, maxMagnitude, meancent, stdcent,
        maxcent, stdMagnitude, pitchmean, pitchmax, pitchstd,
        pitch_tuning_offset, meanrms, maxrms, stdrms
    ])

    ext_features = np.concatenate((ext_features, mfccs, mfccsstd, mfccmax, chroma, melsep, contrast))
    # print(ext_features)
    return ext_features

def extract_features(file: str, pad: bool = False) -> np.ndarray:
    X, sample_rate = librosa.load(file, sr=None)  # 信号值（波形），采样率


    # 产生信号的总时间长度t = dt*采样数 = 采样数/fs
    # 产生信号的周期数 = 总时间长度/T = 总时间长度信号频率 = 采样数/采样频率信号频率
    max_ = X.shape[0] / sample_rate
    if pad:   # 是否填充
        length = (max_ * sample_rate) - X.shape[0]
        X = np.pad(X, (0, int(length)), 'constant')  # ‘constant’——表示连续填充相同的值
    return features(X, sample_rate)

def get_max_min(files: list) -> Tuple[float]:
    min_, max_ = 100, 0

    for file in tqdm(files, total=len(files)):
        sound_file, samplerate = librosa.load(file, sr=None)
        # print("sound_fileshape:{}".format(sound_file.shape))
        t = sound_file.shape[0] / samplerate
        if t < min_:
            min_ = t
        if t > max_:
            max_ = t

    return max_, min_

def get_data_path(data_path: str, class_labels: list) -> list:
    """
    获取所有音频的路径

    Args:
        data_path (str): 数据集文件夹路径
        class_labels (list): 情感标签
    Returns:
        wav_file_path (list): 所有音频的路径
    """
    # print("data_path:{}".format(data_path))
    wav_file_path = []

    # cur_dir = os.getcwd()  # 获取当前路径
    # print("cur_dir:{}".format(cur_dir))
    # sys.stderr.write('Curdir: %s\n' % cur_dir)  # 错误信息写入文件
    # os.chdir(data_path)  # 切换路径

    # 遍历文件夹
    for _, directory in enumerate(class_labels):
        # print("directory:{}".format(directory))        # os.chdir(directory)

        # 读取该文件夹下的音频
        for filename in os.listdir('/home/wangjl/test/Speech-Emotion-Re-master/Dataset2/{}'.format(directory)):
            # if not filename.endswith('wav'):
            #     continue
            # filepath = os.path.join(os.getcwd(), filename)
            filepath = os.getcwd() + '/Dataset2/{}/'.format(directory) + filename
            wav_file_path.append(filepath)

        # os.chdir('..')
    # os.chdir(cur_dir)

    print("wav_file_path:{}".format(wav_file_path))

    shuffle(wav_file_path)  # 将列表的所有元素随机排序。
    return wav_file_path, wav_file_path

def load_feature(config, feature_path: str, train: bool) -> Union[Tuple[np.ndarray], np.ndarray]:
    """
    从 `csv` 文件中加载特征数据

    Args:
        config: 配置项
        feature_path (str): 特征文件路径
        train (bool): 是否为训练数据

    Returns:
        - X (Tuple[np.ndarray]): 训练特征、测试特征和对应的标签
        - X (np.ndarray): 预测特征
    """

    # print("feature_path:{}".format(feature_path))
    features = pd.DataFrame(
        data = joblib.load(feature_path),
        columns = ['file_name', 'features', 'emotion']
        # columns = ['features', 'emotion']
    )
    
    X = list(features['features'])
    Y = list(features['emotion'])

    # 标准化模型路径
    scaler_path = os.path.join(config.checkpoint_path, 'SCALER_LIBROSA.m')

    if train == True:
        # print("x:{}".format(X))
        # 标准化数据
        scaler = StandardScaler().fit(X)


        # 保存标准化模型
        joblib.dump(scaler, scaler_path)
        X = scaler.transform(X)


        # x_train, y_train = X, Y
        # return x_train, y_train
        # 在保持输入数据不变的情况下,如果random_state等于某个固定的值,将得到同样的数据划分
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        return x_train, x_test, y_train, y_test
        

    else:
        # 标准化数据
        # 加载标准化模型
        scaler = joblib.load(scaler_path)
        X = scaler.transform(X)
        return X

# train:True
def get_data(config, data_path: str, feature_path: str, train: bool) -> Union[Tuple[np.ndarray], np.ndarray]:
    """
    提取所有音频的特征: 遍历所有文件夹, 读取每个文件夹中的音频, 提取每个音频的特征，把所有特征保存在 `feature_path` 路径下。

    Args:
        confi: 配置项
        data_path (str): 数据集文件夹/测试文件路径
        feature_path (str): 保存特征的路径
        train (bool): 是否为训练数据

    Returns:
        - train = True: 训练特征、测试特征和对应的标签
        - train = False: 预测特征
    """

    if(train == True):
        files, wavList = get_data_path(data_path, config.class_labels)  # class_labels: ["angry", "fear", "happy", "neutral", "sad", "surprise"]
        # for i in tqdm(range(len(wavList))):
        max_, min_ = get_max_min(files)
    
        print("===========统长结束===========")

        mfcc_data = []
        print("===========提取特征===========")
        for file in tqdm(files, total=len(wavList)):
            # label = re.findall(".(.*)-.*", file)[0]
            label = re.findall("Dataset2/.*?/", file)[0][9:11]  # 获取当前文件标签
            # print("label:{}".format(label))

            # 三分类
            # if(label == "sad" or label == "neutral"):
            #     label = "neutral"
            # elif(label == "angry" or label == "fear"):
            #     label = "negative"
            # elif(label == "happy" or label == "surprise"):
            #     label = "positive"

            features = extract_features(file, max_)
            # mfcc_data.append([features, config.class_labels.index(label)])
            mfcc_data.append([file, features, config.class_labels.index(label)])
    else:
        features = extract_features(data_path)
        mfcc_data = [[data_path, features, -1]]

    # print("mfcc_data:{}".format(mfcc_data))

    # cols = ['file_name', 'features', 'emotion']
    # mfcc_pd = pd.DataFrame(data=mfcc_data, columns=cols)

    # 数据预处理结束，保存mfcc特征到feature_path
    pickle.dump(mfcc_data, open(feature_path, 'wb'))


    # train.py中，返回调用load_feature()
    return load_feature(config, feature_path, train=train)
