# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_menu_dialog(object):
    def setupUi(self, menu_dialog):
        menu_dialog.setObjectName("menu_dialog")
        menu_dialog.resize(527, 386)
        self.verticalLayoutWidget = QtWidgets.QWidget(menu_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_italok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_italok.setObjectName("btn_italok")
        self.horizontalLayout_3.addWidget(self.btn_italok)
        self.btn_etelek = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_etelek.setObjectName("btn_etelek")
        self.horizontalLayout_3.addWidget(self.btn_etelek)
        self.btn_menu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_3.addWidget(self.btn_menu)
        self.btn_kapcsolat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_kapcsolat.setObjectName("btn_kapcsolat")
        self.horizontalLayout_3.addWidget(self.btn_kapcsolat)
        self.btn_rendeles_tartalom = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_rendeles_tartalom.setObjectName("btn_rendeles_tartalom")
        self.horizontalLayout_3.addWidget(self.btn_rendeles_tartalom)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)

        self.retranslateUi(menu_dialog)
        QtCore.QMetaObject.connectSlotsByName(menu_dialog)

    def retranslateUi(self, menu_dialog):
        _translate = QtCore.QCoreApplication.translate
        menu_dialog.setWindowTitle(_translate("menu_dialog", "Menü"))
        self.btn_italok.setText(_translate("menu_dialog", "Italok"))
        self.btn_etelek.setText(_translate("menu_dialog", "Ételek"))
        self.btn_menu.setText(_translate("menu_dialog", "Napi menü"))
        self.btn_kapcsolat.setText(_translate("menu_dialog", "Kapcsolat"))
        self.btn_rendeles_tartalom.setText(_translate("menu_dialog", "Rendelés"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menu_dialog = QtWidgets.QDialog()
    ui = Ui_menu_dialog()
    ui.setupUi(menu_dialog)
    menu_dialog.show()
    sys.exit(app.exec_())
