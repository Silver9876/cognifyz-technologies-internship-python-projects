#palindrom is a string which will be equal to the original string even after the operation of string reversal

str=input("enter the string: ")
str1=""
for i in str:
    str1=i+str1

if(str1==str):
    print("it is a palindrome")
else:
    print("it is not a palindrome")