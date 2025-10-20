from pizza import PepperoniPizza, BBQPizza, SeafoodPizza
from order import Order

class Terminal:
    COMPANY = "Пиццерия #1"
    ORDER_CANCEL_COMMAND = -1
    ORDER_CONFIRMATION_COMMAND = 0

    def __init__(self):
        self.menu = [PepperoniPizza(), BBQPizza(), SeafoodPizza()]
        self.order = None
        self.display_menu = True

    def __str__(self):
        return f"{Terminal.COMPANY}\nДобро пожаловать"

    def show_menu(self):
        if not self.display_menu:
            return
        print(f"\n{Terminal.COMPANY}\nДобро пожаловать\n")
        print("меню ")
        for i, pizza in enumerate(self.menu, 1):
            print(f"{i}. {pizza}")
        print("для выбора укажите цифру.")
        print(f"для отмены  {Terminal.ORDER_CANCEL_COMMAND}")
        print(f"для подтверждения  {Terminal.ORDER_CONFIRMATION_COMMAND}")
        self.display_menu = False

    def process_command(self, menu_item):
        try:
            menu_item = int(menu_item)
            if menu_item == Terminal.ORDER_CANCEL_COMMAND:
                if self.order is None:
                    print("Заказ не создан")
                else:
                    self.order = None
                    print("аказ отменен")
                    self.display_menu = True
            elif menu_item == Terminal.ORDER_CONFIRMATION_COMMAND:
                if self.order is None or not self.order.ordered_pizzas:
                    print("заказ пуст чето добавьте")
                    self.display_menu = True
                else:
                    print("аказ подтвержен")
                    print(self.order)
                    self.accept_payment()
                    self.order.execute()
                    self.order = None
                    self.display_menu = True
            elif 1 <= menu_item <= len(self.menu):
                if self.order is None:
                    self.order = Order()
                pizza = self.menu[menu_item - 1]
                self.order.add(pizza)
                print(f"пицца {pizza.name} добавлена")
            else:
                raise ValueError
        except ValueError:
            print("не могу распознать команду")
        except Exception:
            print("ошибка терминала")
            self.order = None
            self.display_menu = True

    def calculate_change(self, payment):
        if self.order is None:
            raise ValueError("заказ не создан")
        order_total = self.order.total()
        if payment < order_total:
            raise ValueError("неедостаточно средств для оплаты заказа")
        return payment - order_total

    def accept_payment(self):
        try:
            order_total = self.order.total()
            print(f"сумма заказа: {order_total:.2f} ")
            payment = float(input("введите сумму: "))
            change = self.calculate_change(payment)
            print(f"вы внесли {payment:.2f} Сдача {change:.2f} р.")
        except ValueError as e:
            print(str(e) if str(e) else "Ошибка при вводе суммы")
            raise