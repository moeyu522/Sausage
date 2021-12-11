# -*- coding: utf-8 -*-
# @File    : ImageCNNModel.py
# @Time    : 2020/3/23 17:32
# @Author  : Moeyu522 Lee
# @Describe: 生成一个默认10层的CNN网络并指定一些常用的函数参数

import tensorflow.keras as keras
import tensorflow.keras.layers as layers
import numpy as np
from PIL import Image
import cv2 as cv


class ImageCNNModel:
    def __init__(self, image_w=256, image_h=256):
        self.__model__ = keras.Sequential()

        self.__model__.add(layers.Conv2D(filters=16, kernel_size=(7, 7), strides=(2, 2),
                                         padding='same', activation='relu',
                                         name='conv_1', input_shape=(image_w, image_h, 3)))

        self.__model__.add(layers.Conv2D(filters=16, kernel_size=(2, 2),
                                         strides=(2, 2), activation='relu', name='pool_1'))

        self.__model__.add(layers.Conv2D(filters=32, kernel_size=(5, 5),
                                         strides=(2, 2), padding='same', activation='relu', name='conv_2'))

        self.__model__.add(layers.Conv2D(filters=32, kernel_size=(2, 2),
                                         strides=(2, 2), activation='relu', name='pool_2'))

        self.__model__.add(layers.Conv2D(filters=64, kernel_size=(3, 3),
                                         strides=(1, 1), padding='same', activation='relu', name='conv_3'))

        self.__model__.add(layers.Conv2D(filters=64, kernel_size=(3, 3),
                                         strides=(1, 1), padding='same', activation='relu', name='conv_4'))

        self.__model__.add(layers.Conv2D(filters=64, kernel_size=(3, 3),
                                         strides=(1, 1), padding='same', activation='relu', name='conv_5'))

        self.__model__.add(layers.Conv2D(filters=64, kernel_size=(2, 2),
                                         strides=(2, 2), activation='relu', name='pool_3'))

        self.__model__.add(layers.Flatten())

        self.__model__.add(layers.Dense(units=2048, activation='relu', name='dense_1'))

        self.__model__.add(layers.Dropout(rate=0.5))

        self.__model__.add(layers.Dense(units=512, activation='relu', name='dense_2'))

        self.__model__.add(layers.Dropout(rate=0.25))

        self.__model__.add(layers.Dense(units=4, activation='softmax', name='softmax'))

    def compile(self, optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy'):
        self.__model__.compile(optimizer=optimizer,
                               loss=loss,
                               metrics=[metrics])

    def summary(self):
        self.__model__.summary()

    def save(self, filepath='Image_data/ImageMode.h5'):
        self.__model__.save(filepath=filepath)
        print("保存成功！")

    def fit(self, train_image, train_label, batch_size=32, epochs=10):
        self.__model__.fit(x=train_image, y=train_label, batch_size=batch_size, epochs=epochs)

    def evaluate(self, test_image, test_label, batch_size=32, verbose=1):
        self.__model__.evaluate(x=test_image, y=test_label, batch_size=batch_size, verbose=verbose)

    def loadModelFromFile(self, model_path='Image_data/ImageMode.h5'):
        # 从文件载入已经训练好的模型数据
        # 模型数据只载入一次，方便以后用于识别
        self.__model__ = keras.models.load_model(model_path)

    def PredictFromImageNdarray(self, image_ndarray, print_result=False):
        # 用于预测单个图像分类
        # image_ndarray: 图像的ndarray数组
        # print_result: 是否打印每个结果数据，默认不打印
        im = cv.cvtColor(image_ndarray, cv.COLOR_BGR2RGB)
        im = np.expand_dims(im, axis=0)
        pre = self.__model__.predict(im)
        reindex = np.argmax(pre)
        if print_result is False:
            return reindex
        else:
            print("*************")
            print("是过长的概率：{:5.2f}%".format(pre[0][0] * 100))
            print("是破损的概率：{:5.2f}%".format(pre[0][1] * 100))
            print("是正常的概率：{:5.2f}%".format(pre[0][2] * 100))
            print("是过短的概率：{:5.2f}%".format(pre[0][3] * 100))
            print("*************")
            return reindex

    @staticmethod
    def loadModelAndEvaluate(test_image, test_label, batch_size=32, verbose=1, filepath='Image_data/ImageMode.h5'):
        model = keras.models.load_model(filepath)
        model.evaluate(x=test_image, y=test_label, batch_size=batch_size, verbose=verbose)

    @staticmethod
    def loadModelAndPredictFromFile(image_path, print_result=False, model_path='Image_data/ImageMode.h5'):
        # image_path: 图像路径
        # print_result: 是否打印每个结果数据，默认不打印
        # model：用于预测的模型的位置
        im = Image.open(image_path)
        im = np.array(im)
        im = np.expand_dims(im, axis=0)
        model = keras.models.load_model(model_path)
        pre = model.predict(im)
        reindex = np.argmax(pre)
        if print_result is False:
            return reindex
        else:
            print("*************")
            print("是过长的概率：{:5.2f}%".format(pre[0][0] * 100))
            print("是破损的概率：{:5.2f}%".format(pre[0][1] * 100))
            print("是正常的概率：{:5.2f}%".format(pre[0][2] * 100))
            print("是过短的概率：{:5.2f}%".format(pre[0][3] * 100))
            print("*************")
            return reindex
