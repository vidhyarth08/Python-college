file_path = "file.txt"

line_count = 0

with open(file_path,'r') as file:
    for line in file:
        line_count+=1


print(line_count)