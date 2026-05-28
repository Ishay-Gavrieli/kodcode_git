# question 1
class Animal:
    def speak():
        return "..."
    
class Dog(Animal):
    def speak():
        return "woof"
  
# question 2

class Vehicle:
    def describe():
        return "a vehicle"
    
class Car(Vehicle):
    pass



# question 3
class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self, name,school):
        super().__init__(name)
        self.school = school
 

# question 4

class Logger:
    def log(self,msg):
        return msg
    
class TimeLogger(Logger):
    def log(self,msg):
        return ["time"] + super().log(msg)
    

# question 5
import math
class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius
        

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height) / 2
    

def total_area(shapes):
    return sum(shape.area() for shape in shapes)


my_shapes = [
    Square(side=4),        
    Circle(radius=3),    
    Triangle(base=6, height=4) 
]


# question 6
class Cat:
    def speak(self):
        return ""

class Duck:
    def speak(self):
        return "1"
    
def make_them_speak(animals):
    return [animal.speak() for animal in animals]


# question 7

class Animal:
    def __init__(self,eat,drink):
        self.eat = eat
        self.drink = drink 

class Mammal(Animal):
    def __init__(self,eat,drink,sea):
        super().__init__(eat,drink)
        self.sea  = sea

class Dog(Mammal):
    def __init__(self,eat,drink,sea,bark):
        super().__init__(eat,drink,sea)
        self.bark = bark



# question 8
class Animal:
    pass
class Mammal(Animal):
    pass
class Dog(Mammal):
    pass


def count_dogs(animals):
    count = 0
    for animal in animals:
        if isinstance(animal, Dog):
            count += 1
    return count

zoo = [
    Dog(),  
    Dog(), 
    Animal(), 
    Dog()
]


dog_count = count_dogs(zoo)

print(f"Number of dogs found: {dog_count}")



# question 9
class Shape:
    def __str__(self):
        return "Generic Shape"

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def __str__(self):
        return f"Square with side length {self.side}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def __str__(self):
        return f"Circle with radius {self.radius}"

shapes_list = [Square(4), Circle(5), Shape(), Square(10)]

for shape in shapes_list:
    print(shape)


# question 10
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Cash."

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Credit/Debit Card."

cash = CashPayment()
card = CardPayment()

print(cash.pay(50))  
print(card.pay(100))

try:
    invalid_payment = Payment()
except TypeError as e:
    print(f"Error caught successfully!\nException message: {e}")