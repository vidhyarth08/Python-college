num1=int(input("Enter the value of dividend : "))
num2 = int(input("Enter the value of divisor : "))

pro=num1/num2

if num1%num2==0:
    print(f"{num1} / {num2} = {pro}")
    print("It is divisible!")
else:
    print("Not divisible!")