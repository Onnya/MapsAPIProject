import os
import sys

import requests

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,  QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.z_value = 10

        uic.loadUi('map.ui', self)
        self.setWindowTitle('Maps API')

        self.render_map()

    def getImage(self):
        map_params = {
            "ll": "37.732504,55.753215",
            "z": f"{self.z_value}",
            "l": "map",
        }
        map_request = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_request, params=map_params)

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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.z_value < 17:
                self.z_value += 1
        elif event.key() == Qt.Key_PageDown:
            if self.z_value > 0:
                self.z_value -= 1
        self.render_map()

    def render_map(self):
        self.getImage()
        self.pixmap = QPixmap(self.map_file)
        self.label.setPixmap(self.pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())