#!/usr/bin/env python3

class Dog ():
    """Тренируемся в создании классов. Хотя пока всё равно не понимаю зачем"""

    def __init__(self, age=0, rost=0.01, poroda=''):
        self.age = age
        self.rost = rost
        self.poroda = poroda

    def vivod(self):
        print("Собака: " + self.poroda + " рост собаки " + str(self.rost)
              + " см. возраст " + str(self.age) + " лет")


my_car = Dog(10, 125, "Терьер")
my_car.vivod()
