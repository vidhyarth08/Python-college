num = int(input("Enter the number to reverse : "))

reverse_num = 0
temp = num

while num > 0:
    dig = num % 10
    reverse_num = reverse_num * 10 + dig
    num = num//10

print(f"The reverse of the number {temp} is : {reverse_num}")