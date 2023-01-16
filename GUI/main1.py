import sys
import cv2
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from mode1 import RecognizeInDB
from mode2 import Compare
from mode3 import FaceAnalysis


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 641)
        # 给MainWindow设置背景图片
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap('D:\\python\\RRJ\\pycharmproject\\Practice\\chep2\\bdd'
        #                                                      '\\background3.jpg')))
        # MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 220, 101, 31))
        self.label_2.setStyleSheet("font:32px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 320, 101, 31))
        self.label_3.setStyleSheet("font:32px;")
        self.label_3.setObjectName("label_3")
        ##buttons
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(330, 445, 281, 51))
        self.pushButton1.setStyleSheet("color:rgb(101,153,26);\n"
                                       "background-color:rgb(198,224,205);\n"
                                       "hover{color:red};\n"
                                       "border-radius:6px;\n"
                                       "font:28px;")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(330, 505, 281, 51))
        self.pushButton2.setStyleSheet("color:rgb(101,153,26);\n"
                                       "background-color:rgb(198,224,205);\n"
                                       "hover{color:red};\n"
                                       "border-radius:6px;\n"
                                       "font:28px;")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(330, 565, 281, 51))
        self.pushButton3.setStyleSheet("color:rgb(101,153,26);\n"
                                       "background-color:rgb(198,224,205);\n"
                                       "hover{color:red};\n"
                                       "border-radius:6px;\n"
                                       "font:28px;")
        self.pushButton3.setObjectName("pushButton3")
        #####buttons
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 50, 651, 101))
        self.label.setStyleSheet("border-width:0px;\n"
                                 "border-style:solid;\n"
                                 "border-color:rgb(50, 50, 50);\n"
                                 "font:54px;\n"
                                 "\n"
                                 "color:rgb(255, 170, 0)")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(50, 160, 800, 250))
        self.label1.setStyleSheet("border-width:0px;\n"
                                  "border-style:solid;\n"
                                  "border-color:rgb(50, 50, 50);\n"
                                  "font:28px \"Segoe Print\";\n"
                                  "\n"
                                  "color:rgb(101,153,26)")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CS308 project"))
        self.pushButton1.setText(_translate("MainWindow", "Face Recognition"))
        self.pushButton2.setText(_translate("MainWindow", "Face Comparison"))
        self.pushButton3.setText(_translate("MainWindow", "Face Analysis"))
        self.label.setText(_translate("MainWindow", "Welcome!!!"))
        self.label1.setText(_translate("MainWindow",
                                       "This is a face recognition system based on FaceNet512.\n Select a mode and input images/videos with faces!!\n\n\nReference: https://github.com/serengil/deepface"))


class FirstWindowActions(Ui_MainWindow, QMainWindow):
    def __init__(self):
        # 创建界面
        super().__init__()
        self.setupUi(self)
        self.pushButton1.clicked.connect(self.click_button1)
        self.pushButton2.clicked.connect(self.click_button2)
        self.pushButton3.clicked.connect(self.click_button3)

    def click_button1(self):
        self.scend_window = RecognizeInDB_Action()
        self.scend_window.show()
        self.close()

    def click_button2(self):
        self.scend_window = Compare_Action()
        self.scend_window.show()
        self.close()

    def click_button3(self):
        self.scend_window = FaceAnalysis_Action()
        self.scend_window.show()
        self.close()


class RecognizeInDB_Action(RecognizeInDB, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.go_back)

    def go_back(self):
        self.window = FirstWindowActions()
        self.window.show()
        self.close()


class Compare_Action(Compare, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.go_back)

    def go_back(self):
        self.window = FirstWindowActions()
        self.window.show()
        self.close()

class FaceAnalysis_Action(FaceAnalysis, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.go_back)

    def go_back(self):
        self.window = FirstWindowActions()
        self.window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 显示创建的界面
    MainWindow = FirstWindowActions()  # 创建窗体对象
    MainWindow.show()  # 显示窗体

    sys.exit(app.exec_())  # 程序关闭时退出进程
