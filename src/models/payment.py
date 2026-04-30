from models.exceptions import ValidationError
from abc import ABC, abstractmethod
from re import fullmatch

"""
Сущность Payment для последующих экземпляров
или дочерних классов
"""
class Payment(ABC):
    def __init__(self, amount: float):
        if amount < 0:
            raise ValidationError("Сумма не может быть отрицательной")
        self._amount = amount


    @property
    def amount(self):
        return self._amount


    @amount.setter
    def validate_amount(self, total: int):
        if total < 0:
            return "❌ Недостаточно средств на балансе"
        self._amount = total


    @abstractmethod
    def process_payment(self) -> str:
        pass


class CardPayment(Payment):
    def __init__(self, amount: float, card_number: str):
        super().__init__(amount)
        self.__card_number = card_number


    # @property
    # def card_number(self):
    #     return self._card_number


    # @card_number.setter
    # def card_number(self, number: str):
    #     if number.isdigit() and len(number) == 16:
    #         return self._card_number
    #     else:
    #         "❌ Невозможно выполнить операцию"


    def process_payment(self) -> str:
        last_4_numbers = self.__card_number[-4:]
        return f"Оплата картой №{last_4_numbers}: {self._amount} руб."


class PayPalPayment(Payment):
    def __init__(self, amount: float, email: str):
        super().__init__(amount)
        self._email = email


    def process_payment(self) -> str:
        pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        validate = fullmatch(pattern, self._email)
        if validate:
            return f"Оплата PayPal ({self._email}): {self._amount} руб."
        else:
            return "❌ Email адрес не валиден"


# card = CardPayment(1000, "123456781234678")
# pay_pal = PayPalPayment(2000, "user@paypal.com")


# payments = [
#     card,
#     pay_pal
# ]

# for payment in payments:
#     result = payment.process_payment()
#     print(result)
