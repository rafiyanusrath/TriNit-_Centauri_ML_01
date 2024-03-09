from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from ultralytics import YOLO
import cv2
from PIL import Image

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

class YOLODetector_Image(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YOLO Object Detection")
        self.setGeometry(100, 100, 1000, 600)  

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        self.result_label = QLabel(self)
        self.layout.addWidget(self.result_label, alignment=Qt.AlignCenter)

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

        self.model = YOLO(r'C:/Users/takhiuddin/Hackathon/H7/YoloUI (1)/best.pt')


        with open("Styles/styleimg.css", "r") as f:
            self.setStyleSheet(f.read())
    
    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap.scaledToWidth(800))  
        self.image_label.setAlignment(Qt.AlignCenter)

    def detect_objects(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.load_image(file_path)
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
            results = self.model(file_path)

            image_np = cv2.imread(file_path)

            _D00 = 0
            _D40 = 0
            _D10 = 0
            _D20 = 0
            _D44 = 0
            _D01 = 0
            _D11 = 0
            _D50 = 0
            _D43 = 0
            _D0w0 = 0


            for result in results:
                boxes = result.boxes.numpy()
                confidences = boxes.conf
                class_ids = boxes.cls

                for box, confidence, class_id in zip(boxes.xyxy, confidences, class_ids):
                    box = [int(coord) for coord in box]
                    class_label = class_mapping.get(class_id.item(), 'Unknown')
                    cv2.rectangle(image_np, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 4)
                    cv2.putText(image_np, f'{class_label} {confidence.item():.2f}', (box[0], box[1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 4)

                    if class_label == 'D00':
                        _D00 += 1
                    elif class_label == 'D40':
                        _D40 += 1
                    elif class_label == 'D10':
                        _D10 += 1
                    elif class_label == 'D20':
                        _D20 += 1
                    elif class_label == 'D44':
                        _D44 += 1
                    elif class_label == 'D01':
                        _D01 += 1
                    elif class_label == 'D11':
                        _D11 += 1
                    elif class_label == 'D50':
                        _D50 += 1
                    elif class_label == 'D43':
                        _D43 += 1
                    elif class_label == 'D0w0':
                        _D0w0 += 1

            # Display the image with bounding boxes
            result_image = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
            result_pixmap = self.convert_image_to_pixmap(result_image)
            self.result_label.setPixmap(result_pixmap.scaledToWidth(800))  
            self.result_label.setAlignment(Qt.AlignCenter)

            self.D00_count_label.setText(f"D00 Count: {_D00}")
            self.D10_count_label.setText(f"D40 Count: {_D10}")
            self.D20_count_label.setText(f"D20 Count: {_D20}")
            self.D44_count_label.setText(f"D44 Count: {_D44}")
            self.D01_count_label.setText(f"D01 Count: {_D01}")
            self.D11_count_label.setText(f"D11 Count: {_D11}")
            self.D50_count_label.setText(f"D50 Count: {_D50}")
            self.D43_count_label.setText(f"D43 Count: {_D43}")
            self.D0w0_count_label.setText(f"D0w0 Count: {_D0w0}")


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

    def convert_image_to_pixmap(self, image):
        img_data = image.tobytes()
        width, height = image.size[0], image.size[1]

        q_image = QImage(img_data, width, height, QImage.Format_RGB888)
        q_pixmap = QPixmap.fromImage(q_image)

        return q_pixmap
