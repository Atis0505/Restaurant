# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_menu_dialog(object):
    def setupUi(self, menu_dialog):
        menu_dialog.setObjectName("menu_dialog")
        menu_dialog.resize(858, 572)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu_dialog.sizePolicy().hasHeightForWidth())
        menu_dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(menu_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.table_item_list = QtWidgets.QTableWidget(menu_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_item_list.sizePolicy().hasHeightForWidth())
        self.table_item_list.setSizePolicy(sizePolicy)
        self.table_item_list.setObjectName("table_item_list")
        self.table_item_list.setColumnCount(6)
        self.table_item_list.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.table_item_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_item_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_item_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_item_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_item_list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_item_list.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.table_item_list, 7, 0, 1, 4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox_counter = QtWidgets.QSpinBox(menu_dialog)
        self.spinBox_counter.setObjectName("spinBox_counter")
        self.verticalLayout.addWidget(self.spinBox_counter)
        self.btn_add_item = QtWidgets.QPushButton(menu_dialog)
        self.btn_add_item.setObjectName("btn_add_item")
        self.verticalLayout.addWidget(self.btn_add_item)
        self.table_order_list = QtWidgets.QTableWidget(menu_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_order_list.sizePolicy().hasHeightForWidth())
        self.table_order_list.setSizePolicy(sizePolicy)
        self.table_order_list.setObjectName("table_order_list")
        self.table_order_list.setColumnCount(3)
        self.table_order_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_order_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order_list.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.table_order_list)
        self.label_result = QtWidgets.QLabel(menu_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.btn_order_items = QtWidgets.QPushButton(menu_dialog)
        self.btn_order_items.setObjectName("btn_order_items")
        self.verticalLayout.addWidget(self.btn_order_items)
        self.btn_menu_cancel = QtWidgets.QPushButton(menu_dialog)
        self.btn_menu_cancel.setObjectName("btn_menu_cancel")
        self.verticalLayout.addWidget(self.btn_menu_cancel)
        self.gridLayout.addLayout(self.verticalLayout, 7, 5, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_drinks = QtWidgets.QPushButton(menu_dialog)
        self.btn_drinks.setObjectName("btn_drinks")
        self.horizontalLayout_2.addWidget(self.btn_drinks)
        self.btn_food = QtWidgets.QPushButton(menu_dialog)
        self.btn_food.setObjectName("btn_food")
        self.horizontalLayout_2.addWidget(self.btn_food)
        self.btn_menu = QtWidgets.QPushButton(menu_dialog)
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_2.addWidget(self.btn_menu)
        self.btn_contact = QtWidgets.QPushButton(menu_dialog)
        self.btn_contact.setObjectName("btn_contact")
        self.horizontalLayout_2.addWidget(self.btn_contact)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)

        self.retranslateUi(menu_dialog)
        QtCore.QMetaObject.connectSlotsByName(menu_dialog)


    def retranslateUi(self, menu_dialog):
        _translate = QtCore.QCoreApplication.translate
        menu_dialog.setWindowTitle(_translate("menu_dialog", "Menü"))
        item = self.table_item_list.horizontalHeaderItem(0)
        item.setText(_translate("menu_dialog", "ID"))
        item = self.table_item_list.horizontalHeaderItem(1)
        item.setText(_translate("menu_dialog", "Név"))
        item = self.table_item_list.horizontalHeaderItem(2)
        item.setText(_translate("menu_dialog", "Leírás"))
        item = self.table_item_list.horizontalHeaderItem(3)
        item.setText(_translate("menu_dialog", "Kategória"))
        item = self.table_item_list.horizontalHeaderItem(4)
        item.setText(_translate("menu_dialog", "Kiszerelés"))
        item = self.table_item_list.horizontalHeaderItem(5)
        item.setText(_translate("menu_dialog", "Ár"))
        self.btn_add_item.setText(_translate("menu_dialog", "Hozzáad"))
        item = self.table_order_list.horizontalHeaderItem(0)
        item.setText(_translate("menu_dialog", "Név"))
        item = self.table_order_list.horizontalHeaderItem(1)
        item.setText(_translate("menu_dialog", "Darab"))
        item = self.table_order_list.horizontalHeaderItem(2)
        item.setText(_translate("menu_dialog", "Ár"))
        self.btn_order_items.setText(_translate("menu_dialog", "Megrendel"))
        self.btn_menu_cancel.setText(_translate("menu_dialog", "Kilép"))
        self.btn_drinks.setText(_translate("menu_dialog", "Italok"))
        self.btn_food.setText(_translate("menu_dialog", "Ételek"))
        self.btn_menu.setText(_translate("menu_dialog", "Napi menü"))
        self.btn_contact.setText(_translate("menu_dialog", "Kapcsolat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_dialog = QtWidgets.QDialog()
    ui = Ui_menu_dialog()
    ui.setupUi(menu_dialog)
    menu_dialog.show()
    sys.exit(app.exec_())
