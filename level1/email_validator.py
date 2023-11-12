email=input("Enter your email: ")

#inorder to check whether a email is valid or not we follow few rules. They are:
#1.the first element of the email must be a alphabet
#2.we must contail only one @ symbol in out email
#3.the . symbol must be at the 3rd or 4th place from the last in our email
#4.the email must not contain any spaces
#5 the email must not contail any uppercase letters and symbols other than @ and .

k,j,d=0,0,0
if len(email)>=6 and email[0].isalpha() :
    
    if("@" in email) and (email.count("@")) and ((email[-4]==".") ^ (email[-3]==".")):
        for i in email:
            if i==i.isspace():
                k=1
            elif i.isalpha():
                if i==i.upper():
                    j==1
            elif i.isdigit():
                continue
            elif i=="_" or i=="." or i=="@":
                continue
            else:
                d=1
        if k==1 or j==1 or d==1:
            print("wrong email")
        else:
            print("right email")
    else:
        print("wrong email")
else:
    print("wrong email")