import sys
sys.path.append('..')
import cv2
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from deepface import DeepFace


imgNamepath = None

class RecognizeInDB(object):
    def setupUi(self, MainWindow):
        self.img = None
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


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)  # select pic/vid
        self.pushButton_2.setGeometry(QtCore.QRect(30, 150, 230, 41))
        self.pushButton_2.setStyleSheet("font:22px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 30, 700, 81))
        self.label_2.setStyleSheet("font: 45px \"Segoe Print\";\n"
                                   "color:rgb(255, 85, 0);\n"
                                   "text-align:center;\n"
                                   "letter-spacing:4pt;")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 120, 961, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 200, 961, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)  # input path showing
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 150, 250, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 150, 151, 41))
        self.pushButton_3.setStyleSheet("font: 22px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 150, 151, 41))
        self.pushButton_4.setStyleSheet("font:22px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 411, 421))
        self.label_3.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        ###############output
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 270, 250, 251))
        self.label_4.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(540, 430, 501, 400))
        self.info.setStyleSheet("font:26px;")
        self.info.setText("")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 230, 91, 31))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 230, 88, 31))
        self.label_6.setStyleSheet("font: 14pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.pushButton_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.back.raise_()
        self.info.raise_()
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

        # ??????????????????
        self.pushButton_2.clicked.connect(self.openImage)
        self.pushButton_3.clicked.connect(self.startAction)
        self.pushButton_4.clicked.connect(self.saveImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CS308 project"))
        self.pushButton_2.setText(_translate("MainWindow", "Select image/video"))
        self.label_2.setText(_translate("MainWindow", "Face Recognition"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "Input"))
        self.label_6.setText(_translate("MainWindow", "Output"))
        self.menutest2.setTitle(_translate("MainWindow", "@Wu Jingfu, Cui Yanru, Feng Chenchen"))
        self.back.setText(_translate("MainWindow", "Back"))

    # ????????????????????????
    def openImage(self):
        self.info.setText('')
        self.label_3.clear()
        self.label_4.clear()
        global imgNamepath  # ??????????????????????????????????????????????????????????????????????????????
        # ????????????????????????????????????????????????imgName???????????????????????????+??????????????????????????????imgType?????????????????????
        # QFileDialog??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        imgNamepath, imgType = QFileDialog.getOpenFileName(self.centralwidget)
        # ???????????????????????????????????????????????????????????????label??????????????????
        img = None
        if imgNamepath[-3:] == 'mp4':
            vc = cv2.VideoCapture(imgNamepath)
            if vc.isOpened():
                rval, frame = vc.read()
                self.img = frame
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
                img = QtGui.QPixmap(image).scaled(self.label_3.width(), self.label_3.height())
            vc.release()
        else:
            self.img = cv2.imread(imgNamepath)
            img = QtGui.QPixmap(imgNamepath).scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(img)
        self.lineEdit_3.setText(imgNamepath)

    # ?????????????????????(???????????????:?????????????????????Qlabel????????????????????????????????????????????????????????????????????????????????????????????????)
    def saveImage(self):
        img = self.label_4.pixmap().toImage()
        fpath, ftype = QFileDialog.getSaveFileName(self.centralwidget)
        img.save(fpath)

    #?????????????????????????????????
    def startAction(self):
        print('Loading model...')
        classID="Class_ID: "
        name="Name: "
        sample_num="Sample_Num: "
        flag="Flag: "
        gender="Gender: "
        ########???img??????????????????????????????????????????img_in_db#########################
        df = DeepFace.find(self.img, db_path="./tests/test_small", model_name="Facenet", enforce_detection=False, distance_metric="euclidean")
        if len(df.values) > 0:
            identity_num = df.values[0][0].split('\\')[1].split('/')[0]
            print(df.values[0][0].split('\\')[1].split('/')[0])
            identity = pd.read_csv("./tests/identity.csv")
            identity = np.array(identity)
            for i in range(len(identity)):
                if identity[i][0] == identity_num:
                    print(identity[i])
                    classID += identity[i][0]
                    print(classID)
                    name += identity[i][1].split('"')[1]
                    print(name)
                    sample_num += str(identity[i][2])
                    print(sample_num)
                    flag += str(identity[i][3])
                    print(flag)
                    gender += str(identity[i][4])
                    print(gender)
                    break
            if len(df.values) > 1:
                img = QtGui.QPixmap(df.values[1][0][1:]).scaled(self.label_4.width(), self.label_4.height())
                self.label_4.setPixmap(img)
            else:
                img = QtGui.QPixmap(df.values[0][0][1:]).scaled(self.label_4.width(), self.label_4.height())
                self.label_4.setPixmap(img)
            self.info.setText("Personal information in database\n" + classID + "\n" + name + "\n" + sample_num + "\n" + flag + "\n" + gender + "\n")

        else:
            img = QtGui.QPixmap('./GUI/sorry.png').scaled(self.label_4.width(), self.label_4.height())
            self.label_4.setPixmap(img)

