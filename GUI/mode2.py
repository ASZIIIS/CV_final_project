import sys
from cmath import e

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from deepface import DeepFace



img_path1 = None
img_path2 = None
WIDTH = 411
HEIGHT = 421

class Compare(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 961, 721))
        self.label.setStyleSheet("font:28px;\n"
                                 "border-style:solid;\n"
                                 "border-width:1px;\n"
                                 "border-color:rgb(0, 0, 0);\n"
                                 "\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")

        self.back = QtWidgets.QPushButton(self.centralwidget)  # go back
        self.back.setGeometry(QtCore.QRect(20, 10, 80, 35))
        self.back.setStyleSheet("font:22px;")
        self.back.setObjectName("pushButton_2")
        ###################################select pic/vid############################################
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)  # select pic/vid
        self.pushButton_1.setGeometry(QtCore.QRect(30, 95, 200, 41))
        self.pushButton_1.setStyleSheet("font:22px;")
        self.pushButton_1.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)  # input path showing
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 95, 250, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)  # select pic/vid
        self.pushButton_2.setGeometry(QtCore.QRect(500, 95, 200, 41))
        self.pushButton_2.setStyleSheet("font:22px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)  # input path showing
        self.lineEdit_4.setGeometry(QtCore.QRect(700, 95, 250, 41))
        self.lineEdit_4.setObjectName("lineEdit_3")
        ################################select pic/vid###############################################
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 700, 81))
        self.label_2.setStyleSheet("font: 45px \"Segoe Print\";\n"
                                   "color:rgb(255, 85, 0);\n"
                                   "text-align:center;\n"
                                   "letter-spacing:4pt;")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 961, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 140, 961, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        ########## start
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 160, 151, 41))
        self.pushButton_3.setStyleSheet("font: 22px;")
        self.pushButton_3.setObjectName("pushButton_3")
        #input1#
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 225, 411, 421))
        self.label_3.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_3.setText("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 190, 91, 31))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        #input2#
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 225, 411, 421))
        self.label_4.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 190, 88, 31))
        self.label_6.setStyleSheet("font: 14pt \"Arial\";")
        self.label_6.setObjectName("label_6")

        ###output#########################################################
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(40, 330, 961, 721))
        self.output.setStyleSheet("font:28px\"Segoe Print\"")
        self.output.setText("")
        self.output.setObjectName("output")
        self.output.raise_()
        self.label.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.back.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 26))
        self.menubar.setObjectName("menubar")
        self.menutest2 = QtWidgets.QMenu(self.menubar)
        self.menutest2.setObjectName("menutest2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondemo1 = QtWidgets.QAction(MainWindow)
        self.actiondemo1.setObjectName("actiondemo1")
        self.actiondemo2 = QtWidgets.QAction(MainWindow)
        self.actiondemo2.setObjectName("actiondemo2")
        self.menutest2.addAction(self.actiondemo1)
        self.menutest2.addAction(self.actiondemo2)
        self.menubar.addAction(self.menutest2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 按钮关联函数
        self.pushButton_1.clicked.connect(lambda: self.openImage(1))
        self.pushButton_2.clicked.connect(lambda: self.openImage(2))
        self.pushButton_3.clicked.connect(self.startAction)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CS308 project"))
        self.pushButton_1.setText(_translate("MainWindow", "Select Image 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Select Image 2"))
        self.label_2.setText(_translate("MainWindow", "Compare two faces"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.label_5.setText(_translate("MainWindow", "Input1"))
        self.label_6.setText(_translate("MainWindow", "Input2"))
        self.menutest2.setTitle(_translate("MainWindow", "@Wu Jingfu, Cui Yanru, Feng Chenchen"))
        self.back.setText(_translate("MainWindow", "Back"))

    # 选择本地图片上传
    def openImage(self, type):
        global img_path1,img_path2
        img_path, img_type = QFileDialog.getOpenFileName(self.centralwidget)
        img = None
        if img_path[-3:] == 'mp4':
            vc = cv2.VideoCapture(img_path)
            if vc.isOpened():
                rval, frame = vc.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
                img = QtGui.QPixmap(image).scaled(WIDTH, HEIGHT)
            vc.release()
        else:
            img = QtGui.QPixmap(img_path).scaled(WIDTH, HEIGHT)
        if type == 1:
            img_path1 = img_path
            self.label_3.setPixmap(img)
            self.lineEdit_3.setText(img_path1)
        else:
            img_path2 = img_path
            self.label_4.setPixmap(img)
            self.lineEdit_4.setText(img_path2)

    # ToDo: 调用模型辨别并显示结果
    def startAction(self):

        flag = False #相同就True

        res = DeepFace.verify(img_path1, img_path2, detector_backend='opencv', model_name="Facenet", distance_metric="euclidean")
        print(res)
        if res['verified'] == True:
            flag = True
            confidence = 1/e**(res['distance']/10)
            confidence += 0.9*(1-confidence)
        else:
            confidence = (res['distance']-10)/10
            confidence += 0.9*(1-confidence)


        if flag:
            self.output.setText("They are the Same person. Confidence:"+str(confidence))
        else:
            self.output.setText("They are not the Same person. Confidence:"+str(confidence))


