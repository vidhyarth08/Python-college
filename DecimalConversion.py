#decimal to binary
decimal_num = int(input("Enter the value of the decimal number: "))

# empty string to store binary result
binary_num = ''

# copy original number
num = decimal_num

while num > 0:
    rem = num % 2
    binary_num = str(rem) + binary_num
    num = num // 2

if decimal_num == 0:
    binary_num = '0'

print(f"Conversion of decimal number to binary number is : {decimal_num} = {binary_num}")

#decimal to octal

octal_num = ''

num = decimal_num

while num>0:
    rem = num%8
    octal_num = str(rem) + octal_num
    num = num//8

if decimal_num == 0:
    octal_num = '0'

print(f"Conversion of decimal number to octal number is : {decimal_num} = {octal_num}")

#decimal to hexadecimal

hexadecimal_num = ''

num = decimal_num

while num>0:
    rem = num%16
    if rem < 10:
     hexadecimal_num = str(rem) + hexadecimal_num
    else:
        hexadecimal_num = chr(rem - 10 + ord('A')) + hexadecimal_num
    num = num // 16

if decimal_num == 0:
    hexadecimal_num = '0'

print(f"Conversion of decimal number to hexadecimal number is : {decimal_num} = {hexadecimal_num}")