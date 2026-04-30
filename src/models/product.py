from models.exceptions import (NegativePriceError, InsufficientStockError, ValidationError)


class Product:
    def __init__(self, name, price, quantity):
        if quantity < 0:
            raise NegativePriceError

        self.name = name
        self.price = price
        self.quantity = quantity


    def set_price(self, price: float) -> float:
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        self.price = price


    def get_total_price(self):
        return self.price * self.quantity


    def reserve_stock(self, requested_quantity: int):
        """Резервирует количество товара"""
        if requested_quantity > self.quantity:
            raise InsufficientStockError(
                self.name,
                self.quantity,
                requested_quantity
            )

        self.quantity -= requested_quantity


    def __str__(self):
        return f"Товар: {self.name}; Цена: {self.price} руб.; Количество: {self.quantity}"


    def __repr__(self):
        return f"Product(name='{self.name}', price='{self.price}', quantity='{self.quantity}')"


    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price


    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price