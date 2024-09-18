n = int(input("Enter the number: "))

if n <= 1:
    print("Not Prime")
else:
    factor = 0
    for i in range(2, n):
        if n % i == 0:
            factor += 1
            break

    if factor == 0:
        print("Prime")
    else:
        print("Not Prime")
