def fahrenhit():
    value=int(input("enter the temparature: "))
    temp=(value * (9/5)) + 32
    print(f"the temperature in fahrenhit is: {temp}")
    
def celceus():
    value=int(input("enter the temparature: "))
    temp=(value-32)*(5/9)
    print("the temperature in celceus is: ")
    
def default():
    print("you didn't choose the option")

print("1.celcus to fahrenhit\n2.fahrenhit to celceus\n")
choice=int(input("enter your option: "))
cases = {
        1: fahrenhit,
        2: celceus
    }

selected_case = cases.get(choice, default)
selected_case()
