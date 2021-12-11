# -*- coding: utf-8 -*-
# @File    : tempTest.py
# @Time    : 2020/3/24 2:19
# @Author  : Moeyu522 Lee
# @Describe: 临时测试：杂乱无章版本

# 相关实验目录：
# Test_0    测试获取系统时间
# Test_1    图像拼接测试
# Test_2    用鼠标动态的显示一张图像的HSV数值
# Test_3    重命名文件。统一为24位深RGB，png格式
# Test_4    缩放图像大小
# Test_5    论文中5.1.1实验 画出HSV分布图
# Test_6    论文中5.1.1实验 根据粒粒肠的颜色特征提取粒粒肠轮廓
# Test_7    论文中5.1.2实验 得到20个粒粒肠的长度\面积\直径
# Test_8    获取100张过短粒粒肠的长度、面积、直径特征 并统计成折线图
# Test_9    展示图像增强技术的处理结果
# Test_10   论文中第5章一般灰度图像处理
# Test_11   测试模型对图象的正确率并画出统计图

# Test_0
# 测试获取系统时间
# 原始图像命名规则：(年-月-日)+'_'+(hh:mm:ss)+'_'+系统开机到目前位置所拍照的序号
# import datetime
# now_time = datetime.datetime.now().strftime('%F_%T_')
# print(now_time)

# Test_1
# 图像拼接测试
# import numpy as np
# import cv2 as cv
#
# cv.namedWindow('re', flags=cv.WINDOW_NORMAL)
# img1 = cv.imread("passagewayTest.png")
# img2 = img1
#
# img3 = np.hstack([img1, img2])
#
# cv.imshow("re", img3)
# cv.waitKey(0)

# Test_2
# 用鼠标动态的显示一张图像的HSV数值
# import cv2 as cv
# import matplotlib.pyplot as plt
# import numpy as np
#
# image = cv.imread("D:/code/pycharm/CNN/Image_data/image/train/1/1.png")
# cv.namedWindow('re', flags=cv.WINDOW_NORMAL)
# hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
#
#
# def onMouse(event, x, y, flags, param):
#     if event == cv.EVENT_MOUSEMOVE:
#         print("x=={}\ty=={}\tHSV：{}".format(x, y, hsv[y, x]))
#         print("\n")
#
#
# def goto():
#     x = hsv[:, :, 0].flatten()
#     y = np.bincount(x)
#     t = range(1, y.shape[0]-1, 1)
#     plt.plot(t, y[1:y.shape[0]-1]/100)
#     # plt.locator_params('x', nbins=90)
#     plt.show()
#
#
# cv.setMouseCallback("re", onMouse)
#
# while True:  # 无限循环
#     cv.imshow("re", image)  # 显示图像
#     if cv.waitKey() == ord('q'):
#         break  # 按下‘q’键，退出
#     if cv.waitKey() == ord('g'):
#         # 画直方图
#         goto()
# cv.destroyAllWindows()

# Test_3
# 重命名文件。统一为24位深RGB，png格式
# import cv2 as cv
# import os
#
#
# image_root = "Image_data/verification_2"
# pre = "3"
# n = 1
#
# for fname in os.listdir(image_root):
#     im = cv.imread(image_root+"/"+fname)
#     im = cv.cvtColor(im, cv.COLOR_BGRA2BGR)
#     # 删除原文件
#     os.remove(image_root+"/"+fname)
#     cv.imwrite(image_root+"/"+pre+"_"+str(n)+".png", im)
#     n = n+1

# Test_4
# 缩放图像大小
# import cv2 as cv
# import os
#
#
# image_root = "Image_data/verification"
#
#
# for fname in os.listdir(image_root):
#     im = cv.imread(image_root+"/"+fname)
#     new_image = cv.resize(im, (256, 256), interpolation=cv.INTER_AREA)
#     cv.imwrite(image_root+"/"+fname, new_image)

