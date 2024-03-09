import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QFileDialog, QTextEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from ultralytics import YOLO
import cv2

class_mapping = {
    0: 'D00',
    1: 'D40',
    2: 'D10',
    3: 'D20', 
    4: 'D44', 
    5: 'D01',
    6: 'D11',
    7: 'D50',
    8: 'D43', 
    9: 'D0w0',

}

class YOLOVideoDetector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLO Video Detection")
        self.setWindowOpacity(0.95)
        self.setGeometry(100, 100, 1000, 600)  
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(10)  # Set spacing between widgets

        self.video_label = QLabel(self)
        self.layout.addWidget(self.video_label, alignment=Qt.AlignCenter)

        self.detect_button = QPushButton("Detect Objects", self)
        self.detect_button.clicked.connect(self.detect_objects)
        self.layout.addWidget(self.detect_button, alignment=Qt.AlignCenter)

        self.D00_count_label = QLabel("D00: 0", self)
        self.D00_count_label.setVisible(False)
        self.D00_count_label.setObjectName("cl")
        self.layout.addWidget(self.D00_count_label, alignment=Qt.AlignCenter)

        self.D40_count_label = QLabel("D40: 0", self)
        self.D40_count_label.setVisible(False)
        self.D40_count_label.setObjectName("pl")
        self.layout.addWidget(self.D40_count_label, alignment=Qt.AlignCenter)

        self.D10_count_label = QLabel("D10: 0", self)
        self.D10_count_label.setVisible(False)
        self.D10_count_label.setObjectName("pl")
        self.layout.addWidget(self.D10_count_label, alignment=Qt.AlignCenter)

        self.D20_count_label = QLabel("D20: 0", self)
        self.D20_count_label.setVisible(False)
        self.D20_count_label.setObjectName("pl")
        self.layout.addWidget(self.D20_count_label, alignment=Qt.AlignCenter)

        self.D44_count_label = QLabel("D44: 0", self)
        self.D44_count_label.setVisible(False)
        self.D44_count_label.setObjectName("pl")
        self.layout.addWidget(self.D44_count_label, alignment=Qt.AlignCenter)

        self.D01_count_label = QLabel("D01: 0", self)
        self.D01_count_label.setVisible(False)
        self.D01_count_label.setObjectName("pl")
        self.layout.addWidget(self.D01_count_label, alignment=Qt.AlignCenter)

        self.D11_count_label = QLabel("D11: 0", self)
        self.D11_count_label.setVisible(False)
        self.D11_count_label.setObjectName("pl")
        self.layout.addWidget(self.D11_count_label, alignment=Qt.AlignCenter)

        self.D50_count_label = QLabel("D50: 0", self)
        self.D50_count_label.setVisible(False)
        self.D50_count_label.setObjectName("pl")
        self.layout.addWidget(self.D50_count_label, alignment=Qt.AlignCenter)

        self.D43_count_label = QLabel("D43: 0", self)
        self.D43_count_label.setVisible(False)
        self.D43_count_label.setObjectName("pl")
        self.layout.addWidget(self.D43_count_label, alignment=Qt.AlignCenter)

        self.D0w0_count_label = QLabel("D0w0: 0", self)
        self.D0w0_count_label.setVisible(False)
        self.D0w0_count_label.setObjectName("pl")
        self.layout.addWidget(self.D0w0_count_label, alignment=Qt.AlignCenter)

        self.Maintanance_label = QLabel("Mainatenance Status: Normal", self)
        self.Maintanance_label.setVisible(False)
        self.layout.addWidget(self.Maintanance_label, alignment=Qt.AlignCenter)

        self.model = YOLO(r'D:\YoloUI\best.pt')


        self.video_path = ""  # Store the selected video path
        self.cap = cv2.VideoCapture()
        with open("Styles/style.css", "r") as f:
            self.setStyleSheet(f.read())
    
    def load_frame(self, frame):
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        q_pixmap = QPixmap.fromImage(q_image)
        self.video_label.setPixmap(q_pixmap.scaledToWidth(800))
        self.video_label.setAlignment(Qt.AlignCenter)

    def update_count_labels(self, class_counts):
        
        self.D00_count_label.setText(f"D00 Count: {class_counts['_D00']}")
        self.D10_count_label.setText(f"D40 Count: {class_counts['_D10']}")
        self.D20_count_label.setText(f"D20 Count: {class_counts['_D20']}")
        self.D44_count_label.setText(f"D44 Count: {class_counts['_D44']}")
        self.D01_count_label.setText(f"D01 Count: {class_counts['_D01']}")
        self.D11_count_label.setText(f"D11 Count: {class_counts['_D11']}")
        self.D50_count_label.setText(f"D50 Count: {class_counts['_D50']}")
        self.D43_count_label.setText(f"D43 Count: {class_counts['_D43']}")
        self.D0w0_count_label.setText(f"D0w0 Count: {class_counts['_D0w0']}")



        counts={'D00':0, 'D40':0, 'D10':0, 'D20':0, 'D44':0, 'D01':0, 'D11':0, 'D50':0, 'D43':0, 'D0w0':0}

        status=sum(counts.values())
        if status <= 3:
            self.Maintanance_label.setText(f"Maintainance Status: Normal")
            self.Maintanance_label.setStyleSheet("color: green;font-weight: bold")  # Change color to green for Normal
        elif 3 < status <= 5:
            self.Maintanance_label.setText(f"Maintainance Status: Medium")
            self.Maintanance_label.setStyleSheet("color: orange;font-weight: bold")  # Change color to orange for Medium
        else:
            self.Maintanance_label.setText(f"Maintainance Status: High")
            self.Maintanance_label.setStyleSheet("color: red;font-weight: bold")  # Change color to red for High


    def detect_objects(self):
        
        if not self.video_path:
            self.video_path, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mkv)")

        if self.video_path:
            self.cap.open(self.video_path)

          
            self.D00_count_label.setVisible(True)
            self.D40_count_label.setVisible(True)
            self.D10_count_label.setVisible(True)
            self.D20_count_label.setVisible(True)
            self.D44_count_label.setVisible(True)
            self.D01_count_label.setVisible(True)
            self.D11_count_label.setVisible(True)
            self.D50_count_label.setVisible(True)
            self.D43_count_label.setVisible(True)
            self.D0w0_count_label.setVisible(True)
            self.Maintanance_label.setVisible(True)
            self.detect_button.setVisible(False)
            while self.cap.isOpened():
                success, frame = self.cap.read()

                if success:
                    results = self.model(frame, conf=0.25)
                    class_counts = {'D00':0, 'D40':0, 'D10':0, 'D20':0, 'D44':0, 'D01':0, 'D11':0, 'D50':0, 'D43':0, 'D0w0':0}

                    annotated_frame = results[0].plot()

                    for result in results:
                        boxes = result.boxes.numpy()
                        confidences = boxes.conf
                        class_ids = boxes.cls

                        for class_id in class_ids:
                            class_label = class_mapping.get(class_id.item(), 'Unknown')
                            class_counts[class_label] = class_counts.get(class_label, 0) + 1

                    self.update_count_labels(class_counts)

                    rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

                    self.load_frame(rgb_frame)

                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break
                else:
                    break

            self.cap.release()

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YOLOVideoDetector()
    window.setStyleSheet(open("Styles/style.css").read())  # Apply CSS
    window.show()
    sys.exit(app.exec_())
