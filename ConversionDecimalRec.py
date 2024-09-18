def decimal(n):
      if n == 0:
          return '0'
      elif n == 1:
          return '1'
      else:
        return decimal(n // 2) + str(n % 2)
      
num = int(input("Enter the value of the decimal number : "))

print(f"Conversion of decimal number to binary number is : {num} = {decimal(num)}")