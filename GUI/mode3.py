import sys
sys.path.append('..')
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from deepface import DeepFace


imgNamePath = None


class FaceAnalysis(object):
    def setupUi(self, MainWindow):
        self.img=None
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
        self.label_2.setGeometry(QtCore.QRect(350, 30, 700, 81))
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
        self.pushButton_3.setGeometry(QtCore.QRect(680, 150, 151, 41))
        self.pushButton_3.setStyleSheet("font: 22px;")
        self.pushButton_3.setObjectName("pushButton_3")
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
        ######output
        # print("Age: ", demography["age"])
        # 	print("Gender: ", demography["dominant_gender"])
        # 	print("Race: ", demography["dominant_race"])
        # 	print("Emotion: ", demography["dominant_emotion"])
        self.age = QtWidgets.QLabel(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(540, 270, 401, 100))
        self.age.setStyleSheet("font:32px;")
        self.age.setText("Age:")

        self.gender = QtWidgets.QLabel(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(540, 375, 401, 100))
        self.gender.setStyleSheet("font:32px;")
        self.gender.setText("Gender:")

        self.race = QtWidgets.QLabel(self.centralwidget)
        self.race.setGeometry(QtCore.QRect(540, 480, 401, 100))
        self.race.setStyleSheet("font:32px;")
        self.race.setText("Race:")

        self.emotion = QtWidgets.QLabel(self.centralwidget)
        self.emotion.setGeometry(QtCore.QRect(540, 585, 401, 100))
        self.emotion.setStyleSheet("font:32px;")
        self.emotion.setText("Emotion:")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 230, 91, 31))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 230, 88, 31))
        self.label_6.setStyleSheet("font: 14pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.pushButton_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.age.raise_()
        self.gender.raise_()
        self.race.raise_()
        self.emotion.raise_()
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
        self.pushButton_2.clicked.connect(self.openImage)
        self.pushButton_3.clicked.connect(self.startAction)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CS308 project"))
        self.pushButton_2.setText(_translate("MainWindow", "Select picture/video"))
        self.label_2.setText(_translate("MainWindow", "Face Analysis"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.label_5.setText(_translate("MainWindow", "Input"))
        self.label_6.setText(_translate("MainWindow", "Output"))
        self.menutest2.setTitle(_translate("MainWindow", "@Wu Jingfu, Cui Yanru, Feng Chenchen"))
        self.back.setText(_translate("MainWindow", "Back"))

    # 选择本地图片上传
    def openImage(self):
        self.label_3.clear()
        self.age.setText("Age: ")
        self.gender.setText("Gender: ")
        self.race.setText("Race: ")
        self.emotion.setText("Emotion: ")
        global imgNamepath
        imgNamepath, imgType = QFileDialog.getOpenFileName(self.centralwidget)
        # 通过文件路径获取图片文件，并设置图片长宽为label控件的长、宽
        img = None
        if imgNamepath[-3:] == 'mp4':
            vc = cv2.VideoCapture(imgNamepath)
            if vc.isOpened():
                rval, frame = vc.read()
                self.img=frame
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
                img = QtGui.QPixmap(image).scaled(self.label_3.width(), self.label_3.height())
            vc.release()
        else:
            self.img=cv2.imread(imgNamepath)
            img = QtGui.QPixmap(imgNamepath).scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(img)
        self.lineEdit_3.setText(imgNamepath)

    # ToDo: 调用模型辨别并显示结果
    def startAction(self):
        print('Loading model...')
        demography = DeepFace.analyze(self.img, enforce_detection=False)
        print(demography)
        age = demography["age"]
        print(age)
        gender = str(demography["gender"])
        print(gender)
        race = str(demography["dominant_race"])
        print(race)
        emotion = str(demography["dominant_emotion"])
        print(emotion)

        self.age.setText("Age: " + str(age))
        self.gender.setText("Gender: " + str(gender))
        self.race.setText("Race: " + str(race))
        self.emotion.setText("Emotion: " + str(emotion))
