import requests, json, time
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QBoxLayout, QGridLayout, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore


class twojaPogodynka(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.gui()

    def gui(self):

        # widgets
        start = QPushButton("Wprowadź")
        exit = QPushButton("Wyjdź")
        self.cityText = QTextEdit("")
        self.cityText.setPlaceholderText("Wprowadź nazwę miasta...")

        # grid
        grid = QGridLayout()  # ukłąd tabelaryczny czyli tabelkowy
        grid.addWidget(start, 0, 0)
        grid.addWidget(exit, 0, 1)
        grid.addWidget(self.cityText, 1, 0)

        # config qt
        self.setLayout(grid)

        self.resize(400, 200)
        self.setMaximumSize(400, 200)
        self.setMinimumSize(400, 200)
        self.setWindowIcon(QIcon('slonce.jpg'))
        self.setWindowTitle("Pogodynka")
        self.show()

        # działanie przyciwsków
        exit.clicked.connect(self.exit)
        start.clicked.connect(self.weatherCheck)

    def exit(self):
        self.close()

    def weatherCheck(self):
        self.city_name = self.cityText.toPlainText()
        print(self.city_name)
        base_link = "http://api.openweathermap.org/data/2.5/weather?"
        api_code = "8be67c8522f9a54d886ea000e8421460"
        localtime = time.asctime(time.localtime(time.time()))

        complete_url = base_link + "appid=" + api_code + "&q=" + self.city_name

        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]

            temp = y["temp"]
            a = x["weather"]
            weather = a[0]["description"]

            b = temp - 273.15
            c = round(b, 2)
            x1 = ("Pogoda w: " + str(self.city_name) + " jest: " + str(c) + "°C oraz " + str(weather))
            print(x1)
            msg = QMessageBox(self)
            msg.setText(x1)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
        else:
            print("City Not Found")
            error = QMessageBox(self)
            error.setWindowTitle("Błąd!")
            error.setText("Błąd nie znaleziono miasta!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = twojaPogodynka()
    sys.exit(app.exec_())
    app.setLayout(grid)
