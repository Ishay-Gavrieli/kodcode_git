# question 1


diary = ["hello world" "\n" "this is a beautiful day" "\n" "the date is 5/24/2026""\n"]
with open("diary.txt", 'w', encoding="utf-8")as file:
          file.writelines(diary)
          print("the diray is succesfuly crated")

with open("diary.txt", 'r', encoding="utf-8")as file:
        for line in file:
            print(line.strip())
        



# question 2

def add_entry(filename, date, content):
    with open(filename,"a")as file:
            file.write(date + ":")
            file.write(content)
    
       

add_entry("diary.txt","5/24/26"+"\n","i seccesful finish the exercies "+"\n")


with open("diary.txt", 'r', encoding="utf-8")as file:
        for line in file:
                print(line.strip())


# question 3


def search_diary(filename, keyword):
    with open(filename,"r", encoding="utf-8")as file:
        lst = []
        for line in file:
            if keyword in line:
                print(line)
                lst.append(line)
              
    return lst

import os

def safe_read_diary(filename):
    if os.path.exists(filename):
        with open(filename,"r",encoding= "utf-8")as file:
            for line in file:
                print(line)
    else:
        print("the file does not exists")



