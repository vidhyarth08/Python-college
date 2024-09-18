import string

str = input("Enter the str : ")

result = str.translate(str.maketrans("","",string.punctuation))

print(result)