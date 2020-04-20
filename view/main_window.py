from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

login_ui = ''
form_login, base_login = uic.loadUiType(login_ui)

rendeles_ui = ''
form_rendeles, base_rendeles = uic.loadUiType(rendeles_ui)

menu_ui = ''
form_menu, base_menu = uic.loadUiType(menu_ui)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
