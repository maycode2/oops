# Base class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Base class: Animal
class Animal:
    def move(self):
        print("The animal moves.")

# Subclass: Dog
class Dog(Animal):
    def move(self):
        print("The dog runs.")

# Subclass: Bird
class Bird(Animal):
    def move(self):
        print("The bird flies.")

# Create instances and call move()
dog = Dog()
dog.move()

bird = Bird()
bird.move()

car = Car()
car.move()

plane = Plane()
plane.move()
