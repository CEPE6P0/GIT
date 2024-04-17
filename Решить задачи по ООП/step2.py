# 2. Напишите класс "Электронный гаджет", у которого есть атрибуты
# "марка", "модель" и "год_выпуска". Добавьте метод "описание_гаджета",
# который будет выводить информацию об электронном гаджете в формате
# "Гаджет: [марка] [модель], Год выпуска: [год_выпуска]". Создайте объект
# класса и вызовите метод "описание_гаджета".

class ElectronicGadget:
    def __init__(self, brand, model, release_year):
        self.brand = brand
        self.model = model
        self.release_year = release_year

    def describe_gadget(self):
        print(f"Гаджет: {self.brand} {self.model}, Год выпуска: {self.release_year}")

gadget = ElectronicGadget("Apple", "iPhone 14 Pro Max", 2022)

gadget.describe_gadget()
