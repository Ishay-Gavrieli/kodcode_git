# question 1

class Student:
    def __init__(self,name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    
# a = Student("ishay")
# print(a.name)


# question 2
class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def erea(self):
        return self._width * self._height
    
    
# a = Rectangle(3,4)
# print(a.erea)


# question 3

class Thermometer:
    def __init__(self,celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
        if value < -273.15:
            raise ValueError
        self._celsius = value

# t  = Thermometer(25)
# print(t.celsius)

# t.celsius = -2000
# print(t.celsius)


# question 4
class BankAccount:
    def __init__(self,balance):
        self._balance = balance

    @property
    def balance(self):
        return f"your balance is {self._balance}"
  

    def deposit(self,amount):
        if amount <= 0 :
            raise ValueError
        self._balance += amount
        return f"Your balance is {self._balance}"
    
    def withdraw(self,amount):
        if amount > self._balance :
            raise ValueError
        if amount <= 0:
            raise ValueError
        self._balance -= amount
        return f"Withdrew {amount}. Remaining balance: {self._balance}"

# a = BankAccount(214)
# print(a.balance)
# a.deposit(5)

# print(a.balance)


# question 5

class Person:
    def __init__(self,first_name,last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


# a = Person("ishay","gavrieli")
# print(a.full_name)


# question 6

class Temperature:
    def __init__(self,celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 1.8 + 32 
    
    @fahrenheit.setter
    def fahrenheit(self,value):
        self._celsius = (value - 32) / 1.8




# question 7

class Calculator:
        
    @staticmethod
    def is_even(n):
        return n % 2 == 0
    
# a = Calculator
# print(a.is_even(4))

# print(Calculator.is_even(5))



# question 8

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls,pair):
        x,y = pair
        return cls(x,y)
    

p = Point.from_tuple((5, 9))

# print(p.x)  
# print(p.y)

# question 9

class User:
    _count = 0

    def __init__(self,username):
        self.username = username

        User._count += 1

    @classmethod
    def hoe_many(cls):
        return cls._count
    
print(User.how_many())

u1 = User("Ishay")
u2 = User("Dana")
u3 = User("Yossi")
print(User.how_many())

# question 10

class Product:
    def __init__(self, name, price):
        self._name = name
        self.price = price 

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError
    
        self._price = value

p = Product("Laptop", 1500)
print(f"item: {p.name}, price: {p.price}")

p.price = 1350
print(p.price)

