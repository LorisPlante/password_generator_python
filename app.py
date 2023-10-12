from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
import random


from config import getFont
import dialogs


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
        btn_quit.clicked.connect(self.confirm_exit)

        btn_copy = QPushButton("Copier", self)
        btn_copy.clicked.connect(self.copy)

        btn_generate = QPushButton("Générer", self)
        btn_generate.clicked.connect(self.generate)

        button_layout.addWidget(btn_quit)
        button_layout.addWidget(btn_copy)
        button_layout.addWidget(btn_generate)

        self.txt_size = QLabel("Taille : 8")
        option_layout.addWidget(self.txt_size, 0, 0)

        self.option_size = QSlider(Qt.Horizontal)
        self.option_size.setMinimum(0)
        self.option_size.setMaximum(24)
        self.option_size.setValue(8)
        option_layout.addWidget(self.option_size, 1, 0)

        self.option_lowercase = QCheckBox("Minuscules")
        option_layout.addWidget(self.option_lowercase, 0, 1)
        self.option_uppercase = QCheckBox("Majuscules")
        option_layout.addWidget(self.option_uppercase, 1, 1)
        self.option_symbols = QCheckBox("Symboles")
        option_layout.addWidget(self.option_symbols, 0, 2)
        self.option_numbers = QCheckBox("Chiffres")
        option_layout.addWidget(self.option_numbers, 1, 2)

        self.option_lowercase.setChecked(True)
        self.option_numbers.setChecked(True)

        self.option_size.valueChanged.connect(self.change_size)

        self.setStatusBar(QStatusBar(self))
        self.status = self.statusBar()

        self.generate()


    def confirm_exit(self):
        if dialogs.confirm(self):
            QApplication.quit()

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_generated.text())
        self.status.showMessage("Copié !", 2000)
    
    def generate(self):
        size = self.option_size.value()
        has_lower = self.option_lowercase.isChecked()
        has_upper = self.option_uppercase.isChecked()
        has_symbols = self.option_symbols.isChecked()
        has_numbers = self.option_numbers.isChecked()

        mdp = ""
    
        if has_lower:
            mdp += "azertyuiopqsdfghjkllmwxcvbn"
        if has_upper:
            mdp +="AZERTYUIOPQSDFGHJKLMWXCVBN"
        if has_numbers:
            mdp += "0123456789"
        if has_symbols:
            mdp += "!@#$%^&*()_-+=<>?/"
        if not has_lower and not has_numbers and not has_symbols and not has_upper:
            QMessageBox.critical(self,
                                    'Erreur',
                                    'Aucunes option selectionnez',
                                    QMessageBox.Ok)


        mdp = ''.join(random.choice(mdp) for _ in range(size))
        self.password_generated.setText(mdp)


    def change_size(self):
        value = self.option_size.value()
        self.txt_size.setText("Taille : " + str(value))
    

        

app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("TextEditor2000")
window.show()

app.exec()

