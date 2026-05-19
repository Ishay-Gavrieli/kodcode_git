# question 1
count = 0
def bump():
    global count
    count += 1

def value():
    return count

# question 2
def make_counter():
    count = 0
    
    def c():
        nonlocal count 
        count += 1
        return count  

    return c


# question 3
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)


# the output would be :"local","enclosing","global".


# question 4
# it raise typeerror becuse you shadwo the list function by call your variable the same name.
list = [1, 2, 3]
print(list(range(5)))

lst = [1, 2, 3]
print(list(range(5)))

# question 5
# see main.py and mathutils.py


# question 6
# see tools.py


# question 7
import datetime
import datetime as dt
print(datetime.datetime.now())
print(dt.datetime.now())


# question 8
import math as m
def  public_names(m):
    new = [i for i in dir(m) if  i[0] != ("_")]
    return sorted(new)



# question 9
# the bag is happend when you run the function two times its not creat a new list rather it is add to the first list.
def add_item(item, bag=None):
    if bag is None:
        bag = []  
    bag.append(item)
    return bag


# question 10
from geometry import circle
from geometry import rectangle

print(circle.area(5))
print(rectangle.area(4, 6))





