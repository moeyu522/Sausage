# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets

import Image_CAMERA
import Image_CNN
import Image_SERIAL
import SausageMain


class UiMainForm(object):
    def setupUi(self, main_form):
        main_form.setObjectName("main_form")
        main_form.setWindowModality(QtCore.Qt.NonModal)
        main_form.resize(1200, 600)
        main_form.setMinimumSize(QtCore.QSize(1200, 600))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        main_form.setFont(font)
        main_form.setLayoutDirection(QtCore.Qt.RightToLeft)
        main_form.setAutoFillBackground(False)
        main_form.setStyleSheet(";")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(main_form)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(main_form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.image_view = QtWidgets.QLabel(main_form)
        self.image_view.setMinimumSize(QtCore.QSize(500, 500))
        self.image_view.setBaseSize(QtCore.QSize(0, 0))
        self.image_view.setStyleSheet("border-width: 2px;border-style: solid;\n"
                                      "border-color: rgb(169, 169, 169);")
        self.image_view.setText("")
        self.image_view.setScaledContents(True)
        self.image_view.setAlignment(QtCore.Qt.AlignCenter)
        self.image_view.setObjectName("image_view")
        self.verticalLayout_4.addWidget(self.image_view)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.bad_number = QtWidgets.QLabel(main_form)
        self.bad_number.setMinimumSize(QtCore.QSize(250, 0))
        self.bad_number.setMaximumSize(QtCore.QSize(500, 16777215))
        self.bad_number.setStyleSheet("border-width: 2px;border-style: solid;\n"
                                      "border-color: rgb(169, 169, 169);")
        self.bad_number.setText("")
        self.bad_number.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.bad_number.setObjectName("bad_number")
        self.horizontalLayout_11.addWidget(self.bad_number)
        self.label_17 = QtWidgets.QLabel(main_form)
        self.label_17.setEnabled(True)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_11.addWidget(self.label_17)
        self.sum_number = QtWidgets.QLabel(main_form)
        self.sum_number.setMinimumSize(QtCore.QSize(250, 0))
        self.sum_number.setMaximumSize(QtCore.QSize(500, 16777215))
        self.sum_number.setStyleSheet("border-width: 2px;border-style: solid;\n"
                                      "border-color: rgb(169, 169, 169);")
        self.sum_number.setText("")
        self.sum_number.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sum_number.setObjectName("sum_number")
        self.horizontalLayout_11.addWidget(self.sum_number)
        self.label_19 = QtWidgets.QLabel(main_form)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_11.addWidget(self.label_19)
        self.label_18 = QtWidgets.QLabel(main_form)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(20, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(main_form)
        self.label_3.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.rotate_button = QtWidgets.QPushButton(main_form)
        self.rotate_button.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.rotate_button.setFont(font)
        self.rotate_button.setObjectName("rotate_button")
        self.verticalLayout_2.addWidget(self.rotate_button)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serial_port_label = QtWidgets.QLabel(main_form)
        self.serial_port_label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.serial_port_label.setText("")
        self.serial_port_label.setPixmap(QtGui.QPixmap(":/ico/off.ico"))
        self.serial_port_label.setObjectName("serial_port_label")
        self.horizontalLayout.addWidget(self.serial_port_label)
        self.label_2 = QtWidgets.QLabel(main_form)
        self.label_2.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.serial_port_button = QtWidgets.QPushButton(main_form)
        self.serial_port_button.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.serial_port_button.setFont(font)
        self.serial_port_button.setStyleSheet("")
        self.serial_port_button.setObjectName("serial_port_button")
        self.horizontalLayout.addWidget(self.serial_port_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.run_label = QtWidgets.QLabel(main_form)
        self.run_label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.run_label.setText("")
        self.run_label.setPixmap(QtGui.QPixmap(":/ico/off.ico"))
        self.run_label.setObjectName("run_label")
        self.horizontalLayout_2.addWidget(self.run_label)
        self.label_4 = QtWidgets.QLabel(main_form)
        self.label_4.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.run_button = QtWidgets.QPushButton(main_form)
        self.run_button.setEnabled(False)
        self.run_button.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.run_button.setFont(font)
        self.run_button.setObjectName("run_button")
        self.horizontalLayout_2.addWidget(self.run_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 40, -1, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.serial_box = QtWidgets.QSpinBox(main_form)
        self.serial_box.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.serial_box.setFont(font)
        self.serial_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.serial_box.setAlignment(QtCore.Qt.AlignCenter)
        self.serial_box.setReadOnly(False)
        self.serial_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.serial_box.setMinimum(1)
        self.serial_box.setMaximum(5)
        self.serial_box.setObjectName("serial_box")
        self.horizontalLayout_3.addWidget(self.serial_box)
        self.label_6 = QtWidgets.QLabel(main_form)
        self.label_6.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.baud_rate_box = QtWidgets.QSpinBox(main_form)
        self.baud_rate_box.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.baud_rate_box.setFont(font)
        self.baud_rate_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baud_rate_box.setAlignment(QtCore.Qt.AlignCenter)
        self.baud_rate_box.setReadOnly(False)
        self.baud_rate_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.baud_rate_box.setPrefix("")
        self.baud_rate_box.setMinimum(50)
        self.baud_rate_box.setMaximum(115200)
        self.baud_rate_box.setSingleStep(20)
        self.baud_rate_box.setObjectName("baud_rate_box")
        self.horizontalLayout_4.addWidget(self.baud_rate_box)
        self.label_7 = QtWidgets.QLabel(main_form)
        self.label_7.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.data_box = QtWidgets.QSpinBox(main_form)
        self.data_box.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.data_box.setFont(font)
        self.data_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.data_box.setAlignment(QtCore.Qt.AlignCenter)
        self.data_box.setReadOnly(False)
        self.data_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.data_box.setPrefix("")
        self.data_box.setMinimum(6)
        self.data_box.setMaximum(8)
        self.data_box.setObjectName("data_box")
        self.horizontalLayout_5.addWidget(self.data_box)
        self.label_8 = QtWidgets.QLabel(main_form)
        self.label_8.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.check_box = QtWidgets.QSpinBox(main_form)
        self.check_box.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.check_box.setFont(font)
        self.check_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.check_box.setAlignment(QtCore.Qt.AlignCenter)
        self.check_box.setReadOnly(False)
        self.check_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.check_box.setPrefix("")
        self.check_box.setMinimum(0)
        self.check_box.setMaximum(2)
        self.check_box.setObjectName("check_box")
        self.horizontalLayout_6.addWidget(self.check_box)
        self.label_9 = QtWidgets.QLabel(main_form)
        self.label_9.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stop_box = QtWidgets.QSpinBox(main_form)
        self.stop_box.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.stop_box.setFont(font)
        self.stop_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stop_box.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_box.setReadOnly(False)
        self.stop_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.stop_box.setPrefix("")
        self.stop_box.setMinimum(1)
        self.stop_box.setMaximum(2)
        self.stop_box.setObjectName("stop_box")
        self.horizontalLayout_7.addWidget(self.stop_box)
        self.label_10 = QtWidgets.QLabel(main_form)
        self.label_10.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.qt_message = QtWidgets.QMessageBox()
        self.retranslateUi(main_form)
        QtCore.QMetaObject.connectSlotsByName(main_form)

        self.update_ui = SausageMain.UpdateUISign()
        self.status_code_init()
        self.function_init()

        # 载入神经网络模型
        # 并将神经网络模型存入到self.cnn_model
        self.cnn_model = Image_CNN.ImageCNNModel().loadModelFromFile()

        # 获得相机类
        self.camera = Image_CAMERA.CameraMain()

        if self.camera.Rec is True:
            self.camera.stream_on()
        else:
            self.message_show("相机打开失败")
        # 获得第一张图像并展示
        # image = self.camera.getImage(delay_time=0)
        # self.image_show(image_ndarray=image, default_rotate=True)
        # 此处用本地图像代替
        image = cv.imread("passagewayTest.png")
        self.image_show(image_ndarray=image, default_rotate=True)

    def retranslateUi(self, main_form):
        _translate = QtCore.QCoreApplication.translate
        main_form.setWindowTitle(_translate("main_form", "粒粒肠在线检测剔除系统"))
        self.label.setText(_translate("main_form", "图 像 显 示 区 域"))
        self.label_17.setText(_translate("main_form", "不合格数量"))
        self.label_19.setText(_translate("main_form", "当前总数量"))
        self.label_18.setText(_translate("main_form", "数量显示："))
        self.label_3.setText(_translate("main_form", "请先旋转图片至上方为进料口"))
        self.rotate_button.setText(_translate("main_form", "旋转"))
        self.label_2.setText(_translate("main_form", "    运行状态"))
        self.serial_port_button.setText(_translate("main_form", "串口开关"))
        self.label_4.setText(_translate("main_form", "    运行状态  "))
        self.run_button.setText(_translate("main_form", "运行开关"))
        self.serial_box.setPrefix(_translate("main_form", "COM"))
        self.label_6.setText(_translate("main_form", "串  口      "))
        self.label_7.setText(_translate("main_form", "波特率      "))
        self.label_8.setText(_translate("main_form", "数据位"))
        self.label_9.setText(_translate("main_form", "校验位"))
        self.label_10.setText(_translate("main_form", "停止位"))

    def status_code_init(self):
        # 串口开关状态
        self.serial_port_button_code = False
        self.run_button_code = False
        self.rotate_button_code = True
        self.rotate_value = 4

    def function_init(self):
        self.serial_port_button.clicked.connect(self.serial_port_button_function)
        self.run_button.clicked.connect(self.run_button_function)
        self.rotate_button.clicked.connect(self.rotate_image)
        self.update_ui.signal.connect(self.image_show_from_thread)

    def rotate_image(self):
        self.image_ndarray = cv.transpose(self.image_ndarray)
        self.image_ndarray = cv.flip(self.image_ndarray, 1)
        self.rotate_value = self.rotate_value + 1

        image_h, image_w, image_c = self.image_ndarray.shape
        image = QtGui.QImage(self.image_ndarray, image_w, image_h, 3 * image_w, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.image_view.setPixmap(QtGui.QPixmap.fromImage(image))

    def message_show(self, message):
        self.qt_message.information(self.qt_message, '消息', message, self.qt_message.Ok)

    def image_show(self, image_ndarray, default_rotate=True):
        self.image_ndarray = image_ndarray
        if default_rotate is True:
            # n 旋转次数
            n = self.rotate_value % 4
            for i in range(n):
                self.rotate_image()
                # 确保原来旋转的标志值不变
                self.rotate_value = self.rotate_value - 1
        image_h, image_w, image_c = self.image_ndarray.shape
        print("self.rotate_value={}".format(self.rotate_value))
        image = QtGui.QImage(self.image_ndarray, image_w, image_h, 3 * image_w, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.image_view.setPixmap(QtGui.QPixmap.fromImage(image))

    def image_show_from_thread(self, update_ui):
        if update_ui is True:
            self.image_show(image_ndarray=self.image_ndarray, default_rotate=False)

    def serial_port_button_function(self):
        if self.serial_port_button_code is False:
            serial_data = {'serial_box_value': "COM" + str(self.serial_box.value()),
                           'baud_rate_box_value': self.baud_rate_box.value(),
                           'data_box_value': self.data_box.value(),
                           'check_box_value': self.check_box.value(),
                           'stop_box_value': self.stop_box.value()}
            self.serial = Image_SERIAL.ImageSerial(port=serial_data['serial_box_value'],
                                                   baud_rate=serial_data['baud_rate_box_value'],
                                                   data_bits=serial_data['data_box_value'],
                                                   parity=serial_data['check_box_value'],
                                                   stop_bits=serial_data['stop_box_value'])
            if self.serial.Ret is True:
                # 测试时将条件该为False
                self.serial_port_label.setPixmap(QtGui.QPixmap(":/ico/on.ico"))
                self.run_button.setEnabled(True)
                self.rotate_button.setEnabled(False)
                self.serial_port_button_code = True
                # 获取串口、波特率、数据位、校验位、停止位数据并使按钮不可设置
                self.serial_box.setEnabled(False)
                self.baud_rate_box.setEnabled(False)
                self.data_box.setEnabled(False)
                self.check_box.setEnabled(False)
                self.stop_box.setEnabled(False)
                self.rotate_button.setEnabled(False)

                # 开始处理
                sausage_main_thread = SausageMain.SausageMain(name='image_main', ui_class=self)
                sausage_main_thread.start()
            else:
                self.message_show(message="串口打开失败\n" + str(self.serial.e))

        else:
            self.serial.Close_Engine()
            if self.serial.Ret is False:
                self.serial_port_label.setPixmap(QtGui.QPixmap(":/ico/off.ico"))
                self.run_button.setEnabled(False)
                self.rotate_button.setEnabled(True)
                self.run_label.setPixmap(QtGui.QPixmap(":/ico/off.ico"))
                self.serial_port_button_code = False
                self.run_button_code = False
                self.serial_box.setEnabled(True)
                self.baud_rate_box.setEnabled(True)
                self.data_box.setEnabled(True)
                self.check_box.setEnabled(True)
                self.stop_box.setEnabled(True)

    def run_button_function(self):
        if self.run_button_code is False:
            self.run_label.setPixmap(QtGui.QPixmap(":/ico/on.ico"))
            self.run_button_code = True
        else:
            self.run_label.setPixmap(QtGui.QPixmap(":/ico/off.ico"))
            self.run_button_code = False
