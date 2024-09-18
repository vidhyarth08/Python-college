num = int(input("Enter the number to check if it is an armstrong number or not : "))

sum=0
order = len(str(num))
copy_n = num

while num>0:
    digit = num%10
    sum+=digit**order
    num=num//10

if sum==copy_n:
    print("Armstrong number!")
else:
    print("Not an armstrong number!")

#print in range
range_e = int(input("Enter the range to print Armstrong numbers: "))

for num in range(0, range_e + 1):
    sum = 0
    order = len(str(num))
    copy_n = num

    while copy_n > 0:
        digit = copy_n % 10
        sum += digit ** order
        copy_n //= 10

    if sum == num:
        print(num)
