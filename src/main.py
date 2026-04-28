from models.product import Product
from models.order import Order


products = [
    Product("iPhone 15 Pro", 120000, 1),
    Product("Samsung S24 Ultra", 95000, 2),
    Product("iPhone 14", 80000, 1),
    Product("Xiaomi 14", 65000, 1),
    Product("Google Pixel 8", 75000, 5)
]

products.sort()
for product in products:
    print(f"Товар: {product.name}; Цена: {product.price} руб.; Количество: {product.quantity}")


# Проверка заказа
p1 = Product('Samsung S24 Ultra', 80000, 5)
p2 = Product('Samsung S24 Ultra', 95000, 2)
print(f"\np1 < p2: {p1<p2}")


# Создание заказа
order = Order(order_id=123, products='Samsung S24 Ultra', total=250000, user="Иван Иванов")
print(f"\n{order}")
