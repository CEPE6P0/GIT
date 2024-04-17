# 3. Напишите класс "Медицинский прибор", у которого есть атрибуты
# "название", "тип" и "функциональность". Добавьте метод
# "описание_прибора", который будет выводить информацию о медицинском
# приборе в формате "Прибор: [название], Тип: [тип], Функциональность:
# [функциональность]". Создайте объект класса и вызовите метод
# "описание_прибора".

class MedicalDevice:
    def __init__(self, name, type, functionality):
        self.name = name
        self.type = type
        self.functionality = functionality

    def describe_device(self):
        print(f"Прибор: {self.name}, Тип: {self.type}, Функциональность: {self.functionality}")

device = MedicalDevice("Рентгеновский аппарат", "Диагностический", "Визуализация внутренних органов")

device.describe_device()
