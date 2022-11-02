import os
import numpy as np
from extract_feats import mylibrosa as lf
import models
import utils


def predict(config, audio_path: str, model) -> None:
    """
    预测音频情感

    Args:
        config: 配置项
        audio_path (str): 要预测的音频路径
        model: 加载的模型
    """

    # utils.play_audio(audio_path)


    test_feature = lf.get_data(config, audio_path, config.predict_feature_path_librosa, train=False)

    """
        maxIndex: 最大值下标
        secIndex: 次大值下标
        probability: 最大值概率
        secondProb: 次大值概率
    """
    maxIndex, secIndex, maxProb ,secondProb= model.predict(test_feature)

    # predict_classes()、predict_proba()方法在tf.keras.Sequential模块下有效，在tf.keras.Model模块下无效。
    # https: // blog.csdn.net / chenhepg / article / details / 124237827
    # result_prob = model.predict_proba(test_feature)

    # utils.radar(result_prob, config.class_labels)

    return config.class_labels[int(maxIndex)], config.class_labels[int(secIndex)], maxProb, secondProb


def preMain():
    audio_path = r'.\aiJudge'

    fileList = []
    for filename in os.listdir(audio_path):
        file = audio_path + '\\' + filename
        fileList.append(file)
    # print(fileList)

    config = utils.parse_opt()
    model = models.load(config)

    # res: 类别标签， labelProb:概率
    maxLab, secLab, maxlabelProb, secondLabelProb = predict(config, fileList[0], model)
    if maxLab == 'jl':
        maxLab = 'SAS'  # 焦虑
    elif maxLab == 'yy':
        maxLab = 'SDS'  # 抑郁
    elif maxLab == 'zc':
        maxLab = 'NEU'  #  正常

    if secLab == 'jl':
        secLab = 'SAS'  # 焦虑
    elif secLab == 'yy':
        secLab = 'SDS'  # 抑郁
    elif secLab == 'zc':
        secLab = 'NEU'  #  正常
    return maxLab, secLab, maxlabelProb, secondLabelProb