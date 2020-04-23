from qtpy import uic

from model.order_status import OrderStatus
from view.order_window_class import OrderWidnow

menu_ui = r'C:\Users\Attila\PycharmProjects\Restaurant_project\view\menu.ui'
form_menu, base_menu = uic.loadUiType(menu_ui)


class MenuWindow(base_menu, form_menu):
    def __init__(self, order_list=None):
        super(base_menu, self).__init__()
        self.order_list: OrderStatus = order_list
        if not order_list:
            self.order_list = OrderStatus([])
        self.setupUi(self)
        self.btn_italok.clicked.connect(self.get_italok)
        self.btn_rendeles_tartalom.clicked.connect(self.get_order_list)

    def get_italok(self):
        self.order_list.add_new_item('cola')
        for index, order in enumerate(self.order_list.get_ordered_list()):
            print(f'index:{index}, item:{order}')

    def get_order_list(self):
        self.main = OrderWidnow(self.order_list)
        self.main.show()
        self.close()
