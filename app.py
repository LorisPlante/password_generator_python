from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from pathlib import Path
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,200,300,100)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        option_layout = QGridLayout()
        self.password_generated = QLineEdit()
        button_layout = QHBoxLayout()
        main_layout.addLayout(option_layout)    
        main_layout.addWidget(self.password_generated)    
        main_layout.addLayout(button_layout)    

        btn_quit = QPushButton("Quitter", self)
        btn_copy = QPushButton("Copier", self)
        btn_generate = QPushButton("Générer", self)
        button_layout.addWidget(btn_quit)
        button_layout.addWidget(btn_copy)
        button_layout.addWidget(btn_generate)

        self.txt_size = QLabel("Taille : 10")
        option_layout.addWidget(self.txt_size, 0, 0)

        self.option_size = QSlider(Qt.Horizontal)
        self.option_size.setMinimum(0)
        self.option_size.setMaximum(24)
        self.option_size.setValue(12)
        option_layout.addWidget(self.option_size, 1, 0)

        self.option_lowercase = QCheckBox("Minuscules")
        option_layout.addWidget(self.option_lowercase, 0, 1)
        self.option_uppercase = QCheckBox("Majuscules")
        option_layout.addWidget(self.option_uppercase, 1, 1)
        self.option_symbols = QCheckBox("Symboles")
        option_layout.addWidget(self.option_symbols, 0, 2)
        self.option_numbers = QCheckBox("Chiffres")
        option_layout.addWidget(self.option_numbers, 1, 2)




        

app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("TextEditor2000")
window.show()

app.exec()

