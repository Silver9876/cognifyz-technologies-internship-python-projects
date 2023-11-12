#febonacci series program
#febonacci series is a series in which the next element is equal to the sum of its previous two elements

#initially the first two numbers will be 0 and 1
num1=0
num2=1
n=int(input("enter the number of terms you want in the palindrome: "))
print(f"{num1}\n{num2}")
for i in range(0,n-2):
    num3=num1+num2
    print(f"{num3}")
    num1=num2
    num2=num3