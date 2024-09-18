power = int(input("Enter the value of power : "))

num=2
pro=1

if power==0:
    print(f"{1}")
else:
    print(f"{2**power}")

range_end = int(input("Enter the range : "))

for i in range(1,range_end+1):
    power+=i
    print(f"{2**power}")