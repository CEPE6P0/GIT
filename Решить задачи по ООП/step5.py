# 5. Напишите класс "Оптический прибор", у которого есть атрибуты
# "название", "тип" и "мощность". Добавьте метод "описание_прибора",
# который будет выводить информацию об оптическом приборе в формате
# "Прибор: [название], Тип: [тип], Мощность: [мощность]". Создайте объект
# класса и вызовите метод "описание_прибора".

class OpticalDevice:
    def __init__(self, name, type, magnification):
        self.name = name
        self.type = type
        self.magnification = magnification
    def describe_device(self):
        print(f"Прибор: {self.name}, Тип: {self.type}, Мощность: {self.magnification}")

device = OpticalDevice("Микроскоп", "Оптический", "1000x")

device.describe_device()
