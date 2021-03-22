# -*- coding: utf-8 -*-
# @File    : Util.py
# @Time    : 2020/3/23 21:26
# @Author  : Moeyu522 Lee
# @Describe: 公共组件类

import numpy as np
from PIL import Image
import cv2 as cv
import datetime


class Util:

    @staticmethod
    def dealWith(image_path, int_label):
        # 把1张图像做5次处理 加原图像共7种
        # image_path: 需要处理的图片的位置
        # int_label: 图片的标签，整形
        # 返回 图像的ndarray数组，标签的ndarray数组

        image_list_ndarray = []
        label_list_ndarray = []

        image = Image.open(image_path)

        # 添加原图像
        im = np.array(image)
        image_list_ndarray.append(im)
        label_list_ndarray.append(int(int_label))

        # 处理1上下反转
        im = image.transpose(Image.FLIP_TOP_BOTTOM)
        im = np.array(im)
        image_list_ndarray.append(im)
        label_list_ndarray.append(int(int_label))

        # 处理2左右反转
        im = image.transpose(Image.FLIP_LEFT_RIGHT)
        im = np.array(im)
        image_list_ndarray.append(im)
        label_list_ndarray.append(int(int_label))

        # 处理3亮度调节1
        im = image.point(lambda p: p * 0.5)
        im = np.array(im)
        image_list_ndarray.append(im)
        label_list_ndarray.append(int(int_label))

        # 处理4亮度调节2
        im = image.point(lambda p: p * 1.5)
        im = np.array(im)
        image_list_ndarray.append(im)
        label_list_ndarray.append(int(int_label))

        # 旋转90C°
        im = image.transpose(Image.ROTATE_90)
        im = np.array(im)
        image_list_ndarray.append(im)
        label_list_ndarray.append(int(int_label))

        # 旋转270C°
        im = image.transpose(Image.ROTATE_270)
        im = np.array(im)
        image_list_ndarray.append(im)
        label_list_ndarray.append(int(int_label))

        return image_list_ndarray, label_list_ndarray

    @staticmethod
    def disOrder(image_list_ndarray, label_list_ndarray):
        # 对图像排列打乱 返回ndarray数组
        # image_list_ndarray: 图像的ndarray数组
        # label_list_ndarray：标签的ndarray数组
        temp = np.array([image_list_ndarray, label_list_ndarray])
        # 使图片和标签相对应
        temp = temp.transpose()
        # 打乱顺序
        np.random.shuffle(temp)
        # temp[:, 0]为ndarray类型，先转为list在转为ndarray以确保得到个数x宽x高x维度的模型输入数据
        image = np.array(list(temp[:, 0]))
        # 把便签转换成int型
        label = np.array([int(i) for i in temp[:, 1]])
        # image, label为ndarray数组
        return image, label

    @staticmethod
    def locatingObjectsFromSingleImage(image_ndarray):
        # 该项目香肠定位的关键函数为Image_UTIL.Util.locatingObjectsFromSingleImage
        # 主要采用HSV颜色空间进行颜色的初步定位
        # 结合香肠的面积、长轴长、短轴长等特性进一步筛选，去除传送带上的杂质
        # 无效区域为图像顶部1/10
        # image_ndarray: opencv读入的图像的ndarray数组
        # 返回：元组，(cut, top_value, bottom_value, outline)
        # all_cut:
        # passageway_image_cut_effective: 单独通道中通过定位剪切后的有效区域内的香肠照片，ndarray数组
        # passageway_image_cut_invalid: 单独通道中通过定位剪切后的无效区域内的香肠照片，ndarray数组

        # top_value:
        # object_top_value_effective: 有效区域内的单个香肠的定位矩形框的顶部值
        # object_top_value_invalid: 无效区域内的单个香肠的定位矩形框的顶部值

        # bottom_value:
        # object_bottom_value_effective: 有效区域内的单个香肠的定位矩形框的底部值
        # object_bottom_value_invalid: 无效区域内的单个香肠的定位矩形框的底部值

        # all_outline:
        # passageway_image_outline_effective: 通道中有效的香肠的轮廓信息
        # passageway_image_outline_invalid: 通道中无效的香肠的轮廓信息

        passageway_image_cut_effective = []
        passageway_image_cut_invalid = []

        object_top_value_effective = []
        object_top_value_invalid = []

        object_bottom_value_effective = []
        object_bottom_value_invalid = []

        passageway_image_outline_effective = []
        passageway_image_outline_invalid = []

        # 确定图像的高宽
        (image_h, image_w, _) = image_ndarray.shape
        # 计算有效区域的临界值
        effective_region_threshold = image_h / 10

        # 定位图像

        # 颜色空间转换
        hsv_image = cv.cvtColor(image_ndarray, cv.COLOR_BGR2HSV)
        # 香肠的hsv定义
        red_low = np.array([1, 60, 20])
        red_high = np.array([15, 200, 255])
        # 阈值HSV图像仅获得红色
        img = cv.inRange(hsv_image, red_low, red_high)
        # 卷积核
        # 新加入结构元
        kernel = cv.getStructuringElement(shape=cv.MORPH_CROSS, ksize=(5, 5))
        kernel2 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(5, 5))
        # 闭运算
        img_temp = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
        # 开运算
        img_temp = cv.morphologyEx(img_temp, cv.MORPH_OPEN, kernel)
        # 腐蚀3次，膨胀5次
        img_temp = cv.erode(img_temp, kernel2, iterations=3)
        img_temp = cv.dilate(img_temp, kernel2, iterations=5)
        # 找到轮廓
        outline, hierarchy = cv.findContours(img_temp, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # 对轮廓进行处理，筛选轮廓
        if len(outline) == 0:
            all_cut, top, bottom, all_outline = ([], [], [], [])
            return all_cut, top, bottom, all_outline
        else:
            # 计算面积平均值
            sum_area = 0
            for cnt in outline:
                area = cv.contourArea(cnt)
                sum_area = area + sum_area
            # 面积平均值 area_average
            area_average = sum_area / len(outline)

            # 临时outline，用于删除杂质，面积法
            temp_outline = []

            for cnt in outline:
                # 根据平均均值删除一些轮廓
                area = cv.contourArea(cnt)
                if area > area_average * 0.20:
                    temp_outline.append(cnt)

            outline = temp_outline

            # 对轮廓排序 哎，脑袋炸了，就先不考虑性能了，能用就行
            # outline[0][0][0][1] ：第一个轮廓的y值
            # outline[1][0][0][1] ：第二个轮廓的y值
            max_y = outline[0][0][0][1]
            new_outline = []
            while len(outline) != 0:
                # 找到最大值及其位置
                index = 0
                for _index, temp in enumerate(outline):
                    if temp[0][0][1] < max_y:
                        continue
                    else:
                        max_y = temp[0][0][1]
                        # 最大值位置
                        index = _index
                new_outline.append(outline[index])
                # 替换原来假设的最大值
                max_y = outline[0][0][0][1]
                # 找到最大值后 删除原来位置的值
                del outline[index]

            for cnt in new_outline:
                # 做其他运算
                x, y, w, h = cv.boundingRect(cnt)
                # print("x={}\ty={}".format(x, y))
                x, y, w, h = x - 6, y - 6, w + 12, h + 12
                # 在上一步扩大像素6后防止x,y为负值,w,h超出图像范围
                if x < 0:
                    x = 0
                if y < 0:
                    y = 0
                if w > image_w:
                    w = image_w
                if h > image_h:
                    h = image_h
                # 改进cut，原版为剪切的矩形，新版为剪切轮廓，得到只包含轮廓实心的粒粒肠
                # 注意：尺寸与通道大小、原图尺寸有关
                temp = np.ones((image_h, image_w, 3), np.uint8) * 255
                cv.fillPoly(temp, pts=[cnt], color=(0, 0, 0))
                temp = temp[y:y + h, x:x + w]
                # 判断轮廓是否位于有效区域内
                if 0 <= y + 6 <= effective_region_threshold:
                    # passageway_image_cut_invalid.append(image_ndarray[y:y + h, x:x + w])
                    passageway_image_cut_invalid.append(cv.bitwise_or(temp, image_ndarray[y:y + h, x:x + w]))
                    object_top_value_invalid.append(y + 6)
                    object_bottom_value_invalid.append(y + h - 6)
                    passageway_image_outline_invalid.append(cnt)
                else:
                    # passageway_image_cut_effective.append(image_ndarray[y:y + h, x:x + w])
                    passageway_image_cut_effective.append(cv.bitwise_or(temp, image_ndarray[y:y + h, x:x + w]))
                    object_top_value_effective.append(y + 6)
                    object_bottom_value_effective.append(y + h - 6)
                    passageway_image_outline_effective.append(cnt)

            all_cut = (passageway_image_cut_effective, passageway_image_cut_invalid)
            top = (object_top_value_effective, object_top_value_invalid)
            bottom = (object_bottom_value_effective, object_bottom_value_invalid)
            all_outline = (passageway_image_outline_effective, passageway_image_outline_invalid)

            return all_cut, top, bottom, all_outline

    @staticmethod
    def fillAndResizeImage(image_ndarray):
        # 将剪切的香肠图片填充到960*960
        # 再把图像缩小到256*256
        # 新版采用位运算来剪切粒粒肠
        h, w, _ = image_ndarray.shape
        new_image = np.ones((960, 960, 3), np.uint8) * 255
        new_image[int(480 - h / 2):int(480 + h / 2), int(480 - w / 2):int(480 + w / 2)] = image_ndarray
        new_image = cv.resize(new_image, (256, 256), interpolation=cv.INTER_AREA)
        return new_image

    @staticmethod
    def getTimeFromPosition(object_bottom_value_invalid_max, image_h):
        # 计算下一次拍照的速度
        # 传入所有不在有效区域的香肠的下端值的最大值
        # 图像按照1280*960计算
        # 计算公式：
        # (1 - (object_bottom_value_invalid_max / 960)) *  (80/400)
        # 二级传送带速度：v=400mm/s
        # 拍摄区域836mm*80mm
        time = (1 - (object_bottom_value_invalid_max / image_h)) * (1 / 5)
        return time

    @staticmethod
    def nickName(index):
        re = None
        if 0 <= index <= 9:
            re = str(index)
        if index is 10:
            re = 'A'
        if index is 11:
            re = 'B'
        if index is 12:
            re = 'C'
        if index is 13:
            re = 'D'
        if index is 14:
            re = 'E'
        if index is 15:
            re = 'F'
        if index is 16:
            re = 'G'
        if index is 17:
            re = 'H'
        if index is 18:
            re = 'I'
        if index is 19:
            re = 'J'
        if index is 20:
            re = 'K'

        re = re + 'L'

        return re

    @staticmethod
    def saveImage(image, index, save_path='image_save_data/'):
        now_time = datetime.datetime.now().strftime('%F_%T_')
        file_name = save_path + str(now_time) + '_' + str(index) + '.png'
        cv.imwrite(file_name, image)

    @staticmethod
    def mergeImage(image_1, image_2):
        # 拼接图片
        image_re = np.hstack([image_1, image_2])
        return image_re

    @staticmethod
    def CalculateDeviationValue(x, passageway_index, image_w, passageway_number=20):
        # 计算画图的偏差值 不然每个框都会出现在第一个通道
        # 主要计算x值， y值不变
        passageway_spacing = image_w // passageway_number

        return (passageway_index * passageway_spacing) + x
