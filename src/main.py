from typing import List
from models.exceptions import (
    SFMShopExceptions, ValidationError, BusinessLogicError,
    NegativePriceError, InsufficientStockError, InvalidOrderError
)
from models.user import User
from models.product import Product
from models.order import Order


def test_validation_errors():
    """Тест ошибок валидации"""
    try:
        bad_product = Product("Ноутбук", -50_000, 5)
    except NegativePriceError as e:
        print(f"❌ {e}")

    print()


def test_business_logic_errors():
    try:
        laptop = Product("Ноутбук", 50_000, 3)
        laptop.reserve_stock(10)
    except InsufficientStockError as e:
        print(f"❌ {e}")

    print()


def test_order_errors():
    user = User("Иван Иванов", "ivan@test.ru")

    try:
        empty_order = Order(user.name, [], 123)
    except InvalidOrderError as e:
        print(f"❌ {e}")

    print()


def test_successful_flow():
    try:
        # Корректные данные
        user = User("Катя Петрова", "kate@mail.ru")
        laptop = Product("Laptop", 50000, 3)
        mouse = Product("Mouse", 1500, 10)
        keyboard = Product("Keyboard", 3000, 5)

        # Создание заказа
        order = Order(user.name, [laptop, mouse, keyboard], 123)
        print(order.get_summary())

        # Обработка заказа
        success = order.process_order()
        print(f"Статус: {'✅ Успех' if success else '❌ Ошибка'}")

        # Информация
        print(f"{user.get_info()}")

    except SFMShopExceptions as e:
        print(f"❌ SFMShopException ({type(e).__name__}): {e}")
    except Exception as e:
        print(f"💥 Неожиданная ошибка: {e}")


def main():
    """Главная функция - полный тест системы"""
    test_validation_errors()
    test_business_logic_errors()
    test_order_errors()
    test_successful_flow()


if __name__ == "__main__":
    main()
