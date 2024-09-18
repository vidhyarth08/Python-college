num = int(input("Enter the number to find the factors : "))

if num%1==0:
    print(f"{1}")

for i in range(2,num):
    div = num/i
    if num%i == 0:
        print(f"{i}")

print(f"{num}")