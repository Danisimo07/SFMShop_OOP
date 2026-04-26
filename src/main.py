from models.product import Product
from models.user import User
from models.order import Order


# Создаём пользователя
user = User("Иван Иванов", "ivan@test.ru")


# Создаём товары
laptop = Product("Ноутбук", 50_000, 1)
mouse = Product("Мышь", 1_500, 2)


order = Order(user, [laptop, mouse])

print(
    user.get_info(),
    f"Общая стоимость заказа: {order.calculate_total()}",
    sep='\n'
)
