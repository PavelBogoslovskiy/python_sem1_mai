# Задание N1
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"Животное {self.name} издает звук: {self.sound}")


class Cat(Animal):
    def __init__(self, name, sound="мяу", color="серый"):
        super().__init__(name, sound)
        self.color = color

    def make_sound(self):
        print(f"Кот {self.name} цвета {self.color} говорит: {self.sound}")


class Dog(Animal):
    def __init__(self, name, sound="гав", color="коричневый"):
        super().__init__(name, sound)
        self.color = color

    def make_sound(self):
        print(f"Собака {self.name} цвет {self.color} говорит: {self.sound}")


cat = Cat(name="Жорик", color="черный")
dog = Dog(name="Тема")

cat.make_sound()
dog.make_sound()