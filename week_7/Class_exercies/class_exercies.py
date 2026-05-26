# question 1

class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof"
    

 
# question 2

class Rectangle:
    def __init__(self,width,hieght):
        self.width = width
        self.hieght = hieght
    
    def area(self):
        return self.width * self.hieght
        


# question 3

class Counter:
    def __init__(self,start=0):
        self.count = start
    def increasment(self):
        self.count += 1
    def value(self):
        return self.count



# question 4

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} , {self.y}"



# question 5

class BankAccount:
    def __init__(self,balance = 0):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            return "cannot withdraw more than your balance"
        self.balance -= amount


# question 6

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
        
    def to_fahrenheit(self):
        return self.celsius * 2.12 


# question 7

class Student:
    school = "Kodcode" 

    def __init__(self,name):
        self.name = name


# question 8

class Player:
    total = 0

    def __init__(self,players):
        self.players = players
        Player.total += 1


# question 9

class Money:
    def __init__(self,amount):
        self.amount = amount
        
    def is_more_than(self,other):
        return self.amount > other.amount
    

# question 10

class Playlist:
    def __init__(self):
        self.songs = []

    def add(self,title):
        self.songs.append(title)

    def remove(self,title):
        if title in self.songs:
            self.songs.remove(title)

    def count(self):
        return len(self.songs)

    def __str__(self):
        return ",".join(self.songs)
    

