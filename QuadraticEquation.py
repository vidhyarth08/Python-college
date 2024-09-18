import cmath as m

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))

d = b**2 + 4*a*c

if d>0:
   x1 = (-b + m.sqrt(d))/(2*a)
   x2 = (-b - m.sqrt(d))/(2*a)
   print(f"First root : {x1} , Second root : {x2}")
elif d==0:
   x1 = x2 = -b/(2*a)
   print(f"First and second roots are same : {x1}")
else:
     x1 = (-b + m.sqrt(d))/(2*a)
     x2 = (-b - m.sqrt(d))/(2*a)
     p = -b/(2*a)
     q = m.sqrt(d)/(2*a)
     print(f"{x1} = {p} + i*{q}")
     print(f"{x2} = {p} + i*{q}")
