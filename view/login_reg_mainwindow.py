# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_reg_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit

# from view.menu_window import Ui_menu_dialog
#
# class Ui_menu(QDialog, Ui_menu_dialog):
#     def __init__(self, parent=None):
#         QDialog.__init__(self, parent)
#         self.setupUi(self)
from controller.sqlite_controller import SqliteController, Operation
from model.config import Config
from view.menu_window_class import MenuWindow
from view.messagebox_window_class import Messagebox, MessageBoxType
from view.server_window_class import ServerWindow


class Ui_login_reg_mainwindow(object):
    def setupUi(self, login_reg_mainwindow):
        login_reg_mainwindow.setObjectName("login_reg_mainwindow")
        login_reg_mainwindow.resize(417, 224)
        self.centralwidget = QtWidgets.QWidget(login_reg_mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_reg_tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.login_reg_tab_widget.setGeometry(QtCore.QRect(10, 0, 401, 221))
        self.login_reg_tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.login_reg_tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.login_reg_tab_widget.setObjectName("login_reg_tab_widget")
        self.tab_login = QtWidgets.QWidget()
        self.tab_login.setObjectName("tab_login")
        self.login_groupbox = QtWidgets.QGroupBox(self.tab_login)
        self.login_groupbox.setGeometry(QtCore.QRect(10, 10, 381, 161))
        self.login_groupbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_groupbox.setObjectName("login_groupbox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.login_groupbox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.username_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.username_label.setObjectName("username_label")
        self.horizontalLayout_4.addWidget(self.username_label)
        self.username_textbox = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username_textbox.setObjectName("username_textbox")
        self.horizontalLayout_4.addWidget(self.username_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.password_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.password_label.setObjectName("password_label")
        self.horizontalLayout_3.addWidget(self.password_label)
        self.password_textbox = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_textbox.setObjectName("password_textbox")
        self.horizontalLayout_3.addWidget(self.password_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_server = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_server.setObjectName("btn_server")
        self.horizontalLayout.addWidget(self.btn_server)
        self.btn_client = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_client.setObjectName("btn_client")
        self.horizontalLayout.addWidget(self.btn_client)
        self.btn_login_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_login_cancel.setObjectName("btn_login_cancel")
        self.horizontalLayout.addWidget(self.btn_login_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.login_reg_tab_widget.addTab(self.tab_login, "")
        self.tab_reg = QtWidgets.QWidget()
        self.tab_reg.setObjectName("tab_reg")
        self.reg_groupbox = QtWidgets.QGroupBox(self.tab_reg)
        self.reg_groupbox.setGeometry(QtCore.QRect(10, 10, 381, 171))
        self.reg_groupbox.setObjectName("reg_groupbox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.reg_groupbox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 371, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.new_username_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.new_username_label.setObjectName("new_username_label")
        self.horizontalLayout_6.addWidget(self.new_username_label)
        self.new_username_textbox = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.new_username_textbox.setObjectName("new_username_textbox")
        self.horizontalLayout_6.addWidget(self.new_username_textbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.new_password_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.new_password_label.setObjectName("new_password_label")
        self.horizontalLayout_9.addWidget(self.new_password_label)
        self.new_password_textbox = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.new_password_textbox.setObjectName("new_password_textbox")
        self.horizontalLayout_9.addWidget(self.new_password_textbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.new_confirmed_passw_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.new_confirmed_passw_label.setObjectName("new_confirmed_passw_label")
        self.horizontalLayout_7.addWidget(self.new_confirmed_passw_label)
        self.new_confirmed_passw_textbox = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.new_confirmed_passw_textbox.setObjectName("new_confirmed_passw_textbox")
        self.horizontalLayout_7.addWidget(self.new_confirmed_passw_textbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_new_reg = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_new_reg.setObjectName("btn_new_reg")
        self.horizontalLayout_8.addWidget(self.btn_new_reg)
        self.btn_reg_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_reg_cancel.setObjectName("btn_reg_cancel")
        self.horizontalLayout_8.addWidget(self.btn_reg_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.login_reg_tab_widget.addTab(self.tab_reg, "")
        login_reg_mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login_reg_mainwindow)
        self.statusbar.setObjectName("statusbar")
        login_reg_mainwindow.setStatusBar(self.statusbar)

        """My code"""
        self.config_object = Config()
        self.client_dialog = MenuWindow()
        self.server_dialog = ServerWindow()
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
        self.btn_client.clicked.connect(
            lambda: self.login_into_client(self.username_textbox.text(), self.password_textbox.text()))
        self.btn_server.clicked.connect(
            lambda: self.login_into_server(self.username_textbox.text(), self.password_textbox.text()))
        self.btn_new_reg.clicked.connect(
            lambda: self.new_user_reg(self.new_username_textbox.text(), self.new_password_textbox.text(),
                                      self.new_confirmed_passw_textbox.text()))

        self.retranslateUi(login_reg_mainwindow)
        self.login_reg_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(login_reg_mainwindow)

    """My methods"""

    def configuration_start(self):
        self.config_object.check_db_folder_exist()

    def login_into_server(self, login_user_name: str, login_passw: str):
        if self.username_textbox.text() != '' or self.password_textbox.text() != '':
            if len(self.sql.execute_command(operation=Operation.SELECT, main_table_name='User',
                                            where_condition={'UserName': login_user_name, 'Password': login_passw,
                                                             'UserID': '1'})) > 0:
                print('Server login done!')
                self.open_server_dialog()
            else:
                self.message_box.window_execution('Hibás jelszó vagy felhasználónév!', MessageBoxType.ERROR)
        else:
            self.message_box.window_execution('Minden mező kitöltése kötelező!', MessageBoxType.ERROR)

    def login_into_client(self, login_user_name: str, login_passw: str):
        if self.username_textbox.text() != '' or self.password_textbox.text() != '':
            if len(self.sql.execute_command(Operation.SELECT, main_table_name='User', where_condition=
            {'UserName': login_user_name, 'Password': login_passw})) > 0:
                print('Client login done!')
                self.open_client_dialog()
            else:
                self.message_box.window_execution('Hibás jelszó vagy felhasználónév!', MessageBoxType.ERROR)
        else:
            self.message_box.window_execution('Minden mező kitöltése kötelező!', MessageBoxType.ERROR)

    def new_user_reg(self, login_user_name: str, login_passw: str, confirm_passw: str):
        if self.new_username_textbox.text() != '' or self.new_confirmed_passw_textbox.text() != '' or self.new_password_textbox.text() != '':
            if login_passw != confirm_passw:
                self.message_box.window_execution('A megadott jelszavak nem egyeznek meg!', MessageBoxType.REGULAR_INFO)
            elif len((self.sql.execute_command(Operation.SELECT, main_table_name='User',
                                               where_condition={'UserName': login_user_name}))) > 0:
                self.message_box.window_execution('Már létező felhasználónév!', MessageBoxType.REGULAR_INFO)
                self.new_username_textbox: QLineEdit()
                self.new_username_textbox.setText('')
            else:
                try:
                    self.sql.execute_command(Operation.INSERT, main_table_name='User', where_condition=
                    {'UserName': login_user_name, 'Password': login_passw})
                    self.message_box.window_execution('Sikeres regisztráció!',
                                                      MessageBoxType.REGULAR_INFO)
                except Exception as e:
                    self.message_box.window_execution(f'Hiba: {e}', MessageBoxType.ERROR)
        else:
            self.message_box.window_execution('Összes mező kitöltése kötelező!', MessageBoxType.ERROR)

    def close_main_window(self):
        sys.exit()

    def exit_program(self):
        sys.exit()

    def open_client_dialog(self):
        self.btn_server.setEnabled(False)
        self.btn_client.setEnabled(False)
        self.password_textbox.setReadOnly(True)
        self.username_textbox.setReadOnly(True)
        self.tab_reg.setEnabled(False)
        self.client_dialog.show()

    def open_server_dialog(self):
        self.btn_server.setEnabled(False)
        self.btn_client.setEnabled(False)
        self.password_textbox.setReadOnly(True)
        self.username_textbox.setReadOnly(True)
        self.tab_reg.setEnabled(False)
        self.server_dialog.show()

    def retranslateUi(self, login_reg_mainwindow):
        _translate = QtCore.QCoreApplication.translate
        login_reg_mainwindow.setWindowTitle(_translate("login_reg_mainwindow", "MainWindow"))
        self.login_groupbox.setTitle(_translate("login_reg_mainwindow", "Már regisztrált felhasználó számára"))
        self.username_label.setText(_translate("login_reg_mainwindow", "Felhasználónév:"))
        self.password_label.setText(_translate("login_reg_mainwindow", "Jelszó:"))
        self.btn_server.setText(_translate("login_reg_mainwindow", "Szerver"))
        self.btn_client.setText(_translate("login_reg_mainwindow", "Kliens"))
        self.btn_login_cancel.setText(_translate("login_reg_mainwindow", "Kilép"))
        self.login_reg_tab_widget.setTabText(self.login_reg_tab_widget.indexOf(self.tab_login),
                                             _translate("login_reg_mainwindow", "Bejelentkezés"))
        self.reg_groupbox.setTitle(_translate("login_reg_mainwindow", "GroupBox"))
        self.new_username_label.setText(_translate("login_reg_mainwindow", "Felhasználónév:"))
        self.new_password_label.setText(_translate("login_reg_mainwindow", "Jelszó: "))
        self.new_confirmed_passw_label.setText(_translate("login_reg_mainwindow", "Jelszó ismét: "))
        self.btn_new_reg.setText(_translate("login_reg_mainwindow", "Regisztráció"))
        self.btn_reg_cancel.setText(_translate("login_reg_mainwindow", "Kilép"))
        self.login_reg_tab_widget.setTabText(self.login_reg_tab_widget.indexOf(self.tab_reg),
                                             _translate("login_reg_mainwindow", "Regisztráció"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login_reg_mainwindow = QtWidgets.QMainWindow()
    ui = Ui_login_reg_mainwindow()
    ui.setupUi(login_reg_mainwindow)
    login_reg_mainwindow.show()
    sys.exit(app.exec_())
