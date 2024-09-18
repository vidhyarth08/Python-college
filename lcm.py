import math as m

a=int(input("Enter 1st number to find LCM : "))
b=int(input("Enter 2nd number to find LCM : "))

gcd = m.gcd(a,b)

lcm = (a*b) // gcd

print(f"The LCM of {a} and {b} is : {lcm}")