import time

class Order:
    order_count = 0

    def __init__(self):
        self.ordered_pizzas = []
        Order.order_count += 1
        self.order_number = Order.order_count

    def __str__(self):
        res = f"Заказ №{self.order_number}\n"
        for i, pizza in enumerate(self.ordered_pizzas, 1):
            res += f"{i}. {pizza}\n"
        res += f"Сумма заказа: {self.total():.2f} р."
        return res

    def add(self, pizza):
        self.ordered_pizzas.append(pizza)

    def total(self):
        return sum(pizza.price for pizza in self.ordered_pizzas)

    def execute(self):
        print("Заказ поступил")
        for i, pizza in enumerate(self.ordered_pizzas, 1):
            print(f"{i}. {pizza.name}")
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
        print(f"\nЗаказ №{self.order_number} готов")