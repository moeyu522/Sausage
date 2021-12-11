# -*- coding: utf-8 -*-
# @File    : ImageDataGetTest.py
# @Time    : 2020/3/23 23:21
# @Author  : Moeyu522 Lee
# @Describe: 用于前期CNN网络的数据准备，包括图像处理，ndarray数组的制作保存

from Image_data.ImageData import *


# Test_0
# 已经有npy图像数据 载入图像数据
# ((train_image, train_label), (test_image, test_label)) = ImageData().getImageData()

# Test_1
# 制作npy图像数据并保存
# 原始图像数据存放在"Sausage/Image_data/"下，分类标签即文件目录名
# 共有toolong、toosmall、damage、normal四种
# image_data = ImageData.createNewDataAndSave()

# Test_2
# 制作超过1万张的图像
# def connectData(image_data_a, image_data_b):
#     ((train_image, train_label), (test_image, test_label)) = image_data_a
#
#     ((train_image_1, train_label_1), (test_image_1, test_label_1)) = image_data_b
#
#     image_train = np.concatenate((train_image, train_image_1))
#
#     image_label_train = np.concatenate((train_label, train_label_1))
#
#     image_test = np.concatenate((test_image, test_image_1))
#
#     image_label_test = np.concatenate((test_label, test_label_1))
#
#     image_data = ((image_train, image_label_train), (image_test, image_label_test))
#
#     # np.save('Image_data/imageData.npy', arr=data)
#
#     return image_data
#
#
# image_data_1 = ImageData.createNewDataAndSave(isSave=False)
# image_data_2 = ImageData.createNewDataAndSave(isSave=False)
# image_data_temp_1 = connectData(image_data_1, image_data_2)
# del image_data_1
# del image_data_2
# image_data_3 = ImageData.createNewDataAndSave(isSave=False)
# image_data_4 = ImageData.createNewDataAndSave(isSave=False)
# image_data_temp_2 = connectData(image_data_3, image_data_4)
# del image_data_3
# del image_data_4
#
# image_data_temp = connectData(image_data_temp_1, image_data_temp_1)
#
# np.save("../Image_data/ImageData.npy", image_data_temp)
# print("ok")
