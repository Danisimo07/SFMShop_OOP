from models.user import User
from models.product import Product
from models.order import Order


try:
    product1 = Product("Ноутбук", -50000, 1)
except ValueError as e:
    print(e)


try:
    user1 = User("Иван", "ivanmail.ru")
except ValueError as e:
    print(e)


try:
    product2 = Product("Мышь", 1500, 2)
    product3 = Product("Клавиатура", 3000, 1)
    user2 = User("Пётр", "petr@mail.ru")

    order = Order(user2, [product2, product3], 123)
    print(order)

    print(order.get_product("Монитор"))
except KeyError as e:
    print(e)
