n = int(input("Enter the value of n to print the fibonacci series : "))

n0=0
n1=1
print(f"{n0}")
print(f"{n1}")

for i in range(2,n):
    n2=n0+n1
    print(f"{n2}")
    n0=n1
    n1=n2
