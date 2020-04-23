from qtpy import uic

order_ui = r'C:\Users\Attila\PycharmProjects\Restaurant_project\view\order.ui'
form_order, base_order = uic.loadUiType(order_ui)


class OrderWidnow(base_order, form_order):
    def __init__(self, order_list):
        super(base_order, self).__init__()
        self.order_list = order_list
        self.setupUi(self)
