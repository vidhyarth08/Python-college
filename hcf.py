n = int(input("Enter 1st number to find HCF: "))
m = int(input("Enter 2nd number to find HCF: "))

while m!=0:
    rem = n%m
    n=m
    m=rem

print(n)
