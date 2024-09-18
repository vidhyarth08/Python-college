num = int(input("Enter the number to find the factorial : "))

fact=1
if num == 0 or num==1:
    print(f"The factorial of the number is : {num}")

for i in range(1,num+1):
    fact *= i

print(f"The factorial of the number is : {fact}")