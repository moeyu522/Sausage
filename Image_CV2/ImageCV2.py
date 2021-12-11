# -*- coding: utf-8 -*-
# @File    : ImageCV2.py
# @Time    : 2020/3/24 2:10
# @Author  : Moeyu522 Lee
# @Describe: 原始图像的香肠的定位和提取，将提取的香肠存于空白图片中然后返回
# 传入的照片按1280*960计算
# 比较重要的参数说明：
# 原始图像命名规则：(年-月-日)+'_'+(hh:mm:ss)+'_'+系统开机到目前位置所拍照的序号
from Image_UTIL import *


class ImageCV2:
    def __init__(self, image_ndarray, need_to_del_from_last_time=None, passageway_number=20):
        # image_ndarray: 图像的ndarray数组，openCV读取的图像
        # need_to_del_from_last_time: 前一张位于图像下部，需要被删除的部分香肠，数据类型为列表，元素类型为通道名称
        # passageway_number：图像需要划分的通道的数量。默认20
        self.__image_ndarray__ = image_ndarray
        self.__need_to_del_from_last_time__ = need_to_del_from_last_time
        self.__passageway_number__ = passageway_number

    def divideImage(self):
        # 给图像划分，得到图像每个通道的单独图像，存放在一个passageway_list里并返回
        passageway_list = []
        # 划分每个通道的范围
        (image_h, image_w, _) = self.__image_ndarray__.shape
        passageway_spacing = image_w // self.__passageway_number__
        for i in range(0, image_w, passageway_spacing):
            # temp_x和temp_y为每个通道的左上角坐标,计算机坐标系
            temp_x = i
            temp_y = 0
            passageway_list.append(self.__image_ndarray__[temp_y:temp_y + image_h, temp_x:temp_x + passageway_spacing])
        return passageway_list

    def locatingObjects(self):
        # 调用Image_UTIL.locatingObjectsFromSingleImage方法得到单个通道的（剪切图，香肠上端y值，香肠下端y值，香肠原始轮廓）
        # 该方法将进一步处理这些信息，计算出原始图像的下一张时间采集计算点。处于无效区域的香肠的最大下端值
        # 返回：
        # object_bottom_value_invalid_max：无效区域下端最大值
        # next_time_need_to_del: 下一次需要直接删除的香肠，说明第几通道eg，[1,4,18]，1、4、18通道需要删除第一个香肠
        # image_info : 为列表20个，每个元素为元组，每个元组包含每个通道的(cut, top_value, bottom_value, outline)四个元组
        #
        # 划分通道
        passageway_list = self.divideImage()
        object_bottom_value_invalid_max = 0

        # 下一次需要直接删除的香肠
        next_time_need_to_del = []
        # eg： cut包含image_cut_effective和image_cut_invalid两个列表
        image_info = []
        # 所有的有效区域的香肠的上端值
        object_top_value_effective_all = []

        for _passageway_index, _passageway_image in enumerate(passageway_list):
            (cut, top, bottom, outline) = Util.locatingObjectsFromSingleImage(image_ndarray=_passageway_image)

            # 防止通道里一个都没有
            if len(cut) == 0:
                cut = ()
                top = ()
                bottom = ()
                outline = ()
                image_info_temp = (cut, top, bottom, outline)
                image_info.append(image_info_temp)
            else:
                (passageway_image_cut_effective, passageway_image_cut_invalid) = cut
                (object_top_value_effective, object_top_value_invalid) = top
                (object_bottom_value_effective, object_bottom_value_invalid) = bottom
                (passageway_image_outline_effective, passageway_image_outline_invalid) = outline

                # 删除上一次残留在图像中的香肠
                if self.__need_to_del_from_last_time__ is not None:
                    for i in range(0, self.__passageway_number__):
                        if i in self.__need_to_del_from_last_time__:
                            del passageway_image_cut_effective[0]
                            del object_top_value_effective[0]
                            del object_bottom_value_effective[0]
                            del passageway_image_outline_effective[0]

                cut = (passageway_image_cut_effective, passageway_image_cut_invalid)
                top = (object_top_value_effective, object_top_value_invalid)
                bottom = (object_bottom_value_effective, object_bottom_value_invalid)
                outline = (passageway_image_outline_effective, passageway_image_outline_invalid)

                image_info_temp = (cut, top, bottom, outline)
                image_info.append(image_info_temp)

                # 计算无效区域下端最大值
                for i in range(0, len(object_bottom_value_invalid)):
                    if object_bottom_value_invalid_max < object_bottom_value_invalid[i]:
                        object_bottom_value_invalid_max = object_bottom_value_invalid[i]

        # 计算下一次需要删除的通道
        for i in range(len(object_top_value_effective_all)):
            for j in object_top_value_effective_all[i]:
                if max(j) > object_bottom_value_invalid_max:
                    next_time_need_to_del.append(i)

        return next_time_need_to_del, object_bottom_value_invalid_max, image_info
