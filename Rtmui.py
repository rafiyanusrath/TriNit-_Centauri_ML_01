from PyQt5 import QtCore, QtGui, QtWidgets
from vid_detect import YOLOVideoDetector
from img_detect import YOLODetector_Image
from FEye import YOLOWebCamDetector
class Ui_RTM(object):
    def setupUi(self, RTM):
        RTM.setObjectName("RTM")
        RTM.resize(918, 328)
        self.centralwidget = QtWidgets.QWidget(RTM)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 751, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(50, 170, 811, 51))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        #Image button
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setObjectName("b1")
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.clicked.connect(self.import_image)
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)

        #video button
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.setObjectName("b2")
        self.pushButton_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_2.clicked.connect(self.start_video_detection)
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)


        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton.setObjectName("b3")
        self.pushButton_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_3.clicked.connect(self.start_fish_detection)
        RTM.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RTM)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 26))
        self.menubar.setObjectName("menubar")
        RTM.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RTM)
        self.statusbar.setObjectName("statusbar")
        RTM.setStatusBar(self.statusbar)

        self.load_styles()

        self.retranslateUi(RTM)
        QtCore.QMetaObject.connectSlotsByName(RTM)

    def load_styles(self):
        # Load CSS file
        with open("Styles/style.css", "r") as f:
            self.stylesheet = f.read()

        # Apply styles
        self.label.setStyleSheet(self.stylesheet)
        self.pushButton.setStyleSheet(self.stylesheet)
        self.pushButton_2.setStyleSheet(self.stylesheet)
        self.pushButton_3.setStyleSheet(self.stylesheet)

    def retranslateUi(self, RTM):
        _translate = QtCore.QCoreApplication.translate
        RTM.setWindowTitle(_translate("RTM", "MainWindow"))
        self.label.setText(_translate("RTM", "Real-Time Traffic Monitoring Module Via FishEye (Yolov8)"))
        self.label.setObjectName("title")
        self.pushButton.setText(_translate("RTM", "Image"))
        self.pushButton_2.setText(_translate("RTM", "Video Feed"))
        self.pushButton_3.setText(_translate("RTM", "Live Feeds"))

    def import_image(self):
        if not hasattr(self, 'img_detect') or not self.img_detect.isVisible():
            # Create the YOLODetector_Image instance only if it doesn't exist or is not visible
            self.img_detect = YOLODetector_Image()
            self.img_detect.show()
    
    def start_video_detection(self):
        # Create an instance of YOLOVideoDetector
        self.yolo_detector = YOLOVideoDetector()
        self.yolo_detector.show()
    
    def start_fish_detection(self):
        # Create an instance of YOLOVideoDetector
        self.yolo_detector = YOLOFishDetector()
        self.yolo_detector.show()