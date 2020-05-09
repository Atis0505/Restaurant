from typing import List

from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from controller.sqlite_controller import SqliteController, Operation
from model.drink_item import DrinkItem
from model.food_item import FoodItem
from view.messagebox_window_class import Messagebox, MessageBoxType
from view.server_window import Ui_server_window


class ServerWindow(QDialog, Ui_server_window):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        super().__init__()
        self.setupUi(self)
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
        self.get_soups()
        self.server_tabwidget.currentChanged.connect(self.get_selected_tabwidget_on_main)
        self.all_items_tab.currentChanged.connect(self.get_selected_tabwidget_on_secondary)

    def get_selected_tabwidget_on_main(self, index=0):
        if index == 0:
            self.get_actual_orders()
            self.get_soups()
        elif index == 1:
            """Paying tab"""
        elif index == 2:
            self.get_menus()
            """Daily menu tab"""
        elif index == 3:
            """All supplier items tab"""
        elif index == 4:
            """Editing of daily menu tab"""
        elif index == 5:
            """Editing all supplier items tab"""
        elif index == 6:
            """Statistic tab"""

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
