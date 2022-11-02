from cgi import print_form
import re
from matplotlib.ft2font import KERNING_DEFAULT
from matplotlib.pyplot import axis
from tqdm import tgrange
from tensorflow.keras.layers import Convolution2D,MaxPooling2D,Convolution1D,TimeDistributed,MaxPooling1D,BatchNormalization,Multiply
from tensorflow.keras.layers import LSTM as KERAS_LSTM
from tensorflow.python.keras.layers.recurrent import GRU
from tensorflow.keras.layers import add, Activation, Dense, Dropout, Flatten, Input, Permute, Reshape
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD, RMSprop
# from keras.optimizers import adam_v2
from tensorflow.keras.regularizers import l1_l2
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
import numpy as np
from .dnn import DNN
from tensorflow.keras.layers import Bidirectional
from tensorflow_addons.optimizers import AdamW
from tensorflow import keras
import tensorflow as tf
# tf.random.set_seed(10)
from tensorflow.keras.models import Model
from utils import curve
import os
import time
from tensorflow.python.keras.utils import np_utils
from sklearn.metrics import accuracy_score
from abc import ABC, abstractmethod
from typing import Union
import numpy as np
from tensorflow.keras.models import Sequential
from sklearn.metrics import accuracy_score
from sklearn.base import BaseEstimator
from tensorflow.keras import backend as K
import random


# # Seed value
# # Apparently you may use different seed values at each stage
# seed_value= 42

# # 1. Set `PYTHONHASHSEED` environment variable at a fixed value
# import os
# os.environ['PYTHONHASHSEED']=str(seed_value)

# # 2. Set `python` built-in pseudo-random generator at a fixed value
# import random
# random.seed(seed_value)

# # 3. Set `numpy` pseudo-random generator at a fixed value
# import numpy as np
# np.random.seed(seed_value)

# # 4. Set `tensorflow` pseudo-random generator at a fixed value
# import tensorflow as tf
# tf.random.set_seed(seed_value)

# # 5. Configure a new global `tensorflow` session
# # from tensorflow.keras import backend as K
# from tensorflow.compat.v1.keras import backend as K
# session_conf = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
# sess = tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph(), config=session_conf)
# K.set_session(sess)


def setup_seed(seed):
    print('enter setup seed')
    random.seed(seed)  # 为python设置随机种子
    np.random.seed(seed)  # 为numpy设置随机种子
    tf.random.set_seed(seed)  # tf cpu fix seed
    os.environ['TF_DETERMINISTIC_OPS'] = '1'  # tf gpu fix seed, please `pip install tensorflow-determinism` first


setup_seed(42)



def set_tf_device(device):
    print('enter set tf device')
    if device == 'cpu':
        print("Training on CPU...")
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    elif device == 'gpu':
        # os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = '0' #use multi-GPU
        print("Training on GPU...")
        for gpu in tf.config.experimental.list_physical_devices("GPU"):
            tf.config.experimental.set_memory_growth(gpu, True)


set_tf_device('gpu')


def lr_schedule(epoch):
    lr = 0.01
    if epoch >= 200:
        lr *= 0.001
    elif epoch >= 500:
        lr *= 0.0001
    print('Learning rate: ', lr)
    return lr

def wd_schedule(epoch):
    wd = 0.01
    if epoch >= 200:
        wd *= 0.001
    elif epoch >= 500:
        wd *= 0.0015
    print('Weight decay: ', wd)
    return wd



#残差块
def ResBlock(x,hidden_size1,hidden_size2):
    r=Dense(hidden_size1,activation='relu')(x)  #第一隐层
    r=Dense(hidden_size2)(r)  #第二隐层
    if x.shape[1]==hidden_size2:
        shortcut=x
    else:
        shortcut=Dense(hidden_size2)(x)  #shortcut（捷径）
    o=add([r,shortcut])
    o=Activation('relu')(o)  #激活函数
    return o


def reshape_input(data: np.ndarray) -> np.ndarray:
    """
    二维数组转三维
    (n_samples, n_feats) -> (n_samples, time_steps = 1, input_size = n_feats)
    time_steps * input_size = n_feats 
    """
    data = np.reshape(data, (data.shape[0], 1, data.shape[1])) 

    return data

class LSTM(DNN):
    def __init__(self, model: Sequential, trained: bool = False) -> None:
        super(LSTM, self).__init__(model, trained)
        
    @classmethod
    def make(cls,
    checkpoint_path, checkpoint_name,
    x_train, x_test, y_train, y_test, 
    input_shape, epochs ,rnn_size: int,hidden_size: int,dropout: float = 0.5,n_classes: int = 5,
    # lr: float = 0.001
    ):
        """
        搭建模型

        Args:
            cls:<class 'models.dnn.lstm.LSTM'>
            input_shape (int)=312: 特征维度
            rnn_size (int)=128:   LSTM 隐藏层大小
            hidden_size (int)=32: 全连接层大小
            dropout (float, optional, default=0.5): dropout
            n_classes (int, optional, default=6): 标签种类数量
            lr (float, optional, default=0.001): 学习率
        """

        print('----- start training -----')
        

        y_train = np_utils.to_categorical(y_train)
        y_val = np_utils.to_categorical(y_test) 
        x_train, x_test = reshape_input(data=x_train), reshape_input(data=x_test)

        

        # 搭建网络
        input_layer = tf.keras.Input(shape=(1,312,))  # input_layer:(None, 1, 312)
        print("input_layer:{}".format(input_layer.shape))
        conv1 = Convolution1D(filters = 64, kernel_size = (2,), activation = 'relu', padding='same')(input_layer)
        # conv2 = Convolution1D(filters = 128, kernel_size = (1,), activation = 'relu', padding='same')(conv1)
        # x = Convolution2D(filters = 64, kernel_size = (1,1,), activation = 'relu', padding='same')(input_layer)
        # x = Reshape((1,64,))(x)
        biLSTM = Bidirectional(KERAS_LSTM(rnn_size, input_shape=(1, input_shape,), return_sequences=True, kernel_regularizer=keras.regularizers.l1(0.001)))(conv1)
        biGRU = Bidirectional(GRU(256, input_shape=(1, rnn_size), kernel_regularizer=keras.regularizers.l1(0.001)))(biLSTM)
        # attention_emb = attention(512,biGRU,'attention_emb')
        dense1 = Dense(hidden_size, activation='sigmoid')(biGRU)
        res1 = ResBlock(dense1, 16,16)
        bn = BatchNormalization()(res1)
        bn = Reshape((1,16))(bn)
        maxpool = MaxPooling1D(pool_size=2, strides=2, padding='same')(bn)
        dropout1 = Dropout(dropout)(maxpool)
        flatten1 = Flatten()(dropout1)
        output = Dense(n_classes, activation='softmax')(flatten1)
        # 传入数据
        model = Model(inputs=input_layer, outputs=output)
        model.summary()
        adamW = AdamW(learning_rate=lr_schedule(epochs), weight_decay=wd_schedule(epochs))
        model.compile(loss='categorical_crossentropy', optimizer=adamW, metrics=['accuracy'])
        return cls(model)


    def reshape_input(self, data: np.ndarray) -> np.ndarray:
        # print("data1:{}".format(data.shape))  # shape:(1,312)
        """二维数组转三维"""
        # (n_samples, n_feats) -> (n_samples, time_steps = 1, input_size = n_feats)
        # time_steps * input_size = n_feats
        data = np.reshape(data, (data.shape[0], 1, data.shape[1]))  # shape: (1,1,312)
        return data
