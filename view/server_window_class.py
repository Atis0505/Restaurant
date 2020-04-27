from qtpy import uic

server_ui = r'C:\Users\Attila\PycharmProjects\Restaurant_project\view\server_window.ui'
form_server, base_server = uic.loadUiType(server_ui)


class ServerWindow(base_server, form_server):
    def __init__(self):
        super(base_server, self).__init__()
        self.setupUi(self)
