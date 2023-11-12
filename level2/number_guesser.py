import random

n=int(input("enter the range from 1 to: "))
num=random.randint(1,n)
choice =0
while choice!=num:
    choice=int(input("guess the number: "))
    if choice<num:
        print("you have choosen a lesser number")
    elif choice>num:
        print("you have choosen a greater number")
print("you are right")