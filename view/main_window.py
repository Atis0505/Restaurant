import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLineEdit

from controller.sqlite_controller import SqliteController, Operation
from model.config import Config
from view.menu_window_class import MenuWindow
from view.messagebox_window_class import MessageBoxType, Messagebox
from view.server_window_class import ServerWindow

login_reg_ui = r'C:\Users\Attila\PycharmProjects\Restaurant_project\view\login_reg_mainwindow.ui'
form_login, base_login = uic.loadUiType(login_reg_ui)

class MainWindow(base_login, form_login):
    def __init__(self):
        super(base_login, self).__init__()
        self.setupUi(self)
        self.config_object = Config()
        self.message_box = Messagebox()
        self.btn_server.clicked.connect(
            lambda: self.login_into_server(self.username_textbox.text(), self.password_textbox.text()))
        self.btn_client.clicked.connect(
            lambda: self.login_into_client(self.username_textbox.text(), self.password_textbox.text()))
        self.btn_new_reg.clicked.connect(
            lambda: self.new_user_reg(self.new_username_textbox.text(), self.new_password_textbox.text(),
                                      self.new_confirmed_passw_textbox.text()))
        self.btn_login_cancel.clicked.connect(self.close_main_window)
        self.btn_reg_cancel.clicked.connect(self.close_main_window)
        self.configuration_start()
        self.db_path = self.config_object.get_db_path()
        self.sql = SqliteController()

    def configuration_start(self):
        self.config_object.check_db_folder_exist()

    def login_into_server(self, login_user_name: str, login_passw: str):
        if len(self.sql.execute_command(Operation.SELECT, 'User',
                                        [{'UserName': login_user_name, 'Password': login_passw, 'UserID': '1'}])) > 0:
            print('Server login done!')
            self.main = ServerWindow()
            self.main.show()
            self.close()
        else:
            self.message_box.window_execution('Hibás jelszó vagy felhasználónév!', MessageBoxType.ERROR)

    def login_into_client(self, login_user_name: str, login_passw: str):
        if len(self.sql.execute_command(Operation.SELECT, 'User',
                                        [{'UserName': login_user_name, 'Password': login_passw}])) > 0:
            print('Client login done!')
            self.main = MenuWindow()
            self.main.show()
            self.close()
        else:
            self.message_box.window_execution('Hibás jelszó vagy felhasználónév!', MessageBoxType.ERROR)

    def new_user_reg(self, login_user_name: str, login_passw: str, confirm_passw: str):
        if self.new_username_textbox.text() != '' or self.new_confirmed_passw_textbox.text() != '' or self.new_password_textbox.text() != '':
            if login_passw != confirm_passw:
                self.message_box.window_execution('A megadott jelszavak nem egyeznek meg!', MessageBoxType.REGULAR_INFO)
            elif len((self.sql.execute_command(Operation.SELECT, 'User', [{'UserName': login_user_name}]))) > 0:
                self.message_box.window_execution('Már létező felhasználónév!', MessageBoxType.REGULAR_INFO)
                self.new_username_textbox: QLineEdit()
                self.new_username_textbox.setText('')
            else:
                self.sql.execute_command(Operation.INSERT, 'User',
                                         [{'UserName': login_user_name, 'Password': login_passw}])
                if self.message_box.window_execution('Sikeres regisztráció! Szeretne bejelentkezni?',
                                                     MessageBoxType.QUESTION):
                    self.main = MenuWindow()
                    self.main.show()
                    self.close()
        else:
            self.message_box.window_execution('Összes mező kitöltése kötelező!', MessageBoxType.ERROR)
        # query = f'{login_user_name, login_passw, confirm_passw}'
        # self.connect_to_sql(query)
        # print(query)

    def close_main_window(self):
        sys.exit()


if __name__ == "__main__":
    print(__name__)
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
