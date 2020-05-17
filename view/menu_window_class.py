import sys
from datetime import datetime
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
        self.table_item_list.cellClicked.connect(self.add_item_to_order)
        self.table_item_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_order_list.cellClicked.connect(self.delete_item_from_order)
        self.btn_order_items.clicked.connect(self.send_order)
        self.btn_menu_cancel.clicked.connect(self.close_menu_window)

    def add_item_to_order(self, row, column):
        print(f'Row: {row}')
        print(f'Column: {column}')
        if self.actual_list_type == ItemType.FOOD:
            self.order_table_list.append(self.food_list[row])
        elif self.actual_list_type == ItemType.DRINK:
            self.order_table_list.append(self.drinks_list[row])
        self.refresh_order_table()

    def delete_item_from_order(self, row, column):
        item = self.table_order_list.item(row, column)
        not_deleted = True
        i = 0
        while (not_deleted):
            if type(self.order_table_list[i]) is DrinkItem and self.order_table_list[i].drink_item_name == item.text():
                self.order_table_list.pop(i)
                not_deleted = False
            elif type(self.order_table_list[i]) is FoodItem and self.order_table_list[i].food_item_name == item.text():
                self.order_table_list.pop(i)
                not_deleted = False
            else:
                i += 1
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

    def get_finally_price(self):
        final_price = 0
        for key, value in self.ordered_dict_for_order_qtable.items():
            key: Union[DrinkItem, FoodItem]
            if type(key) is DrinkItem:
                final_price += int(key.drink_price) * value
            elif type(key) is FoodItem:
                final_price += int(key.food_price) * value
        return final_price

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
        self.label_final_price.setText(str(self.get_finally_price()))

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

    def send_order(self):
        self.sql.execute_command(Operation.INSERT, 'RestaurantOrder',
                                 insertion_value_dict={
                                     'StartTime': str(datetime.today()).split('.')[0].replace('-', '.'), 'EndTime': '',
                                     'Price': str(self.get_finally_price()), 'Making': 1, 'Served': 0,
                                     'Paid': 0})
        order_id = self.sql.execute_command(Operation.SELECT, 'RestaurantOrder', ['RestaurantOrderID'])[-1]
        for key, value in self.ordered_dict_for_order_qtable.items():
            key: Union[DrinkItem, FoodItem]
            if type(key) is DrinkItem:
                print('DrinItem sent')
                self.sql.execute_command(Operation.INSERT, 'RestaurantDrinkOrderItem',
                                         insertion_value_dict={'RestaurantOrderID': str(order_id[0]),
                                                               'DrinkItemID': key.drink_item_id, 'Quantity': value})
            elif type(key) is FoodItem:
                print('FoodItem sent')
                self.sql.execute_command(Operation.INSERT, 'RestaurantFoodOrderItem',
                                         insertion_value_dict={'RestaurantOrderID': str(order_id[0]),
                                                               'FoodItemID': key.food_item_id, 'Quantity': value})
        self.clear_order_table()
        self.clear_item_table_list()
        self.label_final_price.setText('')
        self.ordered_dict_for_order_qtable = {}
        self.order_table_list = []
        self.get_drinks()

    def close_menu_window(self):
        sys.exit()
