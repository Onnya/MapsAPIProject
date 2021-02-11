import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,  QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QIcon


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map.ui', self)
        #self.setWindowIcon(QIcon("icon.png"))
        #self.setWindowTitle('Жёлтые окружности')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())