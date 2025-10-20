import time

class Pizza:
    def __init__(self):
        self.name = "раготовка"
        self.testo = "тонкое"
        self.sauce = "кечтуп"
        self.nachinkf = []
        self.price = 0

    def __str__(self):
        res = f"пицца: {self.name} | цена: {self.price:.2f} р.\n"
        res += f"тесто: {self.testo} соус: {self.sauce}\n"
        res += f"начинка: {', '.join(self.nachinkf)}"
        return res

    def prepare(self):
        print(f"начинаю готовить пиццу {self.name}")
        time.sleep(1)
        print(f"замешиваю {self.testo} тесто")
        time.sleep(1)
        print(f"добавляю соус: {self.sauce}.")
        time.sleep(1)
        print(f"добавляю{', '.join(self.nachinkf)}")

    def bake(self):
        time.sleep(1)
        print("выпекаю пиццу. готово")

    def cut(self):
        time.sleep(1)
        print("нарезаю")

    def pack(self):
        time.sleep(1)
        print("eпаковываю")

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "gепперони"
        self.testo = "тонкое"
        self.sauce = "томатный"
        self.nachinkf = ["пепперони", "моцарелла"]
        self.price = 110000.00

class BBQPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "барбекю"
        self.testo = "тонкое"
        self.sauce = "барбекю"
        self.nachinkf = ["бекон", "ветчинв", "петрушка", "моцарелла"]
        self.price = 1100.00

class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Дары моря"
        self.testo = "пышное"
        self.sauce = "тар-тар"
        self.nachinkf = ["кальмари", "кревети", "миди", "моцарелла"]
        self.price = 1000.00