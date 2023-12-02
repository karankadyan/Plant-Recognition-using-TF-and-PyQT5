import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from plant_recognition_model import PlantRecognition


class PlantRecognitionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Plant Recognition App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(420, 420)

        self.predict_button = QPushButton("Predict Plant", self)
        self.predict_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.predict_button.setFixedSize(200, 50)
        self.predict_button.clicked.connect(self.predict_plant)

        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 14)
        self.result_label.setFont(font)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.predict_button)
        self.layout.addWidget(self.result_label)

        self.plant_recognition = PlantRecognition()

    def predict_plant(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp *.jpeg)")

        if image_path:
            predicted_class = self.plant_recognition.predict_plant(image_path)

            pixmap = QPixmap(image_path).scaled(600, 400, Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
            self.image_label.adjustSize()

            self.result_label.setText(f"Prediction: {predicted_class}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    mainWin = PlantRecognitionApp()
    mainWin.show()
    sys.exit(app.exec_())
