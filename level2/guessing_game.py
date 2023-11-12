#guessing game
#we have used a random module inorder to choose a random integer

import random
n=random.randint(1,100)
choice=0
while n!=choice:
    choice=int(input("choose a number: "))
    if n>choice:
        print("you have choosen a lesser number")
    elif n<choice:
        print("you have choosen a greater number")
        
print("you are right")