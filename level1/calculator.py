num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
operator=input("enter the operation you want to perform (+,-,*,/,%): ")

result=0
if operator=="+":
    result=num1+num2
elif operator== "-":
    result= num1-num2
elif operator == "*":
    result = num1*num2
elif operator == "/":
    result=num1/num2
elif operator == "%":
    result = num1%num2
else:
    print("enter a valid opeartor")
    
print(f"the result is: {result}")
    