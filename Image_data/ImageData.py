# -*- coding: utf-8 -*-
# @File    : ImageData.py
# @Time    : 2020/3/23 20:45
# @Author  : Moeyu522 Lee
# @Describe: 制作用于CNN网络训练的数据并保存为npy格式
# 图像标签说明：
# 过长：0
# 破损：1
# 正常：2
# 过短：3

import numpy as np
import os
import Image_UTIL


class ImageData:
    def __init__(self, file_dir=os.path.dirname(__file__)):
        if os.path.isfile(file_dir + '\\imageData.npy'):
            self.__imageData__ = np.load(file=file_dir + '\\imageData.npy', allow_pickle=True)
        else:
            print("图像ndarray数据不存在，请先调用ImageData的静态createNewDataAndSave方法并在实例化后调用loadNewData方法")

    def loadNewData(self, file_dir=os.path.dirname(__file__)):
        if os.path.isfile(file_dir + '\\imageData.npy'):
            self.__imageData__ = np.load(file=file_dir + '\\imageData.npy', allow_pickle=True)
        else:
            print("图像ndarray数据不存在，请先调用ImageData的静态createNewDataAndSave方法并在实例化后调用loadNewData方法")

    def getImageData(self):
        return self.__imageData__

    @staticmethod
    def createNewDataAndSave(file_dir=os.path.dirname(__file__), isSave=True):
        # file_dir：训练数据存放的目录，默认为当前文件的同级
        # 描述：读取图像并将图像转换成ndarray格式存放在元组里
        # 元组元素描述：(train_image, train_label, test_image, test_label)
        # 图像将通过反转，亮度调节方式增加原数据规模

        train_image = []
        train_label = []
        test_image = []
        test_label = []

        toolong_image = []
        toolong_label = []

        damage_image = []
        damage_label = []

        normal_image = []
        normal_label = []

        toosmall_image = []
        toosmall_label = []

        # 标签为整形且以0开始
        for fname in os.listdir(file_dir + "\\toolong"):
            fpath = file_dir + "\\toolong\\" + fname
            image_list, label_list = Image_UTIL.Util.dealWith(fpath, 0)
            toolong_image.extend(image_list)
            toolong_label.extend(label_list)

        for fname in os.listdir(file_dir + "\\damage"):
            fpath = file_dir + "\\damage\\" + fname
            image_list, label_list = Image_UTIL.Util.dealWith(fpath, 1)
            damage_image.extend(image_list)
            damage_label.extend(label_list)

        for fname in os.listdir(file_dir + "\\normal"):
            fpath = file_dir + "\\normal\\" + fname
            image_list, label_list = Image_UTIL.Util.dealWith(fpath, 2)
            normal_image.extend(image_list)
            normal_label.extend(label_list)

        for fname in os.listdir(file_dir + "\\toosmall"):
            fpath = file_dir + "\\toosmall\\" + fname
            image_list, label_list = Image_UTIL.Util.dealWith(fpath, 3)
            toosmall_image.extend(image_list)
            toosmall_label.extend(label_list)

        # 0.95作为训练集 0.05为测试集
        train_image.extend(toolong_image[0:int(len(toolong_image) * 0.95)])
        train_image.extend(damage_image[0:int(len(damage_image) * 0.95)])
        train_image.extend(normal_image[0:int(len(normal_image) * 0.95)])
        train_image.extend(toosmall_image[0:int(len(toosmall_image) * 0.95)])

        train_label.extend(toolong_label[0:int(len(toolong_label) * 0.95)])
        train_label.extend(damage_label[0:int(len(damage_label) * 0.95)])
        train_label.extend(normal_label[0:int(len(normal_label) * 0.95)])
        train_label.extend(toosmall_label[0:int(len(toosmall_label) * 0.95)])

        test_image.extend(toolong_image[int(len(toolong_image) * 0.95):])
        test_image.extend(damage_image[int(len(damage_image) * 0.95):])
        test_image.extend(normal_image[int(len(normal_image) * 0.95):])
        test_image.extend(toosmall_image[int(len(toosmall_image) * 0.95):])

        test_label.extend(toolong_label[int(len(toolong_label) * 0.95):])
        test_label.extend(damage_label[int(len(damage_label) * 0.95):])
        test_label.extend(normal_label[int(len(normal_label) * 0.95):])
        test_label.extend(toosmall_label[int(len(toosmall_label) * 0.95):])

        # 打乱训练集和测试集
        train = Image_UTIL.Util.disOrder(train_image, train_label)
        test = Image_UTIL.Util.disOrder(test_image, test_label)

        # 保存元组train 、test
        save_data = (train, test)
        if isSave is True:
            np.save(file=file_dir+'\\imageData.npy', arr=save_data)
            print("保存成功！")
            print("保存位置: {}".format(file_dir+"\\imageData.npy"))
        return save_data
