"""
Создаём родительский класс
"""
class Product:
    def __init__(self, name, price, discount_rate):
        self.name = name
        self._price = price
        self._discount_rate = discount_rate


    @property
    def price(self):
        return f"Цена без изменений: {self._price:.2f} руб."


    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ошибка: цена не может быть отрицательной")
        self._price = value


    @property
    def discount_rate(self):
        return f"Скидка на товар: {self._discount_rate * 100}%"


    @discount_rate.setter
    def discount_rate(self, value):
        if not 0 <= value <= 1:
            raise ValueError("Скидка только 0-100%")
        self._discount_rate = value


    @property
    def finnaly_price(self):
        discounted = round(self._price * (1 - self._discount_rate), 2)
        return f"Цена со скидкой: {discounted:.2f} руб."


laptop = Product("Ноутбук", 50_000, 0.1)


print(
    laptop.price,
    laptop.discount_rate,
    laptop.finnaly_price,
    sep='\n'
    )

print()

laptop.discount_rate = 0.5
print(
    laptop.price,
    laptop.discount_rate,
    laptop.finnaly_price,
    sep='\n'
)

print()

laptop.price = 40_000
laptop.discount_rate = 0.25

print(
    laptop.price,
    laptop.discount_rate,
    laptop.finnaly_price,
    sep='\n'
)
