class Product:
    def __init__(self, name, price, quantity):
        self.name = name

        if price < 0:
            raise ValueError("Цена не может быть отрицательной")

        self.price = price
        self.quantity = quantity


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