a = int(input("Enter 1st number to swap : "))
b = int(input("Enter 2nd number to swap : "))

print(f"Numbers before swapping : a : {a} , b : {b}")

a=a^b
b=a^b
a=a^b

print(f"Numbers after swapping : a : {a} , b : {b}")