row = int(input("Enter the number of rows : "))

for i in range(1,row+1):
    print(' ' * (row-i) + '*' * (2*i-1))

print("<-------------------->")

for i in range(row,0,-1):
    print(' ' * (row-i) + '*' * (2*i-1))