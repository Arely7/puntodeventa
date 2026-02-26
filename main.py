#pip install pyqt6 pyqt6-tools

from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette

class Login(QtWidgets.QMainWindow):
    login_successfull = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui", self)
        self.controller = LoginController(self, self)
        self.apply_theme()

    def apply_theme(self):
        is_dark = self.palette().color(QPalette.ColorRole.Window).lightness() <128
        print(f"Is dark: {is_dark}")

class Sell(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main.ui", self)

class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.sell_window = Sell()
        self.login_window.login_successfull.connect(self.show_main_window)
        #muestra la pantalla
        self.login_window.show()

    def show_main_window(self):
        self.sell_window.show()#Abrir ventana de venta
        self.login_window.close()#Cerrar ventana de login

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())