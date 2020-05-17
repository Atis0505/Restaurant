from datetime import datetime
from typing import List, Optional

from PyQt5.QtCore import QTimer, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QLineEdit

from controller.sqlite_controller import SqliteController, Operation
from model.drink_item import DrinkItem
from model.food_item import FoodItem
from model.restaurant_order import RestaurantOrder
from view.messagebox_window_class import Messagebox, MessageBoxType
from view.server_window import Ui_server_window


class ServerWindow(QDialog, Ui_server_window):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        super().__init__()
        self.setupUi(self)
        self.lineEdit_new_item_discount.setValidator(QRegExpValidator(QRegExp("\d+")))
        self.lineEdit_new_item_unitprice.setValidator(QRegExpValidator(QRegExp("\d+")))
        self.selected_order_id = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer_label)
        self.timer.start(1000)
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.get_actual_orders)
        self.refresh_timer.start(30000)
        self.message_box = Messagebox()
        self.sql = SqliteController()
        self.soup_list: List[FoodItem] = []
        self.salad_list: List[FoodItem] = []
        self.meat_list: List[FoodItem] = []
        self.dessert_list: List[FoodItem] = []
        self.fishfood_list: List[FoodItem] = []
        self.coffee_tee_list: List[DrinkItem] = []
        self.soft_drinks_list: List[DrinkItem] = []
        self.beer_list: List[DrinkItem] = []
        self.wein_list: List[DrinkItem] = []
        self.shoot_list: List[DrinkItem] = []
        self.restaurant_order_list: List[RestaurantOrder] = []
        self.get_soups()
        self.get_actual_orders()
        self.comboBox_new_item_type.addItems(['Ételek', 'Italok'])
        self.comboBox_item_types.addItems(['Ételek', 'Italok'])
        self.refresh_category()
        self.refresh_items()
        self.refresh_category_in_new_item_form()
        self.table_orders.cellClicked.connect(self.get_selected_order_details)
        self.server_tabwidget.currentChanged.connect(self.get_selected_tabwidget_on_main)
        self.all_items_tab.currentChanged.connect(self.get_selected_tabwidget_on_secondary)
        self.btn_order_delete.clicked.connect(self.delete_actual_order)
        self.btn_paid.clicked.connect(self.set_paid)
        self.comboBox_item_types.currentTextChanged.connect(self.refresh_category)
        self.comboBox_item_category.currentTextChanged.connect(self.refresh_items)
        self.comboBox_new_item_type.currentTextChanged.connect(self.refresh_category_in_new_item_form)
        self.comboBox_items.currentText.connect(self.get_selected_item_details)
        self.btn_save_new_item.clicked.connect(self.save_new_item)

    def get_selected_tabwidget_on_main(self, index=0):
        if index == 0:
            self.get_actual_orders()
            self.get_soups()
        elif index == 1:
            self.check_status()

    def get_selected_tabwidget_on_secondary(self, index):
        if index == 0:
            self.get_soups()
        elif index == 1:
            self.get_salads()
        elif index == 2:
            self.get_roast_meat()
        elif index == 3:
            self.get_fish_mains()
        elif index == 4:
            self.get_desserts()
        elif index == 5:
            self.get_coffee_tee()
        elif index == 6:
            self.get_soft_drinks()
        elif index == 7:
            self.get_beers()
        elif index == 8:
            self.get_wein()
        elif index == 9:
            self.get_shoots()

    def get_soups(self):
        try:
            soupsID = self.sql.execute_command(Operation.SELECT, main_table_name='FoodCategory',
                                               column_names=['FoodCategoryID'],
                                               where_condition={'FoodCategoryName': 'Levesek'})
            print(soupsID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='FoodItem',
                                            where_condition={'FoodCategory': f"{soupsID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                food_item = FoodItem(*[str(inf) if type(inf) == int else inf for inf in row])
                food_item.food_category_id = 'Levesek'
                if food_item not in self.soup_list:
                    self.soup_list.append(food_item)
                    self.table_soup_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_soup_list.setItem(index_i, index_j,
                                                     QTableWidgetItem(str(data)))
            self.table_soup_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_salads(self):
        try:
            saladsID = self.sql.execute_command(Operation.SELECT, main_table_name='FoodCategory',
                                                column_names=['FoodCategoryID'],
                                                where_condition={'FoodCategoryName': 'Saláták'})
            print(saladsID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='FoodItem',
                                            where_condition={'FoodCategory': f"{saladsID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                food_item = FoodItem(*[str(inf) if type(inf) == int else inf for inf in row])
                food_item.food_category_id = 'Saláták'
                if food_item not in self.salad_list:
                    self.salad_list.append(food_item)
                    self.table_salad_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_salad_list.setItem(index_i, index_j,
                                                      QTableWidgetItem(str(data)))
            self.table_salad_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_roast_meat(self):
        try:
            roast_meatID = self.sql.execute_command(Operation.SELECT, main_table_name='FoodCategory',
                                                    column_names=['FoodCategoryID'],
                                                    where_condition={'FoodCategoryName': 'Sültek'})
            print(roast_meatID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='FoodItem',
                                            where_condition={'FoodCategory': f"{roast_meatID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                food_item = FoodItem(*[str(inf) if type(inf) == int else inf for inf in row])
                food_item.food_category_id = 'Sültek'
                if food_item not in self.meat_list:
                    self.meat_list.append(food_item)
                    self.table_meat_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_meat_list.setItem(index_i, index_j,
                                                     QTableWidgetItem(str(data)))
            self.table_meat_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_fish_mains(self):
        try:
            fish_mainID = self.sql.execute_command(Operation.SELECT, main_table_name='FoodCategory',
                                                   column_names=['FoodCategoryID'],
                                                   where_condition={'FoodCategoryName': 'Halételek'})
            print(fish_mainID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='FoodItem',
                                            where_condition={'FoodCategory': f"{fish_mainID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                food_item = FoodItem(*[str(inf) if type(inf) == int else inf for inf in row])
                food_item.food_category_id = 'Halételek'
                if food_item not in self.fishfood_list:
                    self.fishfood_list.append(food_item)
                    self.table_fishfood_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_fishfood_list.setItem(index_i, index_j,
                                                         QTableWidgetItem(str(data)))
            self.table_fishfood_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_desserts(self):
        try:
            dessertID = self.sql.execute_command(Operation.SELECT, main_table_name='FoodCategory',
                                                 column_names=['FoodCategoryID'],
                                                 where_condition={'FoodCategoryName': 'Desszertek'})
            print(dessertID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='FoodItem',
                                            where_condition={'FoodCategory': f"{dessertID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                food_item = FoodItem(*[str(inf) if type(inf) == int else inf for inf in row])
                food_item.food_category_id = 'Desszertek'
                if food_item not in self.dessert_list:
                    self.dessert_list.append(food_item)
                    self.table_dessert_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_dessert_list.setItem(index_i, index_j,
                                                        QTableWidgetItem(str(data)))
            self.table_dessert_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_coffee_tee(self):
        try:
            coffee_teeID = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkCategory',
                                                    column_names=['DrinkCategoryID'],
                                                    where_condition={'DrinkCategoryName': 'Kávé/Tea'})
            print(coffee_teeID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkItem',
                                            where_condition={'DrinkCategory': f"{coffee_teeID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                drink_item = DrinkItem(*[str(inf) if type(inf) == int else inf for inf in row])
                drink_item.drink_category_id = 'Kávé/Tea'
                if drink_item not in self.coffee_tee_list:
                    self.coffee_tee_list.append(drink_item)
                    self.table_coffee_tee_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_coffee_tee_list.setItem(index_i, index_j,
                                                           QTableWidgetItem(str(data)))
            self.table_coffee_tee_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_soft_drinks(self):
        try:
            soft_drinkID = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkCategory',
                                                    column_names=['DrinkCategoryID'],
                                                    where_condition={'DrinkCategoryName': 'Üditők'})
            print(soft_drinkID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkItem',
                                            where_condition={'DrinkCategory': f"{soft_drinkID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                drink_item = DrinkItem(*[str(inf) if type(inf) == int else inf for inf in row])
                drink_item.drink_category_id = 'Kávé/Tea'
                if drink_item not in self.soft_drinks_list:
                    self.soft_drinks_list.append(drink_item)
                    self.table_soft_drinks_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_soft_drinks_list.setItem(index_i, index_j,
                                                            QTableWidgetItem(str(data)))
            self.table_soft_drinks_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_beers(self):
        try:
            beerID = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkCategory',
                                              column_names=['DrinkCategoryID'],
                                              where_condition={'DrinkCategoryName': 'Sörök'})
            print(beerID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkItem',
                                            where_condition={'DrinkCategory': f"{beerID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                drink_item = DrinkItem(*[str(inf) if type(inf) == int else inf for inf in row])
                drink_item.drink_category_id = 'Sörök'
                if drink_item not in self.beer_list:
                    self.beer_list.append(drink_item)
                    self.table_beer_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_beer_list.setItem(index_i, index_j,
                                                     QTableWidgetItem(str(data)))
            self.table_beer_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_wein(self):
        try:
            weinID = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkCategory',
                                              column_names=['DrinkCategoryID'],
                                              where_condition={'DrinkCategoryName': 'Borok'})
            print(weinID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkItem',
                                            where_condition={'DrinkCategory': f"{weinID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                drink_item = DrinkItem(*[str(inf) if type(inf) == int else inf for inf in row])
                drink_item.drink_category_id = 'Borok'
                if drink_item not in self.wein_list:
                    self.wein_list.append(drink_item)
                    self.table_wein_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_wein_list.setItem(index_i, index_j,
                                                     QTableWidgetItem(str(data)))
            self.table_wein_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_shoots(self):
        try:
            shootID = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkCategory',
                                               column_names=['DrinkCategoryID'],
                                               where_condition={'DrinkCategoryName': 'Tömények'})
            print(shootID[0][0])
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='DrinkItem',
                                            where_condition={'DrinkCategory': f"{shootID[0][0]}"})
            pass
            for index_i, row in enumerate(rows):
                drink_item = DrinkItem(*[str(inf) if type(inf) == int else inf for inf in row])
                drink_item.drink_category_id = 'Tömények'
                if drink_item not in self.shoot_list:
                    self.shoot_list.append(drink_item)
                    self.table_shoot_list.insertRow(index_i)
                    for index_j, data in enumerate(row):
                        if data == None:
                            data = ''
                        self.table_shoot_list.setItem(index_i, index_j,
                                                      QTableWidgetItem(str(data)))
            self.table_shoot_list.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)
        self.table_shoot_list.resizeColumnsToContents()

    def update_timer_label(self):
        self.label_actual_time.setText(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))

    def get_actual_orders(self):
        try:
            rows = self.sql.execute_command(Operation.SELECT, main_table_name='RestaurantOrder')
            del self.restaurant_order_list[:]
            self.clear_orders_table()
            for index_i, row in enumerate(rows):
                restaurant_order = RestaurantOrder(*[inf for inf in row])
                self.restaurant_order_list.append(restaurant_order)
                self.table_orders.insertRow(index_i)
                self.table_orders.setItem(index_i, 0, QTableWidgetItem(str(restaurant_order.restaurant_order_id)))
                self.table_orders.setItem(index_i, 1, QTableWidgetItem(restaurant_order.start_time))
                self.table_orders.setItem(index_i, 2, QTableWidgetItem(restaurant_order.end_time))
                self.table_orders.setItem(index_i, 3, QTableWidgetItem(str(restaurant_order.price)))
                if restaurant_order.paid == 0:
                    if restaurant_order.making == 1 and restaurant_order.served == 0:
                        self.table_orders.setItem(index_i, 4, QTableWidgetItem('Készül'))
                    if restaurant_order.making == 0 and restaurant_order.served == 1:
                        self.table_orders.setItem(index_i, 4, QTableWidgetItem('Felszolgálva'))
                    self.table_orders.setItem(index_i, 5, QTableWidgetItem('Nincs fizetve'))
                else:
                    self.table_orders.setItem(index_i, 4, QTableWidgetItem('Végzett'))
                    self.table_orders.setItem(index_i, 5, QTableWidgetItem('Fizetve'))
            self.table_orders.resizeColumnsToContents()
        except Exception as e:
            self.message_box.window_execution(f'Hiba a tábla feltöltésénél: \n{e}', MessageBoxType.ERROR)

    def get_selected_order_details(self, row=None, column=None):
        self.clear_item_table_list()
        if not row:
            row = 0
        if self.table_orders.item(row, 0):
            self.selected_order_id = self.table_orders.item(row, 0).text()
            drink_tuple_list = self.sql.execute_command(Operation.SELECT, main_table_name='RestaurantDrinkOrderItem',
                                                        where_condition={'RestaurantOrderID': str(
                                                            self.table_orders.item(row, 0).text())})
            drink_itemID_count_pairs = [tuple(y for y in x[2:]) for x in drink_tuple_list]
            food_tuple_list = self.sql.execute_command(Operation.SELECT, main_table_name='RestaurantFoodOrderItem',
                                                       where_condition={'RestaurantOrderID': str(
                                                           self.table_orders.item(row, 0).text())})
            food_itemID_count_pairs = [tuple(y for y in x[2:]) for x in food_tuple_list]
            self.label_order_id.setText(self.selected_order_id)
            self.label_order_status.setText(self.table_orders.item(row, 4).text())
            self.label_result.setText(self.table_orders.item(row, 3).text())
            self.label_order_time.setText(self.table_orders.item(row, 1).text())
            self.check_status()

            for index, tuple_data in enumerate(drink_itemID_count_pairs):
                self.table_order_details.insertRow(index)
                drink_obj = DrinkItem(*list(self.sql.execute_command(Operation.SELECT, main_table_name='DrinkItem',
                                                                     where_condition={
                                                                         'DrinkItemID': str(tuple_data[0])})[0]))
                self.table_order_details.setItem(index, 0, QTableWidgetItem(str(tuple_data[1])))
                self.table_order_details.setItem(index, 1, QTableWidgetItem(drink_obj.drink_item_name))
                self.table_order_details.setItem(index, 2, QTableWidgetItem(str(drink_obj.drink_price * tuple_data[1])))

            for index, tuple_data in enumerate(food_itemID_count_pairs):
                shifted_index = index + len(drink_itemID_count_pairs)
                self.table_order_details.insertRow(shifted_index)
                food_obj = FoodItem(*list(self.sql.execute_command(Operation.SELECT, main_table_name='FoodItem',
                                                                   where_condition={'FoodItemID': str(tuple_data[0])})[
                                              0]))
                self.table_order_details.setItem(shifted_index, 0, QTableWidgetItem(str(tuple_data[1])))
                self.table_order_details.setItem(shifted_index, 1, QTableWidgetItem(food_obj.food_item_name))
                self.table_order_details.setItem(shifted_index, 2,
                                                 QTableWidgetItem(str(food_obj.food_price * tuple_data[1])))

    def clear_item_table_list(self):
        while (self.table_order_details.rowCount() > 0):
            {
                self.table_order_details.removeRow(0)
            }

    def clear_orders_table(self):
        while (self.table_orders.rowCount() > 0):
            {
                self.table_orders.removeRow(0)
            }

    def delete_actual_order(self):
        self.sql.execute_command(Operation.DELETE, main_table_name='RestaurantOrder', set_id=self.selected_order_id)
        self.sql.execute_command(Operation.DELETE, main_table_name='RestaurantDrinkOrderItem',
                                 set_id=self.selected_order_id)
        self.sql.execute_command(Operation.DELETE, main_table_name='RestaurantFoodOrderItem',
                                 set_id=self.selected_order_id)
        self.clear_item_table_list()
        self.label_result.setText('-')
        self.label_order_time.setText('-')
        self.label_order_status.setText('-')
        self.label_order_id.setText('-')
        selected_index = None
        for index, order in enumerate(self.restaurant_order_list):
            if order.restaurant_order_id == int(self.selected_order_id):
                selected_index = index
        self.restaurant_order_list.pop(selected_index)
        self.table_orders.removeRow(selected_index)
        self.get_actual_orders()
        self.check_status()

    def set_paid(self):
        self.sql.execute_command(Operation.UPDATE, main_table_name='RestaurantOrder', set_id=self.selected_order_id,
                                 update_value_dict={'Making': '0', 'Served': '0', 'Paid': '1',
                                                    'EndTime': str(datetime.today()).split('.')[0].replace('-', '.')})
        self.label_order_status.setText('Végzett')
        self.get_actual_orders()
        self.check_status()

    def check_status(self):
        if self.label_order_status.text() == 'Végzett' or self.label_order_status.text() == '-':
            self.btn_paid.setEnabled(False)
        else:
            self.btn_paid.setEnabled(True)

    def refresh_category(self):
        if self.comboBox_item_types.currentText() == 'Ételek':
            self.comboBox_item_category.clear()
            self.comboBox_item_category.addItems(self.get_drink_categories())
        elif self.comboBox_item_types.currentText() == 'Italok':
            self.comboBox_item_category.clear()
            self.comboBox_item_category.addItems(self.get_food_categories())

    def refresh_items(self):
        category_id = None
        if self.comboBox_item_types.currentText() == 'Ételek':
            self.comboBox_items.clear()
            self.comboBox_items.addItems(self.get_fooditems_by_category_id(self.comboBox_item_category.currentText()))
        elif self.comboBox_item_types.currentText() == 'Italok':
            self.comboBox_items.clear()
            self.comboBox_items.addItems(self.get_drinkitems_by_category_id(self.comboBox_item_category.currentText()))

    def get_selected_item_details(self):
        pass

    def get_fooditems_by_category_id(self, category_name) -> List[str]:
        food_list = None
        category_id = [id[0] for id in self.sql.execute_command(Operation.SELECT, main_table_name='FoodCategory',
                                                                column_names=['FoodCategoryID'], where_condition={
                'FoodCategoryName': category_name})][0]
        food_list = [name[0] for name in
                     self.sql.execute_command(Operation.SELECT, main_table_name='FoodItem', column_names=['FoodName'],
                                              where_condition={'FoodCategory': category_id})]
        return food_list

    def get_drinkitems_by_category_id(self, category_name) -> List[str]:
        drink_list = None
        category_id = [id[0] for id in self.sql.execute_command(Operation.SELECT, main_table_name='DrinkCategory',
                                                                column_names=['DrinkCategoryID'], where_condition={
                'DrinkCategoryName': category_name})][0]
        drink_list = [name[0] for name in
                      self.sql.execute_command(Operation.SELECT, main_table_name='DrinkItem',
                                               column_names=['DrinkItemName'],
                                               where_condition={'DrinkCategory': category_id})]
        return drink_list

    def get_drink_categories(self) -> List[str]:
        drinks_categories = [name[0] for name in
                             self.sql.execute_command(Operation.SELECT, main_table_name='FoodCategory',
                                                      column_names=['FoodCategoryName'])]
        return drinks_categories

    def get_food_categories(self):
        food_categories = [name[0] for name in
                           self.sql.execute_command(Operation.SELECT, main_table_name='FoodCategory',
                                                    column_names=['FoodCategoryName'])]
        return food_categories

    def refresh_category_in_new_item_form(self):
        if self.comboBox_item_types.currentText() == 'Ételek':
            self.comboBox_new_item_category.clear()
            self.comboBox_new_item_category.addItems(self.get_food_categories())
        elif self.comboBox_item_types.currentText() == 'Italok':
            self.comboBox_new_item_category.clear()
            self.comboBox_new_item_category.addItems(self.get_drink_categories())

    def get_category_id_by_name(self, table_name, cat_name):
        return [id[0] for id in
                self.sql.execute_command(Operation.SELECT, main_table_name=table_name, column_names=[table_name + "ID"],
                                         where_condition={table_name + 'Name': cat_name})][0]

    def save_new_item(self):
        main_table = None
        dict_structure = {}
        if self.check_all_details():
            if self.comboBox_new_item_type.currentText() == 'Ételek':
                main_table = 'FoodItem'
            elif self.comboBox_new_item_type.currentText() == 'Italok':
                main_table = 'DrinkItem'
            if main_table:
                column_names = self.sql.execute_command(Operation.SELECT_COLUMNS, main_table_name=main_table)
            dict_structure = {
                column_names[1]: self.lineEdit_new_item_name.text(),
                column_names[2]: self.lineEdit_new_item_description.text(),
                column_names[3]: self.lineEdit_new_item_unitprice.text(),
                column_names[4]: self.get_category_id_by_name(
                    "FoodCategory" if self.comboBox_new_item_type.currentText() == "Ételek" else "DrinkCategory",
                    self.comboBox_new_item_category.currentText()),
                column_names[5]: self.lineEdit_new_item_discount.text()
            }
            if main_table and dict_structure:
                self.sql.execute_command(Operation.INSERT, main_table_name=main_table,
                                         insertion_value_dict=dict_structure)
                self.set_details_empty(
                    [self.lineEdit_new_item_name, self.lineEdit_new_item_unitprice, self.lineEdit_new_item_description,
                     self.lineEdit_new_item_discount])
        else:
            self.message_box.window_execution("Nincs kitöltve az összes mező!", MessageBoxType.ERROR)

    def check_all_details(self) -> bool:
        if any(self.is_empty([self.lineEdit_new_item_name.text(),
                              self.lineEdit_new_item_unitprice.text(),
                              self.comboBox_new_item_category.currentText(),
                              self.comboBox_new_item_type.currentText(), self.lineEdit_new_item_description.text()])):
            return False
        else:
            return True

    def is_empty(self, texts_list: List[str]) -> Optional[List[bool]]:
        results: List[bool] = []
        if texts_list:
            for text in texts_list:
                if text:
                    results.append(False)
                else:
                    results.append(True)
            return results

    def set_details_empty(self, item_list: List[QLineEdit]):
        for item in item_list:
            item.setText('')
