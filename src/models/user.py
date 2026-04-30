from models.exceptions import ValidationError


class User:
    def __init__(self, name, email):
        """Инициализация пользователей с полной валидацией"""
        if not name or len(name.strip()) < 2:
            raise ValidationError("Имя пользователя недолжно быть короче 2 символов")

        if "@" not in email or "." not in email.split("@")[1]:
            raise ValidationError("Неверный формат email (требуется @ и домен)")

        self.name = name.strip()
        self._email = email.lower()


    def get_email(self):
        return self._email


    def set_email(self, email):
        if "@" not in email and "." not in email.split("@")[1]:
            return ValidationError("Неверный формат email")
        self._email = email.lower()


    def get_info(self):
        return f"Пользователь: {self.name}; Email: {self._email}"


    def __str__(self):
        return self.name


    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}')"