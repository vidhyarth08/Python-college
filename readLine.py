def read_file_into_list(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip()) 
    return lines

print(read_file_into_list('use your text file to count the lines'))