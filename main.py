# -*- coding: utf-8 -*-


import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import tensorflow as tf
import selectFunc as selectFunc
import os



with tf.device('/cpu:0'):
    flagAiJudge = os.path.exists(r'.\aiJudge')
    if(flagAiJudge==False):
        os.makedirs(r'.\aiJudge')

    # 函数调用
    selectFunc.selectFunc()
