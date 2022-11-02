import math
import os
from typing import Optional
from abc import ABC, abstractmethod
from matplotlib.pyplot import axis, xticks
import numpy as np
from tensorflow.keras.models import Sequential, model_from_json
from ..base import BaseModel
from utils import curve
import time
import tensorflow as tf
import tensorflow.keras
from tensorflow.python.keras.utils import np_utils




class DNN(BaseModel, ABC):
    """
    所有基于 Keras 的深度学习模型的基类

    Args:
        n_classes (int): 标签种类数量
        lr (float): 学习率
    """
    def __init__(self, model: Sequential, trained: bool = False) -> None:
        super(DNN, self).__init__(model, trained)
        # print(self.model.summary())

    def save(self, path: str, name: str) -> None:
        """
        保存模型

        Args:
            path (str): 模型路径
            name (str): 模型文件名
        """
        h5_save_path = os.path.join(path, name + '.h5')
        self.model.save_weights(h5_save_path)

        save_json_path = os.path.join(path, name + '.json')
        with open(save_json_path, "w") as json_file:
            json_file.write(self.model.to_json())

    @classmethod
    def load(cls, path: str, name: str):
        """
        加载模型

        Args:
            path (str): 模型路径
            name (str): 模型文件名
        """
        # 加载 json
        model_json_path = os.path.abspath(os.path.join(path, name + '.json'))
        json_file = open(model_json_path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)

        # 加载权重
        model_path = os.path.abspath(os.path.join(path, name + '.h5'))
        model.load_weights(model_path)

        return cls(model, True)

    def train(
        self,
        # reduce,
        # checkp,
        x_train: np.ndarray,
        y_train: np.ndarray,
        x_val: Optional[np.ndarray] = None,
        y_val: Optional[np.ndarray] = None,
        batch_size: int = 10,
        n_epochs: int = 100
    ) -> None:
        """
        训练模型

        Args:
            x_train (np.ndarray): 训练集样本
            y_train (np.ndarray): 训练集标签
            x_val (np.ndarray, optional): 测试集样本
            y_val (np.ndarray, optional): 测试集标签
            batch_size (int): 批大小
            n_epochs (int): epoch 数
        """



        print("enter dnn.py")

        if x_val is None or y_val is None:
            print("x_val is None or y_val is None")
            x_val, y_val = x_train, y_train 

        # print(x_train.shape)
        # print(x_val.shape)
        x_train, x_val = self.reshape_input(x_train), self.reshape_input(x_val)
        # print(x_train.shape)
        # print(x_val.shape)
        
        # callbacks =[
        #     reduce, checkp
        # ]

        # x_train = tf.convert_to_tensor
        # y_train = tf.convert_to_tensor
        # x_val = tf.convert_to_tensor
        # y_val = tf.convert_to_tensor
        # LSTM 模型通过调用 fit() 函数进行训练,返回一个叫作 history 的变量
        # 该变量包含损失函数的轨迹，以及在模型编译过程中被标记出来的任何一个度量指标。这些得分会在每一个 epoch 的最后被记录下来。


        # x_train = np.expand_dims(x_train, axis=1)
        
        # y_train = np.expand_dims(y_train, axis=1)
        # x_val = np.expand_dims(x_val, axis=1)
        # y_val = np.expand_dims(y_val, axis=1)
        # print("y_val_shape:{}".format(y_val.shape))



        history = self.model.fit(
            x_train, y_train,
            batch_size = batch_size,
            epochs = n_epochs,
            shuffle = False, # 每个 epoch 开始前随机排列训练数据
            validation_data = (x_val, y_val),
            # callbacks = callbacks
        )

        # print("history:{}".format(history.history))


        nowTime = time.time()
        # if (os.path.exists('./lossAndAcc/la/' + str(nowTime)) == False):
        os.makedirs('/home/8TDisk/wangjl/SER/lossAndAcc/' + str(nowTime))

        filePath = str('/home/8TDisk/wangjl/SER/lossAndAcc/' + str(nowTime))

        # 绘图
        # 训练集上的损失和准确率
        acc = history.history['accuracy']
        loss = history.history['loss']
        # 验证集上的损失和准确率
        val_acc = history.history['val_accuracy']
        val_loss = history.history['val_loss']

        curve(acc, val_acc, 'Accuracy', 'acc', filePath, nowTime)  # 绘制损失值和准确率曲线
        curve(loss, val_loss, 'Loss', 'loss', filePath, nowTime)

        self.trained = True

    def predict(self, samples: np.ndarray) -> np.ndarray:
        """
        预测音频的情感

        Args:
            samples (np.ndarray): 需要识别的音频特征

        Returns:
            results (np.ndarray): 识别结果
        """



        # 没有训练和加载过模型
        if not self.trained:
            raise RuntimeError('There is no trained model.')

        # print("samples:{}".format(samples))
        samples = self.reshape_input(samples)

        # 最大值概率
        prod = max(self.model.predict(samples)[0])


        prodList = list(self.model.predict(samples)[0])
        print("sortedPred:{}".format(prodList))

        newPred = []
        for i in range(len(prodList)):
            newPred.append(prodList[i])
        newPred.sort()  # 默认逆序

        maxClassLabelIndex = prodList.index(newPred[-1])
        secClassLabelIndex = prodList.index(newPred[-2])

        # 返回最大值概率下标，次大值概率下标，最大值概率，次大值概率
        return maxClassLabelIndex, secClassLabelIndex, prodList[maxClassLabelIndex] , prodList[secClassLabelIndex]



