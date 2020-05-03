from enum import Enum
from typing import List, Union

from PyQt5.QtWidgets import QTableWidgetItem, QDialog
from qtconsole.qt import QtGui

from controller.sqlite_controller import SqliteController, Operation
from model.drink_item import DrinkItem
from model.food_item import FoodItem
from view.menu_window import Ui_menu_dialog
from view.messagebox_window_class import Messagebox, MessageBoxType


class ItemType(Enum):
    FOOD = 'FOOD'
    DRINK = 'DRINK'


class MenuWindow(QDialog, Ui_menu_dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        super().__init__()
        self.message_box = Messagebox()
        self.drinks_list: List[DrinkItem] = []
        self.food_list: List[FoodItem] = []
        self.order_table_list: List[Union[DrinkItem, FoodItem]] = []
        self.ordered_dict_for_order_qtable: dict = {}
        self.setupUi(self)
        self.actual_list_type = ItemType.DRINK
        self.table_item_list.setRowCount(0)
        self.sql = SqliteController()
        self.get_drinks()
        self.btn_drinks.clicked.connect(self.get_drinks)
        self.btn_food.clicked.connect(self.get_food)
        self.btn_menu.clicked.connect(self.get_menu)
        self.btn_contact.clicked.connect(self.get_contact)
        self.table_item_list.cellClicked.connect(self.add_item_to_order)
        self.table_item_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_order_list.cellClicked.connect(self.delete_item_from_order)

        # self.btn_rendeles_tartalom.clicked.connect(self.get_order_list)

    def add_item_to_order(self, row, column):
        print(f'Row: {row}')
        print(f'Column: {column}')
        if self.actual_list_type == ItemType.FOOD:
            self.order_table_list.append(self.food_list[row])
        elif self.actual_list_type == ItemType.DRINK:
            self.order_table_list.append(self.drinks_list[row])
        self.refresh_order_table()

    def delete_item_from_order(self, row, column):
        self.order_table_list.pop(row)
        self.refresh_order_table()

    def get_drinks(self):
        self.clear_item_table_list()
        self.actual_list_type = ItemType.DRINK
        try:
            rows = self.sql.execute_command(Operation.SELECT, 'DrinkItem', [])
            for index_i, row in enumerate(rows):
                drink_item = DrinkItem(*[str(inf) if type(inf) == int else inf for inf in row])
                if drink_item not in self.drinks_list:
                    self.drinks_list.append(drink_item)
                    self.table_item_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        # self.table_item_list.setItem(index_i, index_j, OwnQTableWidgetItem(text=str(data), index=index_i, db_item=drink_item))
                        self.table_item_list.setItem(index_i, index_j,
                                                     QTableWidgetItem(str(data)))
            self.table_item_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_food(self):
        self.clear_item_table_list()
        self.actual_list_type = ItemType.FOOD
        widget = QTableWidgetItem('Hello')
        try:
            rows = self.sql.execute_command(Operation.SELECT, 'FoodItem', [])
            for index_i, row in enumerate(rows):
                food_item = FoodItem(*[str(inf) if type(inf) == int else inf for inf in row])
                if food_item not in self.food_list:
                    self.food_list.append(food_item)
                    self.table_item_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_item_list.setItem(index_i, index_j, QTableWidgetItem(str(data)))
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_menu(self):
        # drink_list: List[DrinkItem] = []
        # try:
        #     rows = self.sql.execute_command(Operation.SELECT, 'DrinkItemID', [])
        #     for index_i, row in enumerate(rows):
        #         self.table_item_list.insertRow(index_i)
        #         for index_j, data in enumerate(row):
        #             if data == None:
        #                 data = ''
        #             self.table_item_list.setItem(index_i, index_j, QTableWidgetItem(str(data)))
        # except Exception as e:
        #     self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)
        pass

    def get_contact(self):
        pass

    def refresh_order_table(self):
        self.clear_order_table()
        self.collect_order_items_into_ordered_list()
        for index_i, key_element in enumerate(self.ordered_dict_for_order_qtable.keys()):
            key_element: Union[DrinkItem, FoodItem]
            self.table_order_list.insertRow(index_i)
            if type(key_element) == DrinkItem:
                self.table_order_list.setItem(index_i, 0, QTableWidgetItem(key_element.drink_item_name))
                self.table_order_list.setItem(index_i, 1,
                                              QTableWidgetItem(str(self.ordered_dict_for_order_qtable[key_element])))
                self.table_order_list.setItem(index_i, 2, QTableWidgetItem(
                    str(int(key_element.drink_price) * self.ordered_dict_for_order_qtable[key_element])))
            elif type(key_element) == FoodItem:
                self.table_order_list.setItem(index_i, 0, QTableWidgetItem(key_element.food_item_name))
                self.table_order_list.setItem(index_i, 1,
                                              QTableWidgetItem(str(self.ordered_dict_for_order_qtable[key_element])))
                self.table_order_list.setItem(index_i, 2, QTableWidgetItem(
                    str(int(key_element.food_price) * self.ordered_dict_for_order_qtable[key_element])))
        self.table_order_list.resizeColumnsToContents()

    def clear_order_table(self):
        while (self.table_order_list.rowCount() > 0):
            {
                self.table_order_list.removeRow(0)
            }

    def clear_item_table_list(self):
        while (self.table_item_list.rowCount() > 0):
            {
                self.table_item_list.removeRow(0)
            }
        self.drinks_list = []
        self.food_list = []

    def collect_order_items_into_ordered_list(self):
        self.ordered_dict_for_order_qtable = {}
        for order_item in self.order_table_list:
            if self.ordered_dict_for_order_qtable:
                if order_item in self.ordered_dict_for_order_qtable.keys():
                    self.ordered_dict_for_order_qtable[order_item] = self.ordered_dict_for_order_qtable[order_item] + 1
                else:
                    self.ordered_dict_for_order_qtable[order_item] = 1
            else:
                self.ordered_dict_for_order_qtable[order_item] = 1
        print('OK')
