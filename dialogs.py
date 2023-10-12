from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


def confirm(parent):
    #question
    # deux bouttons : oui / non
    # return true / false
    response = QMessageBox.question(parent,
                                    'Confirm',
                                    'Are you sure ?',
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
    return response == QMessageBox.Yes