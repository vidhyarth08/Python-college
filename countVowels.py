str = input("Enter the string : ")

vowels="aeiou"
count=0

for char in str:
    if char in vowels:
        count+=1


print(count)