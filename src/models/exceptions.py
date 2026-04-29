class SFMShopExceptions(Exception):
    """Базовый класс всех ошибок SFMShop"""
    pass


class ValidationError(SFMShopExceptions):
    """Ошибка валидации данных"""
    pass


class BusinessLogicError(SFMShopExceptions):
    """Ошибка бизнес-логики"""
    pass


class DatabaseError(SFMShopExceptions):
    """Ошибка БД"""
    pass


class NegativePriceError(ValidationError):
    """Отрицательная цена"""
    def __init__(self, price: float):
        super().__init__(f"Цена {price} не может быть отрицательной!")


class InsufficientStockError(BusinessLogicError):
    """Недостаточно товаров на складе"""
    def __init__(self, product_name: str, available: int, requested: int):
        super().__init__(f"Недостаточно {product_name}: есть {available}, нужно {requested}")


class InvalidOrderError(BusinessLogicError):
    """Невалидный заказ"""
    def __init__(self, reason: str):
        super().__init__(f"Невалидный заказ: {reason}")