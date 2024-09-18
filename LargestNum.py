n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
n3 = int(input("Enter 3rd number : "))

if n1>n2:
    if n1>n3:
        print("1st number is largest!")
    else:
        print("3rd number is largest!")
if n2>n1:
    if n2>n3:
        print("2nd number is largest!")
    else:
        print("3rd number is largest!")