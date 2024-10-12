class Animal:
    def __init__(self, name, alive, fed):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name, edible):
        self.name = name
        self.edible = False


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Mammal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name, edible):
        self.name = name
        self.edible = True  # Переопределил edible для фруктов


a1 = Predator("Лев", True, False)
a2 = Mammal("Шимпанзе", True, False)
p1 = Flower("Гладиолус", False)
p2 = Fruit("Яблоко", True)

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
