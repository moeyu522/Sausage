# -*- coding: utf-8 -*-
# @File    : ExhibitionMain.py
# @Time    : 2020/3/28 19:48
# @Author  : Moeyu522 Lee
# @Describe: 演示主要功能
import _thread
import sys
import threading
import time

import cv2 as cv
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QWidget

import Image_CV2
import Image_UI
import Image_UTIL


class ExhibitionMain(threading.Thread):
    def __init__(self, name, ui_class):
        threading.Thread.__init__(self)
        self.name = name
        self.ui_class = ui_class
        self.need_to_del_from_last_time = []
        self.next_pic_time = 0
        # 20个通道的单独照片
        # 元组(cut, top_value, bottom_value, outline)
        self.image_info = []
        # 总的香肠数
        self.sum_num = 0
        # 坏的香肠数
        self.bad_num = 0
        # 处于无效区域的香肠的总数
        self.sum_invalid = 0
        self.image_ndarray = None
        # 实验开始总共的图像
        self.image_sum = 0
        # 是否更新UI标志 数组为0 表示所有线程都结束
        self.my_thread = []

    def run(self):
        self.todo()

    def todo(self):

        self.image_ndarray = cv.imread("Test/test_1.png")

        # 判断图像是否需要旋转
        # n 旋转次数
        n = self.ui_class.rotate_value % 4
        for i in range(n):
            self.image_ndarray = cv.transpose(self.image_ndarray)
            self.image_ndarray = cv.flip(self.image_ndarray, 1)
            print("test=={}\n".format(self.ui_class.rotate_value))

        # 原图像的w, h , c 信息
        (self.image_h, self.image_w, _) = self.image_ndarray.shape
        # opencv处理照片
        opencv = Image_CV2.ImageCV2(image_ndarray=self.image_ndarray,
                                    need_to_del_from_last_time=self.need_to_del_from_last_time,
                                    passageway_number=2)

        self.need_to_del_from_last_time, self.object_bottom_value_invalid_max, self.image_info = opencv.locatingObjects()

        # 计算下一次拍照的时间
        self.next_pic_time = Image_UTIL.Util.getTimeFromPosition(self.object_bottom_value_invalid_max, self.image_h)
        print("下一次拍照的时间是：{}ms".format(self.next_pic_time))

        for passageway_number, passageway_info in enumerate(self.image_info):
            # 开通多线程处理
            self.my_thread.append(1)
            _thread.start_new_thread(self.getInfoAndSend, (passageway_number, passageway_info))

        _thread.start_new_thread(self.update_UI, ())

    def getInfoAndSend(self, passageway_number, passageway_info):
        (cut, top_value, bottom_value, outline) = passageway_info
        if len(cut) == 0:
            self.my_thread.pop()
            return
        send_time = []
        # 计算发送时间：
        for pos in bottom_value[0]:
            send_time.append(Image_UTIL.Util.getTimeFromPosition(pos, self.image_h))
        self.sum_num = self.sum_num + len(cut[0])
        self.sum_invalid = self.sum_invalid + len(cut[1])
        for _index, image in enumerate(cut[0]):
            re = self.ui_class.cnn_model.PredictFromImageNdarray(
                image_ndarray=Image_UTIL.Util.fillAndResizeImage(image), print_result=False)
            if re != 2:
                # 坏的香肠
                self.bad_num = self.bad_num + 1
                # self.ui_class.serial.Send_data(data=Image_UTIL.Util.nickName(passageway_number))
                # 延时 ms
                print("延时了{}ms发送信息".format(send_time[_index] / 100))
                time.sleep(send_time[_index] / 100)
                print("发送了剔除信息{}".format(Image_UTIL.Util.nickName(passageway_number)))
            # 画框
            # 红色：坏的
            # 绿色：好的
            # 蓝色：不在有效区域的
            x, y, w, h = cv.boundingRect(outline[0][_index])
            # 计算画图的偏差值 不然每个框都会出现在第一个通道
            x = Image_UTIL.Util.CalculateDeviationValue(x=x,
                                                        passageway_index=passageway_number,
                                                        image_w=self.image_w,
                                                        passageway_number=2)
            if re in [0, 1, 3]:
                cv.rectangle(self.image_ndarray, (x, y), (x + w, y + h), (0, 0, 255), 2)
            if re == 2:
                cv.rectangle(self.image_ndarray, (x, y), (x + w, y + h), (0, 255, 0), 2)
            for temp_outline in outline[1]:
                x, y, w, h = cv.boundingRect(temp_outline)
                # 计算画图的偏差值 不然每个框都会出现在第一个通道
                x = Image_UTIL.Util.CalculateDeviationValue(x=x,
                                                            passageway_index=passageway_number,
                                                            image_w=self.image_w,
                                                            passageway_number=2)
                cv.rectangle(self.image_ndarray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        self.my_thread.pop()

    def update_UI(self):
        while len(self.my_thread) != 0:
            pass
        self.ui_class.bad_number.setText(str(self.bad_num))

        self.ui_class.sum_number.setText(str(self.sum_num))

        self.ui_class.image_ndarray = self.image_ndarray
        self.ui_class.update_ui.start()
        if self.sum_invalid == 0:
            # self.ui_class.serial.Send_data('T')
            print("串口给单片机发送光电控制有效信息 T")
            self.control_flag = True
        else:
            self.control_flag = False
            # self.ui_class.serial.Send_data('F')
            print("串口给单片机发送光电控制有效信息 F")


class UpdateUISign(QThread):
    signal = pyqtSignal(bool)  # 括号里填写信号传递的参数

    def __init__(self):
        super(UpdateUISign, self).__init__()

    def run(self):
        # 进行任务操作
        update_ui = True
        self.signal.emit(update_ui)


if __name__ == '__main__':
    # 获得UI
    app = QApplication([])
    widget = QWidget()
    ui = Image_UI.ExhibitionUI.UiMainForm()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
