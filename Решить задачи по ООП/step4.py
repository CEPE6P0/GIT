# 4. Напишите класс "Растение", у которого есть атрибуты "название",
# "вид" и "возраст". Добавьте метод "описание_растения", который будет
# выводить информацию о растении в формате "Растение: [название], Вид:
# [вид], Возраст: [возраст]". Создайте объект класса и вызовите метод
# "описание_растения".

class Plant:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def describe_plant(self):
        print(f"Растение: {self.name}, Вид: {self.species}, Возраст: {self.age}")

plant = Plant("Роза", "Чайно-гибридная", 5)

plant.describe_plant()