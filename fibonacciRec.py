def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Enter the value of n to print the fibonacci series : "))

for i in range(0,num):
    print(f"The fibonacci series is : {fibo(i)}")