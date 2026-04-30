from models.exceptions import InvalidOrderError, BusinessLogicError
from models.product import Product
from models.user import User

class Order:
    def __init__(self, user: User, products: list[Product], order_id: int):
        """Инициализация заказов с полной валидацией"""
        if not user:
            raise InvalidOrderError("Пользователь обязателен")
        
        if not products:
            raise BusinessLogicError("В заказе должны быть товары")

        if not all(isinstance(p, Product) for p in products):
            raise InvalidOrderError("Все элементы должны быть в Product")


        self.user = user
        self.products = products[:]
        self.order_id = order_id
        self.total = self.calculate_total()


    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(f"Ожидался Product, получен {type(product).__name__}")
        if product.quantity == 0:
            raise InvalidOrderError(f"Товара '{product.name}' нет на складе")
        self.products.append(product)
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
            if product.name == product_name:
                return product
        raise KeyError("Товар не найден")


    def get_summary(self) -> str:
        """Краткая сводка заказа"""
        product_names = ", ".join(p.name for p in self.products)
        return f"Заказ #{self.order_id}: {len(self.products)} товаров ({product_names}), {self.total}р"


    def process_order(self) -> bool:
        """Обработка заказов (резервирование товаров)"""
        try:
            for product in self.products:
                product.reserve_stock(1)
            print(f"✅ Заказ #{self.order_id} успешно обработан!")
            return True
        except Exception as e:
            print(f"❌ Ошибка обработки заказа #{self.order_id}: {e}")
            return False


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
