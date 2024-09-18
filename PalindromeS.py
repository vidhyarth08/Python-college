str = input("Enter the string to check if it is palindrome or not : ")

reverse_str = ''

for i in range(len(str)-1,-1,-1):
    reverse_str += str[i]

if reverse_str == str:
    print(f"{str} is palindrome.")
else:
    print("Not palindrome.")