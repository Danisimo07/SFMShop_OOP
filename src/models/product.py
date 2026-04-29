from models.exceptions import NegativePriceError, InsufficientStockError


class Product:
    def __init__(self, name, price, quantity):
        self.name = name

        if price < 0:
            raise NegativePriceError("Цена не может быть отрицательной")

        if quantity < 0:
            raise NegativePriceError

        self.price = price
        self.quantity = quantity


    def reserve_stock(self, requested_quantity: int):
        """Резервирует количество товара"""
        if requested_quantity > self.quantity:
            raise InsufficientStockError(
                self.name,
                self.quantity,
                requested_quantity
            )

        self.quantity -= requested_quantity


    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return True if self.price < other.price else False


    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price


    def get_total_price(self):
        return self.price * self.quantity