a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

sign = input("Do you want to '+' ,'-' , '*' , '/' : ")

if sign == '+':
    print(f"The addition of {a} and {b} is : {a+b}")
elif sign == '-':
    print(f"The subtraction of {a} and {b} is : {a-b}")
elif sign == '*':
    print(f"Th multiplication of {a} and {b} is : {a*b}")
elif sign == '/':
    if b!=0:
        print(f"The division of  {a} and {b} is : {a/b}")
    else:
        print("Cannot be divided!")
else:
    print("Invalid choice!")