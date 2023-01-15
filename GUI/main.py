import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap

imgNamepath = None


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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 410, 181, 51))
        self.pushButton.setStyleSheet("color:rgb(101,153,26);\n"
                                      "background-color:rgb(198,224,205);\n"
                                      "hover{color:red};\n"
                                      "border-radius:6px;\n"
                                      "font:28px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 50, 651, 101))
        self.label.setStyleSheet("border-width:0px;\n"
                                 "border-style:solid;\n"
                                 "border-color:rgb(50, 50, 50);\n"
                                 "font:54px;\n"
                                 "\n"
                                 "color:rgb(255, 170, 0)")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(50, 180, 800, 200))
        self.label1.setStyleSheet("border-width:0px;\n"
                                 "border-style:solid;\n"
                                 "border-color:rgb(50, 50, 50);\n"
                                 "font:30px;\n"
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
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.label.setText(_translate("MainWindow", "Welcome!!!"))
        self.label1.setText(_translate("MainWindow", "This is a face recognition system based on FaceNet512.\n Input images/videos with faces for recognition!\n\n\nReference: https://github.com/serengil/deepface"))

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 给MainWindow设置图标
        # MainWindow.setWindowIcon(QIcon('D:\\download\\xj.ico'))  # 路径错误找不到问题所在

        # 给MainWindow设置背景图片
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap('D:\\python\\RRJ\\pycharmproject\\Practice\\chep2\\bdd'
        #                                                      '\\background3.jpg')))
        # MainWindow.setPalette(palette)

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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)  # select pic/vid
        self.pushButton_2.setGeometry(QtCore.QRect(30, 150, 230, 41))
        self.pushButton_2.setStyleSheet("font:22px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 30, 700, 81))
        self.label_2.setStyleSheet("font: 75 26pt \"Segoe Print\";\n"
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 270, 401, 421))
        self.label_4.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
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
        self.pushButton_4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
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
        self.pushButton_4.clicked.connect(self.saveImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CS308 project"))
        self.pushButton_2.setText(_translate("MainWindow", "Select picture/video"))
        self.label_2.setText(_translate("MainWindow", "Face Recognition System"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "Input"))
        self.label_6.setText(_translate("MainWindow", "Output"))
        self.menutest2.setTitle(_translate("MainWindow", "@Wu Jingfu, Cui Yanru, Feng Chenchen"))
        self.actiondemo1.setText(_translate("MainWindow", "demo1"))
        self.actiondemo2.setText(_translate("MainWindow", "demo2"))

    # 选择本地图片上传
    def openImage(self):
        global imgNamepath  # 这里为了方便别的地方引用图片路径，将其设置为全局变量
        # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是默认打开的路径，第四个参数是需要的格式
        imgNamepath, imgType = QFileDialog.getOpenFileName(self.centralwidget)
        # 通过文件路径获取图片文件，并设置图片长宽为label控件的长、宽
        img = None
        if imgNamepath[-3:] == 'mp4':
            vc = cv2.VideoCapture(imgNamepath)
            if vc.isOpened():
                rval, frame = vc.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
                img = QtGui.QPixmap(image).scaled(self.label_3.width(), self.label_3.height())
            vc.release()
        else:
            img = QtGui.QPixmap(imgNamepath).scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(img)
        self.lineEdit_3.setText(imgNamepath)

    # 保存图片到本地(第二种方式:首先提取相对应Qlabel中的图片，然后打开一个保存文件的弹出框，最后保存图片到选中的路径)
    def saveImage(self):
        # 提取Qlabel中的图片
        img = self.label_4.pixmap().toImage()
        fpath, ftype = QFileDialog.getSaveFileName(self.centralwidget)
        img.save(fpath)

    # ToDo: 调用模型辨别并显示结果
    def startAction(self):
        img = None
        if imgNamepath[-3:] == 'mp4':
            vc = cv2.VideoCapture(imgNamepath)
            # n = 1  # 计数
            if vc.isOpened():  # ToDo:这里先只写了读视频的第一帧
                rval, frame = vc.read()
                img = frame
            # else:
            #     rval = False
            # timeF = 10  # 视频帧计数间隔频率
            # i = 0
            # while rval:  # 循环读取视频帧
            #     rval, frame = vc.read()
            #     if (n % timeF == 0):  # 每隔timeF帧进行存储操作
            #         i += 1
            #         print(i)
            #         cv2.imwrite('images/{}.jpg'.format(i), frame)  # 存储为图像
            #     n = n + 1
            #     cv2.waitKey(1)
            vc.release()
        else:
            img = cv2.imread(imgNamepath)
        print('Loading model...')
        img = cv2.resize(img, dsize=(768, 1080))
        # 图像转灰度图像
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 灰度图像到反转灰度图像
        inverted_gray_image = 255 - gray_image
        # 模糊倒置灰度图像
        blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19, 19), 0)
        # 反转模糊图像
        inverted_blurred_image = 255 - blurred_inverted_gray_image
        # 准备照片素描
        sketck = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
        # 因为不知道怎么将<class 'numpy.ndarray'>转换为<class 'PyQt5.QtGui.QPixmap'>类型，因此采用暂存再读出的方式
        cv2.imwrite('ZC.jpg', sketck)
        # pyqt5从路径读取图片
        imgShow = QPixmap('ZC.jpg').scaled(self.label_4.width(), self.label_4.height())
        self.label_4.setScaledContents(True)
        self.label_4.setPixmap(imgShow)


class FirstWindowActions(Ui_MainWindow, QMainWindow):

    def __init__(self):
        # 创建界面
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_login_button)

    def click_login_button(self):
        """点击登录按钮，跳转到相应界面"""
        # 实例化第二个界面的后端类，并对第二个界面进行显示
        self.scend_window = SecondWindowActions()
        # 显示第二个界面
        self.scend_window.show()
        # 关闭第一个界面
        self.close()


class SecondWindowActions(Ui_MainWindow2, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 显示创建的界面
    MainWindow = FirstWindowActions()  # 创建窗体对象
    MainWindow.show()  # 显示窗体

    sys.exit(app.exec_())  # 程序关闭时退出进程
