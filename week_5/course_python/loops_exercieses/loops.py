# question 1

i = 0
while i < 10:
    i += 1 
    
    if i == 7:
        break
    if i % 2 == 0:
        continue
        
    print(i)


# question 2

while True:
    user_password = input("Please entre your password:")
    if user_password == "1234":
        print("Welcome")
        break
    print("Try again")


# question 3

products_list = []

while True:
    product_name = input("Please enter your product (type done to exit):").lower()
    if product_name == "done":
        print(products_list)
        break
    products_list.append(product_name)



# question 4

vowels = ["a","e","i","o","u"]
user_string = input("Please enter your string:").lower()

count = 0
for i in user_string:
    if i in vowels:
        count += 1

print(f"There are {count} times vowels in your string")



# question 5

for i in range(1,6):
    for j in range(1,6):
        print(f"{i} * {j} = {i*j}")


# question 6

user_string = input("Please enter your string:")
for i in range(len(user_string)-1,-1,-1):
    print(user_string[i],end="")




# question 7

num = int(input("Please enter your number:"))
count = 0

while num > 0:
    if num % 2 == 0:
        count += 1
    num = num // 10
    
print(count)



# question 8


user_string = input("Please enter your string:")
result = ""

for i in user_string:
    result += i*2

print(result)


# question 9

highest = 0
while True:
    num = int(input("Please enter positive number (0 to exit):"))
    if num > highest:
        highest = num
    elif num == 0:
        break

print(highest)

# question 10
#1
user_string = input("Please enter your string:")
print(user_string.isalnum())

#2
user_string = input("Please enter your string:")
str_flag = True
for i in user_string:
    if not i.isalpha() and not i.isdigit():
        str_flag = False
        break

print(str_flag)
    

# question 11

num = int(input("Please enter your number:"))

result = 0
base_ten = 10

while num > 0:
    result *= base_ten
    result += num % 10
  
    num = num // 10

print(result)



