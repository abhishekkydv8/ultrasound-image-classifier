from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ultrasound Image Classifier")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ultrasound Classifier UI Placeholder"))
        self.setLayout(layout)
