def fact(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * fact(n-1)
    
num = int(input("Enter the number to find the factorial : "))

print(f"The factorial of the number is : {fact(num)}")