# Test_5
# 论文中5.1.1实验 画出HSV分布图
# import matplotlib.pyplot as plt
# import cv2 as cv
# import numpy as np
# import os
#
# H = 0
# S = 1
# V = 2
#
#
# def get(f_path, index):
#     image = cv.imread(f_path)
#     hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
#
#     x_temp = hsv[:, :, index].flatten()
#
#     return x_temp
#
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# path = "D:/code/pycharm/CNN/Image_data/image/train/2"
# x = np.array([], dtype=np.uint8)
# for fname in os.listdir(path):
#     fpath = path + fname
#     # 得到单个的HSV中的某一项
#     temp = get(path+"/"+fname, V)
#     x = np.append(x, temp)
#
# y = np.bincount(x)
# t = range(1, y.shape[0], 1)
# plt.plot(t, y[1:y.shape[0]] / 10)
# plt.locator_params('x', nbins=25)
# plt.title("S分布")
# plt.xlabel("S值")
# plt.ylabel("出现次数/10")
# plt.show()
# print("ok")


# Test_6
# 论文中5.1.1实验 根据粒粒肠的颜色特征提取粒粒肠轮廓
# import os
# import numpy as np
#
#
# image_root = "../Image_data/verification_1"
#
# for _index, fname in enumerate(os.listdir(image_root)):
#     print("当前文件：", image_root+"/"+fname)
#     im = cv.imread(image_root+"/"+fname)
#     hsv_image = cv.cvtColor(im, cv.COLOR_BGR2HSV)
#     red_low = np.array([1, 60, 20])
#     red_high = np.array([15, 200, 255])
#     # 阈值HSV图像仅获得红色
#     img = cv.inRange(hsv_image, red_low, red_high)
#     cv.imshow("img", img)
#     cv.waitKey(0)


# Test_7
# 论文中5.1.2实验 得到20个粒粒肠的长度\面积\信息
# import os
# import numpy as np
# import cv2 as cv
# import math
#
# image_root = "../Image_data/verification_2"
#
# for _index, fname in enumerate(os.listdir(image_root)):
#     print("当前文件：", image_root + "/" + fname)
#     im = cv.imread(image_root + "/" + fname)
#     hsv_image = cv.cvtColor(im, cv.COLOR_BGR2HSV)
#     red_low = np.array([1, 60, 20])
#     red_high = np.array([15, 200, 255])
#     # 阈值HSV图像仅获得红色
#     img = cv.inRange(hsv_image, red_low, red_high)
#     kernel = cv.getStructuringElement(shape=cv.MORPH_CROSS, ksize=(5, 5))
#     kernel2 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(5, 5))
#     # 闭运算
#     img_temp = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
#     # 开运算
#     img_temp = cv.morphologyEx(img_temp, cv.MORPH_OPEN, kernel)
#     # 腐蚀3次，膨胀5次
#     img_temp = cv.erode(img_temp, kernel2, iterations=3)
#     img_temp = cv.dilate(img_temp, kernel2, iterations=5)
#     # 找到轮廓
#     outline, hierarchy = cv.findContours(img_temp, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#
#     for cnt in outline:
#         rect = cv.minAreaRect(cnt)
#         box = cv.boxPoints(rect)
#         box1 = np.int64(np.around(box))
#         im = cv.drawContours(im, [box1], 0, (0, 255, 0), 2)
#         p1, p2, p3, _ = box1
#         # print("p1=={}\tp2=={}\tp3=={}".format(p1, p2, p3))
#         area = cv.contourArea(cnt)
#         L = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
#         C = math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
#         print("长度\t{}\t面积\t{}\t直径{}".format(round(L), area, round(C)))
#
#     # print("")
#     # cv.imshow("img", img_temp)
#     # cv.waitKey(0)

