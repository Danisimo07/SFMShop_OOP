class User:
    def __init__(self, name, email):
        self.name = name

        if "@" not in email:
            raise ValueError("Неверный формат email")

        self.email = email


    def __str__(self):
        return self.name


    def __rerp__(self):
        return f"User(name='{self.name}', email='{self.email}')"


    def get_info(self):
        return f"Пользователь: {self.name}; Email: {self.email}"
