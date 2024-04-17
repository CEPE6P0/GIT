# 1. Напишите класс "Орудие", у которого есть атрибуты "название",
# "материал" и "цена". Добавьте метод "описание_орудия", который будет
# выводить информацию об орудии в формате "Орудие: [название], Материал:
# [материал], Цена: [цена]". Создайте объект класса и вызовите метод
# "описание_орудия".

class Tool:
    def __init__(self, name, material, price):
        self.name = name
        self.material = material
        self.price = price
    def describe_tool(self):
        print(f"Орудие: {self.name}, Материал: {self.material}, Цена: {self.price}")

tool = Tool("Молоток", "Сталь", 1000)

tool.describe_tool()