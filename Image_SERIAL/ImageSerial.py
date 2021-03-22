# -*- coding: utf-8 -*-
# @File    : ImageSerial.py
# @Time    : 2020/3/25 22:11
# @Author  : Moeyu522 Lee
# @Describe: 项目串口设计

import threading

import serial
import serial.tools.list_ports


class ImageSerial:
    def __init__(self, port, baud_rate, data_bits, parity, stop_bits, timeout=3):
        self.port = port
        self.baud_rate = baud_rate
        self.data_bits = data_bits
        # 校验位
        if parity == 0:
            parity = 'None'
        if parity == 1:
            parity = 'Odd'
        if parity == 2:
            parity = 'Even'
        self.parity = parity
        # 停止位
        self.stop_bits = stop_bits
        # 超时
        self.timeout = timeout

        self.Ret = False

        try:
            self.main_engine = serial.Serial(self.port, self.baud_rate,bytesize=self.data_bits, timeout=self.timeout)
            if self.main_engine.is_open:
                self.Ret = True
        except Exception as e:
            self.e = e
            self.Ret = False

    # 打印可用串口列表
    @staticmethod
    def Print_Used_Com():
        port_list = list(serial.tools.list_ports.comports())
        print("串口信息:")
        print(port_list)

    # 打开串口
    def Open_Engine(self):
        self.main_engine.open()

    # 关闭串口
    def Close_Engine(self):
        self.main_engine.close()
        self.Ret = False
        # 检验串口是否打开
        print(self.main_engine.is_open)

    # 接收一行数据
    # 使用readline()时应该注意：打开串口时应该指定超时，否则如果串口没有收到新行，则会一直等待。
    # 如果没有超时，readline会报异常。
    def Read_Line(self):
        return self.main_engine.readline()

    # 发数据
    def Send_data(self, data):
        self.main_engine.write(data.encode('utf8'))

    # 接受数据
    def receive_data(self):
        receive_thread = SerialThread(name='Receive', main_engine=self.main_engine)

        receive_data = receive_thread.start()

        if receive_data is not None:
            return receive_data
        else:
            return None


class SerialThread(threading.Thread):
    def __init__(self, name, main_engine):
        threading.Thread.__init__(self)
        self.name = name
        self.main_engine = main_engine

    def run(self):
        data = None
        while True:
            try:
                if self.main_engine.in_waiting:
                    data = self.main_engine.read_all()
                    # 退出标志
                    if data == "exit":
                        break
                    else:
                        print("接收ascii数据：", data)
                        return data
            except Exception as e:
                print("异常报错：", e)
                return data
