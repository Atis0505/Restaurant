import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

login_reg_ui = r'C:\Users\Attila\PycharmProjects\Restaurant_project\view\login_reg_mainwindow.ui'
form_login, base_login = uic.loadUiType(login_reg_ui)


# order_ui = 'view/order.ui'
# form_order, base_order = uic.loadUiType(order_ui)

# menu_ui = 'view/menu.ui'
# form_menu, base_menu = uic.loadUiType(menu_ui)


class MainWindow(base_login, form_login):
    def __init__(self):
        super(base_login, self).__init__()
        self.setupUi(self)
        self.btn_server.clicked.connect(
            lambda: self.login_into_server(self.username_textbox.text(), self.password_textbox.text()))
        self.btn_client.clicked.connect(
            lambda: self.login_into_client(self.username_textbox.text(), self.password_textbox.text()))
        self.btn_new_reg.clicked.connect(
            lambda: self.new_user_reg(self.new_username_textbox.text(), self.new_password_textbox.text(),
                                      self.new_confirmed_passw_textbox.text()))
        self.btn_login_cancel.clicked.connect(self.close_main_window)
        self.btn_reg_cancel.clicked.connect(self.close_main_window)

    def login_into_server(self, login_user_name: str, login_passw: str):
        query = f'{login_user_name, login_passw}'
        self.connect_to_sql(query)
        print(query)

    def login_into_client(self, login_user_name: str, login_passw: str):
        query = f'{login_user_name, login_passw}'
        self.connect_to_sql(query)
        print(query)

    def new_user_reg(self, login_user_name: str, login_passw: str, confirm_passw: str):
        if login_passw != confirm_passw:
            self.test_printing('Bad login')
        query = f'{login_user_name, login_passw, confirm_passw}'
        self.connect_to_sql(query)
        print(query)

    def close_main_window(self):
        sys.exit()

    def test_printing(self, message: str):
        print(message)

    def connect_to_sql(self, query: str):
        print('Connect to SQL!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
