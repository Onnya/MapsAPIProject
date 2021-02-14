import os
import sys

import requests

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,  QMainWindow
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.getImage()
        uic.loadUi('map.ui', self)
        self.setWindowTitle('Maps API')

        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)

    def getImage(self):
        map_request = "http://static-maps.yandex.ru/1.x/?ll=37.732504%2C55.753215&z=10&l=map"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def closeEvent(self, event):
        os.remove(self.map_file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())