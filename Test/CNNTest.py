# -*- coding: utf-8 -*-
# @File    : CNNTest.py
# @Time    : 2020/3/23 17:34
# @Author  : Moeyu522 Lee
# @Describe: CNN测试 包括CNN的训练，模型保存，模型评价，单个图像分类测试

import Image_CNN
from Image_data.ImageData import *
import numpy as np
import os

# Test_0
# 查看网络结构
# model = Image_CNN.ImageCNNModel()
# model.summary()

# Test_1
# 载入图像数据，训练CNN网络，保存CNN网络模型
# ((train_image, train_label), (test_image, test_label)) = ImageData().getImageData()
#
# model = Image_CNN.ImageCNNModel(image_w=128, image_h=128)
# model.compile()
# model.fit(train_image=train_image, train_label=train_label)
# model.evaluate(test_image=test_image, test_label=test_label)
# model.save()

# Test_2
# 载入图像数据，加载已有模型并完成模型评估
# ((train_image, train_label), (test_image, test_label)) = ImageData().getImageData()
# Image_CNN.ImageCNNModel.loadModelAndEvaluate(test_image=test_image, test_label=test_label, batch_size=64)

# Test_3
# 加载已有模型，单个图像分类测试
# path = ' '
# Image_CNN.ImageCNNModel.loadModelAndPredictFromFile(image_path=path,
#                                                     print_result=True,
#                                                     model_path="../Image_data/ImageMode.h5")
