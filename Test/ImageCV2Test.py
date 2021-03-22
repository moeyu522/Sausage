# -*- coding: utf-8 -*-
# @File    : ImageCV2Test.py
# @Time    : 2020/3/24 17:57
# @Author  : Moeyu522 Lee
# @Describe: OpenCV的测试，哎，最难写的一个类，发呆半天，代码两三行

# 相关实验目录：
# Test_0    测试divideImage函数，将读取的图像一分为三
# Test_1    测试静态方法locatingObjectsFromSingleImage对图像的正确定位
# Test_2    测试本项目中HSV的提取结果

from Image_CV2 import *
import cv2 as cv
from Image_UTIL import *

# Test_0
# 测试divideImage函数，将读取的图像一分为三
# cv.namedWindow('re1', flags=cv.WINDOW_NORMAL)
# cv.namedWindow('re2', flags=cv.WINDOW_NORMAL)
# cv.namedWindow('re3', flags=cv.WINDOW_NORMAL)
# image = cv.imread('passagewayTest.png')
#
# image_cv = ImageCV2(image_ndarray=image, need_to_del_from_last_time=None, passageway_number=3)
# passageway_list = image_cv.divideImage()
#
# cv.imshow('re1', passageway_list[0])
# cv.imshow('re2', passageway_list[1])
# cv.imshow('re3', passageway_list[2])
# cv.waitKey(0)

# Test_1
# 测试静态方法locatingObjectsFromSingleImage对图像的正确定位
# 该测试获取图像的香肠的剪切后的图像并展示，并对处于有效区域内的香肠加绿色框
# image = cv.imread('passagewayTest.png')
# cv.namedWindow('re1', flags=cv.WINDOW_NORMAL)
# cv.namedWindow('re2', flags=cv.WINDOW_NORMAL)
# (cut, top, bottom, outline) = Util.locatingObjectsFromSingleImage(image_ndarray=image)
#
# (outline_effective, outline_invalid) = outline
# (cut_effective, _) = cut
#
# for i in range(len(outline_effective)):
#     x, y, w, h = cv.boundingRect(outline_effective[i])
#     cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# for i in range(len(outline_invalid)):
#     x, y, w, h = cv.boundingRect(outline_invalid[i])
#     cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
# cv.imshow('re1', image)
# cv.imshow('re2', cut_effective[1])
# cv.waitKey(0)

# Test_2
# 测试本项目中HSV的提取结果
# import numpy as np
# import os
#
# image_root = "D:/code/pycharm/image/pic/4"
# cv.namedWindow('re', flags=cv.WINDOW_NORMAL)
# cv.namedWindow('re2', flags=cv.WINDOW_NORMAL)
# cv.namedWindow('re3', flags=cv.WINDOW_NORMAL)
# cv.namedWindow('re4', flags=cv.WINDOW_NORMAL)
#
# for _index, fname in enumerate(os.listdir(image_root)):
#     print("当前文件：", image_root + "/" + fname)
#     I = cv.imread(image_root + "/" + fname)
#     hsv_image = cv.cvtColor(I, cv.COLOR_BGR2HSV)
#     cv.imshow("re", I)
#     # 香肠的hsv定义
#     red_low = np.array([1, 60, 20])
#     red_high = np.array([15, 200, 255])
#     # 阈值HSV图像仅获得红色
#     img = cv.inRange(hsv_image, red_low, red_high)
#     cv.imshow("re2", img)
#
#     def onMouse(event, x, y, flags, param):
#         # 显示HSV值
#         if event == cv.EVENT_MOUSEMOVE:
#             print("x=={}\ty=={}\t值：{}".format(x, y, hsv_image[y, x]))
#             print("\n")
#
#
#     kernel = cv.getStructuringElement(shape=cv.MORPH_CROSS, ksize=(5, 5))
#     kernel2 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(5, 5))
#     # 闭运算
#     img_temp = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
#     # 开运算
#     img_temp = cv.morphologyEx(img_temp, cv.MORPH_OPEN, kernel)
#     # 腐蚀3次，膨胀5次
#     img_temp = cv.erode(img_temp, kernel2, iterations=3)
#     img_temp = cv.dilate(img_temp, kernel2, iterations=5)
#     # cv.imshow("re3", img_temp)
#     # 找到轮廓
#     img = cv.inRange(img_temp, 254, 255)
#     outline, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     cv.imshow("re3", img_temp)
#     print(len(outline))
#     for cnt in outline:
#         rect = cv.minAreaRect(cnt)
#         box = cv.boxPoints(rect)
#         box1 = np.int64(np.around(box))
#         im2 = cv.drawContours(I, [box1], 0, (0, 255, 0), 2)
#
#         temp = np.ones((I.shape[0], I.shape[1], 3), np.uint8) * 255
#         cv.fillPoly(temp, pts=[cnt], color=(0, 0, 0))
#         i = cv.bitwise_or(temp, I)
#         cv.imshow("re4", i)
#
#     cv.setMouseCallback("re", onMouse)
#
#     cv.waitKey(0)