# Test_8
# 获取100张过短粒粒肠的长度、面积、直径特征 并统计成折线图
# import cv2 as cv
# import os
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# filename = ["normal"]
# # 统计值
# length_list = []
# area_list = []
# diameter_list = []
#
#
# def onMouse(event, x, y, flags, param):
#     if event == cv.EVENT_MOUSEMOVE:
#         print("x=={}\ty=={}\t".format(x, y))
#         print("\n")
#
#
# # cv.namedWindow('re', flags=cv.WINDOW_NORMAL)
# # cv.setMouseCallback("re", onMouse)
# for name in filename:
#     image_root = "../Image_data/" + name
#     for _index, fname in enumerate(os.listdir(image_root)):
#         im = cv.imread(image_root + "/" + fname)
#         print("当前文件：", image_root + "/" + fname)
#         # im = cv.imread("../Image_data/damage/1_79.png")
#         im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#         img = cv.inRange(im_gray, 30, 100)
#         clahe = cv.createCLAHE(clipLimit=2.0,
#                                tileGridSize=(8, 8))
#
#         # 第二步：进行自适应直方图均衡化
#         cll = clahe.apply(img)
#         kernel = cv.getStructuringElement(shape=cv.MORPH_CROSS, ksize=(5, 5))
#         kernel2 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(5, 5))
#         # 闭运算
#         img_temp = cv.morphologyEx(cll, cv.MORPH_CLOSE, kernel)
#         # 开运算
#         img_temp = cv.morphologyEx(img_temp, cv.MORPH_OPEN, kernel)
#         # 腐蚀3次，膨胀5次
#         img_temp = cv.erode(img_temp, kernel2, iterations=3)
#         img_temp = cv.dilate(img_temp, kernel2, iterations=5)
#         # 让图像只有0和255
#         img_temp = cv.inRange(img_temp, 254, 255)
#         # 找到轮廓
#         outline, hierarchy = cv.findContours(img_temp, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#
#         for cnt in outline:
#             print("outline=={}".format(len(outline)))
#             rect = cv.minAreaRect(cnt)
#             box = cv.boxPoints(rect)
#             box1 = np.int64(np.around(box))
#             im = cv.drawContours(im, [box1], 0, (0, 255, 0), 2)
#             area = cv.contourArea(cnt)
#             p0, p1, p2, p3 = box1
#             print("p0=={}\tp3=={}".format(p0, p3))
#             print("p1=={}\tp2=={}".format(p1, p2))
#             print("中心=={}".format(rect[0]))
#             D = round(rect[1][0])
#             L = round(rect[1][1])
#             if D > L:
#                 D, L = L, D
#             print("角度:", rect[2])
#             print("长度:{}\t面积:{}\t直径:{}\n".format(round(L), area, round(D)))
#             length_list.append(L)
#             area_list.append(area)
#             diameter_list.append(D)
#
#         # print("")
#         # cv.imshow("re", im)
#         # cv.waitKey(0)
#
# # 画统计图
# # 可以更改plot函数的参数来画不同的图
# # length_list 长度
# # area_list 面积
# # diameter_list 直径
# y = np.bincount(area_list)
# # x_min  X轴的最小值，和值的显示范围有关
# x_min = 2250
# t = range(x_min, y.shape[0], 1)
# plt.plot(t, y[x_min:y.shape[0]])
# # plt.locator_params('x', nbins=500)
# plt.title("面积统计")
# plt.xlabel("面积(Pixel)")
# plt.ylabel("出现次数")
# plt.show()

