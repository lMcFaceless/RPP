import os

import pandas
import pandas as pd

data = pd.read_csv("data.csv")


class Object:
    def __init__(self, name):
        self.name = name


class Food(Object):  # Наследование от класса Object
    def __init__(self):  # Конструктор
        self.number = None
        self.quantity = None
        self.servTime = None
        self.replaceTime = None
        self.foodLeft = None
        super().__init__(None)

    def __repr__(self):  # Перегрузка стандартной операции repr
        return 'Food({!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(self.number, self.name, self.quantity, self.servTime,
                                                                 self.replaceTime,
                                                                 self.foodLeft)

    def __setattr__(self, key, value):  # метод setattr для заполнения значений полей
        value = value
        self.__dict__[key] = value

    def __iter__(self):  # Итератор
        self.a = 0
        return self

    def __next__(self):  # Часть итератора
        if self.a < len(self.name):
            x = self.a
            self.a += 1
            return self.name[x]
        else:
            raise StopIteration

    def generator(self):  # Генератор
        self.a = 0
        yield self

    def __getitem__(self, key):  # Метод для доступа к элементу коллекции по ключу
        return self.__dict__[key]

    def getQuantity(self):  # Статический метод, вычисляющий кол-во еды
        return self.quantity * self.foodLeft


# food = Food()
# food.name = "name3"
# food.quantity = 100
# food.foodLeft = 30
# print(food.name)
# for i in food:  # Итерация имени объекта food
#     print(i)
# print(food["name"])
# print(food.getQuantity())
foods = []

for i in range(len(data["Number"])):  # Чтение из scv файла
    food = Food()
    food.number = data["Number"][i]
    food.name = data["name"][i]
    food.quantity = data["quantity"][i]
    food.servTime = data["servTime"][i]
    food.replaceTime = data["replaceTime"][i]
    food.foodLeft = data["foodLeft"][i]
    foods.append(food)
print(foods)

names = []
for food in foods:
    names.append(food.name)

print(sorted(names))  # Сортировка по алфавиту

print("Сортировка по количеству, больше 100: ")
for food in foods:
    if food.quantity > 100:
        print(food)

newFood = Food()
newFood.number = len(foods) + 1
newFood.name = "water"
newFood.quantity = 50
newFood.servTime = "2021-07-25 16:17:45.04"
newFood.replaceTime = "2021-07-25 16:18:00.00"
newFood.foodLeft = 30

newRow = [newFood.number, newFood.name, newFood.quantity, newFood.servTime, newFood.replaceTime, newFood.foodLeft]
data.loc[len(data)] = newRow
print(data)
data.to_csv("data.csv", index=False)  # Добавление строки в csv файл
