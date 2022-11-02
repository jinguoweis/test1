import os
from typing import Optional
from abc import ABC, abstractmethod
import numpy as np
from keras.models import Sequential, model_from_json
from ..base import BaseModel
from utils import curve

class DNN(BaseModel, ABC):
    """
    所有基于 Keras 的深度学习模型的基类

    Args:
        n_classes (int): 标签种类数量
        lr (float): 学习率
    """
    def __init__(self, model: Sequential, trained: bool = False) -> None:
        super(DNN, self).__init__(model, trained)
        print(self.model.summary())

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
        if x_val is None or y_val is None:
            x_val, y_val = x_train, y_train

        x_train, x_val = self.reshape_input(x_train), self.reshape_input(x_val)
        # LSTM 模型通过调用 fit() 函数进行训练,返回一个叫作 history 的变量
        # 该变量包含损失函数的轨迹，以及在模型编译过程中被标记出来的任何一个度量指标。这些得分会在每一个 epoch 的最后被记录下来。
        history = self.model.fit(
            x_train, y_train,
            batch_size = batch_size,
            epochs = n_epochs,
            shuffle = True, # 每个 epoch 开始前随机排列训练数据
            validation_data = (x_val, y_val)
        )

        # print("history:{}".format(history.history))


        # 绘图
        # 训练集上的损失和准确率
        acc = history.history['accuracy']
        loss = history.history['loss']
        # 验证集上的损失和准确率
        val_acc = history.history['val_accuracy']
        val_loss = history.history['val_loss']

        curve(acc, val_acc, 'Accuracy', 'acc')  # 绘制损失值和准确率曲线
        curve(loss, val_loss, 'Loss', 'loss')

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

        print("samples:{}".format(samples))
        samples = self.reshape_input(samples)
        print("self.model.predict(samples):{}".format(self.model.predict(samples)))
        return np.argmax(self.model.predict(samples), axis=1)

    # @abstractmethod
    # def reshape_input(self):
    #     pass
