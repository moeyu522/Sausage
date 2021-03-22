# -*- coding: utf-8 -*-
# @File    : CameraMain.py
# @Time    : 2020/3/25 3:31
# @Author  : Moeyu522 Lee
# @Describe: 拍照主入口

import Image_CAMERA.gxipy as gx
import time


class CameraMain:
    def __init__(self):
        self.Rec = True
        # 创建一个设备管理
        device_manager = gx.DeviceManager()
        dev_num, dev_info_list = device_manager.update_device_list()
        if dev_num is 0:
            print("相机：设备数为0！")
            self.Rec = False
            return

        # 打开一个设备
        # 获取设备基本信息列表
        str_sn = dev_info_list[0].get("sn")
        self.cam = device_manager.open_device_by_sn(str_sn)

        # 设置参数

        # 设置触发模式为OFF
        self.cam.TriggerMode.set(gx.GxSwitchEntry.OFF)

    # 发送开始命令，相机开始传送图像数据
    def stream_on(self):
        self.cam.stream_on()

    def stream_off(self):
        self.cam.stream_off()

    # 软件控制拍照
    def getImage(self, delay_time):
        # delay_time: 下一次拍照的时间
        time.sleep(delay_time)

        # 提高照片质量
        if self.cam.GammaParam.is_readable():
            gamma_value = self.cam.GammaParam.get()
            gamma_lut = gx.Utility.get_gamma_lut(gamma_value)
        else:
            gamma_lut = None
        if self.cam.ContrastParam.is_readable():
            contrast_value = self.cam.ContrastParam.get()
            contrast_lut = gx.Utility.get_contrast_lut(contrast_value)
        else:
            contrast_lut = None
        color_correction_param = self.cam.ColorCorrectionParam.get()

        # 得到原始图像
        raw_image = self.cam.data_stream[0].get_image()
        if raw_image is None:
            return None

        # 转换为RGB
        rgb_image = raw_image.convert("RGB")
        if rgb_image is None:
            return None
        # 提高照片质量
        rgb_image.image_improvement(color_correction_param, contrast_lut, gamma_lut)

        # 创建image_ndarray
        numpy_image = rgb_image.get_numpy_array()
        if numpy_image is None:
            return None

        return numpy_image
