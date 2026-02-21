class Animals():
    def __init__(self, name, age, species, habitat):
        self.name = name
        self.age = age
        self.species = species
        self.habitat = habitat

    def make_sound(self):
        print("ovoz chqaryapti.")

    def eat(self):
        print("Ovqatlanyapti")

    def move(self):
        print("harakatlanmoqda")

    def sleep(self):
        print(f"{self.habitat}da uxlaydi")

class Dog(Animals):
    def __init__(self, name, age, habitat, bread, is_trained):
        super().__init__(name, age, "Dog", habitat)
        self.bread = bread
        self.is_trained = is_trained

    def make_sound(self):
        print("vov", "vov")

class Cat(Animals):
    def __init__(self, name, age, habitat, color, is_indoor):
        super().__init__(name, age, "Cat", habitat)
        self.color = color
        self.is_door = is_indoor

    def make_sound(self):
        print("Miyov")

class Bird(Animals):
    def __init__(self, name, age, habitat, can_fly, wing_span):
        super().__init__(name, age, "Bird", habitat)
        self.can_fly = can_fly
        self.wing_span = wing_span

    def make_sound(self):
        print("Chug'ur", "Chug'ur")

class Fish(Animals):
    def __init__(self, name, age, habitat, water_type, tank_size):
        super().__init__(name, age, "Fish", habitat)
        self.water_type = water_type
        self.tank_size = tank_size

    def make_sound(self):
        print("....")

Animals = [
    Dog("Bobik", 3, "hovli", "Ovcharka", True),
    Cat("Mosh", 2, "uy", "oq", True),
    Bird("Qaqu", 1, "qafas", True, "30 sm"),
    Fish("Nemo", 1, "akvarium", "chuchuk", "20L"),
    Dog("Dobbi", 4, "hovli", "Bulldog", False)
]

for a in Animals:
    print(a.name, "-", a.species)
    a.make_sound()
    a.eat()
    a.move()
    a.sleep()
    print("-" * 30)
