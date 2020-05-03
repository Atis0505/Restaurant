from PyQt5.QtWidgets import QDialog
from qtpy import uic

from view.messagebox_window_class import Messagebox
from view.server_window import Ui_server_window

server_ui = r'C:\Users\Attila\PycharmProjects\Restaurant_project\view\server_window.ui'
form_server, base_server = uic.loadUiType(server_ui)


class ServerWindow(QDialog, Ui_server_window):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        # super(base_server, self).__init__()
        super().__init__()
        self.setupUi(self)
        self.message_box = Messagebox()
        # self.server_tabwidget.currentChanged.connect(self.tab_changing)
