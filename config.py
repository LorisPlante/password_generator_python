import sys
from PySide6.QtGui import QFont

# print(sys.platform)
# print(sys.version)
# print(sys.version_info)

def getFont():
    if sys.platform == "darwin":
        font = QFont('Monaco', 12)
    elif sys.platform.find("linux") != -1:
        font = QFont('Monospace', 12)
    else:
        font = QFont('Courier New', 12)
    return font