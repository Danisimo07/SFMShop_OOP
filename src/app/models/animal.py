from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: int = 0):
        self.name = name
        self._weight = weight


    @property
    def weight(self):
        return self._weight


    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Вес не может быть меньше 0")
        self._weight = value


    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def __init__(self, title: str, weight: int):
        super().__init__(title, weight)


    def weight_dog(self) -> str:
        result = self.weight
        return f"Вес собаки {result} кг."


    def make_sound(self):
        return f"Собака {self.name} делает: \"Гав-гав\""


class Cat(Animal):
    def __init__(self, title: str, weight: int):
        super().__init__(title, weight)


    def weight_cat(self) -> str:
        result = super().weight
        return f"Вес кошки/(-та) {result}"


    def make_sound(self):
        return f"Кошка {self.name} делает: \"Мяу\""


dog = Dog("Бобик-ёбик", 34)
cat = Cat("Барсик", 6)

animals = [
    dog,
    cat
]

for animal in animals:
    sound = animal.make_sound()
    print(sound)


print(
    f"Вес собаки \"{dog.name}\" составляет {dog.weight:.2f}",
    f"Вес кошки/(-та) \"{cat.name}\" составляет {cat.weight:.2f} кг.",
    sep='\n'
)
