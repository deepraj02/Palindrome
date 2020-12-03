
#^Palindrome Program in Python

    #$ Normal Method
a=input("Enter Any String:-\t")
if a.lower()==a[::-1].lower():
    print("True,the string is Palindrome")
else:
    print("False,the string is not Palindrome")

    #% Using Lambda
x=input("Enter any String:-\t")
a=lambda p:p.lower()==p[::-1].lower()
print(a(x))