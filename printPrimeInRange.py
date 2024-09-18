def prime(n):
   if n <= 1:
    print("Not Prime")
   else:
    factor = 0
    for i in range(2, n):
        if n % i == 0:
            factor += 1
            break

    if factor == 0:
        return True
    else:
        return False

for i in range(1,101):
    if prime(i):
        print(i)