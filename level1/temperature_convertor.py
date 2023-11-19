def fahrenhit():
    value = int(input("Enter the temperature: "))
    temp = (value * (9/5)) + 32
    print(f"The temperature in Fahrenheit is: {temp}")

def celceus():
    value = int(input("Enter the temperature: "))
    temp = (value - 32) * (5/9)
    print(f"The temperature in Celsius is: {temp}")

def default():
    print("You didn't choose a valid option.")

print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n")
choice = int(input("Enter your option: "))
cases = {
    1: fahrenhit,
    2: celceus
}

selected_case = cases.get(choice, default)
selected_case()
