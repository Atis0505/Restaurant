from PyQt5.QtWidgets import QDialog

from controller.sqlite_controller import SqliteController, Operation
from view.messagebox_window_class import Messagebox
from view.server_window import Ui_server_window


class ServerWindow(QDialog, Ui_server_window):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        super().__init__()
        self.setupUi(self)
        self.message_box = Messagebox()
        self.sql = SqliteController()
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
        self.sql.execute_command(Operation.SELECT, 'FoodCategoryID')
        self.sql.execute_command(Operation.SELECT, 'FoodItem', ['FoodCategoryID'])
        pass

    def get_salads(self):
        pass

    def get_roast_meat(self):
        pass

    def get_fish_mains(self):
        pass

    def get_desserts(self):
        pass

    def get_coffee_tee(self):
        pass

    def get_soft_drinks(self):
        pass

    def get_beers(self):
        pass

    def get_wein(self):
        pass

    def get_shoots(self):
        pass
