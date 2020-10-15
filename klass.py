 #!/usr/bin/env python3

class Car ():
    """Здесь должно быть описание класса."""
    def __init__ (self, age, rost, poroda):
        self.age = age
        self.rost = rost
        self.poroda = poroda
    def vivod (self) :
        print("Описание собаки: " + self.poroda) 


my_car = Car (10, 125, "frdog")
my_car.vivod()
