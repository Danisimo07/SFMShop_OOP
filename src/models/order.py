from models.product import Product
# from models.user import User

class Order:
    def __init__(self, user: str, products: list[Product], order_id: int):
        self.user = user
        self.products = products
        self.order_id = order_id
        self.total = self.calculate_total()


    def __str__(self):
        return f"Заказ #{self.order_id} на сумму {self.total} руб. (Пользователь: {self.user})"


    def __repr__(self):
        return f"Order(order_id='{self.order_id}', total='{self.total}', user='{self.user}')"


    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_total_price()
        return total


    def get_product(self, product_name):
        for product in self.products:
            if product == product_name:
                return product
        raise KeyError("Товар не найден")


# # Создаём пользователя
# user = User("Иван Иванов", "ivan@test.ru")


# # Создаём товары
# laptop = Product("Ноутбук", 50_000, 1)
# mouse = Product("Мышь", 1_500, 2)


# order = Order(user, [laptop, mouse])

# print(
#     user.get_info(),
#     f"Общая стоимость заказа: {order.calculate_total()}",
#     sep='\n'
# )
