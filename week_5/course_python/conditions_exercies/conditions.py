# question 1

age = int(input("Please enter your age:"))

if age < 0 or age > 120 :
    print("Invalid")

elif 0 <= age <= 12 :
    print("Child")

elif 13 <= age <= 17 :
    print("Teen")

else:
    print("Adult")


# question 2 

character = input("Please enter a signal character:").lower()
vowel = ("a","e","i","o","u")

if not character.isalpha():
    print("Invalid")
elif character in vowel:
    print("Vowel")
else:
    print("Consonant")


# question 3

user_age = int(input("Please enter your age:"))
ages = [19,20,21] 

if user_age < 16 :
    print("Rejected")
elif user_age > 18:
    if user_age  in ages:
        print("Permission granted")
    
    else:
        user_vip = input("Do you have a vip card (yes/no):").lower()
        if user_vip == "yes":
            print("Permission granted")
        else:
            print("Rejected")
        
else:
    print("Rejected")


# question 4

password = "123456789"

user_password = input("Please enter your password:")

if user_password == password:
    print("Access Granted")
elif len(user_password) < 8:
    print("Too short")
else:
    print("Wrong password")


# question 5

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

x_min, x_max = 10, 50
y_min, y_max = 20, 80

if x < x_min or x > x_max or y < y_min or y > y_max:
    print("Outside the rectangle")

elif x == x_min or x == x_max or y == y_min or y == y_max:
    print("On the edge")

else:
    print("Inside the rectangle")


# question 6

user_name = input("Please enter your name:")
default_name = "Anonymous"
    
print(f"great to see you here {user_name or default_name}")


# question 8

num1 = int(input("Please enter your first number:"))
num2 = int(input("Please enter your second number:"))
num3 = int(input("Please enter your third number:"))

print((num1 >= 0) + (num2 >= 0)  + (num3 >= 0 ))



# question 10
#1

user_score = int(input("Please enter your score (0 to 100) :"))

print(((90 <= user_score <= 100) and "A") 
      or ((80 <= user_score <= 89) and "B") 
      or ((79 >= user_score >= 70) and "C" ) 
      or(70 > user_score and "F") )

#2
user_score = int(input("Please enter your score (0 to 100) :"))

print((90 <= user_score <= 100) * "A"
      ,(80 <= user_score <= 89) * "B" 
      , (79 >= user_score >= 70) * "C" 
      ,(70 > user_score) * "F" )