# Test_9
# 展示图像增强技术的处理结果
# 一共7种
# import cv2 as cv
# from PIL import Image
# import numpy as np
# cv.namedWindow('re', flags=cv.WINDOW_NORMAL)
#
#
# # 原图像
# image = Image.open("../Image_data/verification_2/1_3.png")
# image_np = np.array(image)
# image_np = cv.cvtColor(image_np, cv.COLOR_RGB2BGR)
# # cv.imshow("re", image_np)
#
# # 处理1上下反转
# im_2 = image.transpose(Image.FLIP_TOP_BOTTOM)
# im_2_np = np.array(im_2)
# im_2_np = cv.cvtColor(im_2_np, cv.COLOR_RGB2BGR)
# # cv.imshow("re", im_2_np)
#
# # 处理2左右反转
# im_3 = image.transpose(Image.FLIP_LEFT_RIGHT)
# im_3_np = np.array(im_3)
# im_3_np = cv.cvtColor(im_3_np, cv.COLOR_RGB2BGR)
# # cv.imshow("re", im_3_np)
#
# # 处理3亮度调节1
# im_4 = image.point(lambda p: p * 0.5)
# im_4_np = np.array(im_4)
# im_4_np = cv.cvtColor(im_4_np, cv.COLOR_RGB2BGR)
# cv.imshow("re", im_4_np)
#
# # 处理4亮度调节2
# im_5 = image.point(lambda p: p * 1.5)
# im_5_np = np.array(im_5)
# im_5_np = cv.cvtColor(im_5_np, cv.COLOR_RGB2BGR)
# # cv.imshow("re", im_5_np)
#
# # 旋转90C°
# im_6 = image.transpose(Image.ROTATE_90)
# im_6_np = np.array(im_6)
# im_6_np = cv.cvtColor(im_6_np, cv.COLOR_RGB2BGR)
# # cv.imshow("re", im_6_np)
#
# # 旋转270C°
# im_7 = image.transpose(Image.ROTATE_270)
# im_7_np = np.array(im_7)
# im_7_np = cv.cvtColor(im_7_np, cv.COLOR_RGB2BGR)
# # cv.imshow("re", im_7_np)
#
# cv.waitKey(0)

# Test_10
# 论文中第5章一般灰度图像处理
# import cv2 as cv
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
#     im = cv.cvtColor(I, cv.COLOR_BGR2GRAY)
#     eq = cv.equalizeHist(im)
#     img = cv.inRange(im, 30, 100)
#     # eq 一般直方图化
#     # eq = cv.equalizeHist(im)
#     # img = cv.Canny(im, 30, 70)
#
#     cv.imshow("re", I)
#     clahe = cv.createCLAHE(clipLimit=2.0,
#                            tileGridSize=(8, 8))
#
#     # 第二步：进行自适应直方图均衡化
#     cll = clahe.apply(img)
#
#
#     def onMouse(event, x, y, flags, param):
#     # 显示灰度值
#         if event == cv.EVENT_MOUSEMOVE:
#             print("x=={}\ty=={}\t值：{}".format(x, y, im[y, x]))
#             print("\n")
#
#
#     kernel = cv.getStructuringElement(shape=cv.MORPH_CROSS, ksize=(5, 5))
#     kernel2 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(5, 5))
#     # 闭运算
#     img_temp = cv.morphologyEx(cll, cv.MORPH_CLOSE, kernel)
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
#     cv.imshow("re2", cll)
#     cv.waitKey(0)


# Test_11
# 测试模型对图象的正确率并画出统计图
# import Image_CNN
# import cv2 as cv
# import matplotlib.pyplot as plt
# from Image_data.ImageData import *
#
# rootPath = "../Image_data"
#
# path = ["/toolong/", "/damage/", "/normal/", "/toosmall/"]
#
# # path = ["/all_damage/"]
#
# name_list = ["toolong", "damage", "normal", "toosmall"]
# num_list = [0, 0, 0, 0]
#
# model = Image_CNN.ImageCNNModel()
# model.loadModelFromFile(model_path="../Image_data/ImageMode.h5")
#
# for _index, value in enumerate(path):
#     for fileName in os.listdir(rootPath + value):
#         image = cv.imread(rootPath + value + fileName)
#         preResult = model.PredictFromImageNdarray(image_ndarray=image, print_result=True)
#
#         # 做判断 检测是否预判准确
#         realResult = int(fileName[0])
#
#         if preResult == realResult:
#             # 预判准确
#             num_list[_index] = num_list[_index] + 1
#
# print("准确率：\n过长：{}%\n破损{}%：\n正常：{}%\n过短：{}%\n".format(num_list[0], num_list[1], num_list[2], num_list[3]))
#
#
# def autoLabel(rects):
#     for rect in rects:
#         height = rect.get_height()
#         plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, 1.03 * height, '%s' % int(height))
#
#
# autoLabel(plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list))
# plt.show()
