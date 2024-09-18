import hashlib

def find_file_hash(file_path, hash_type="md5"):
    hash_func = hashlib.new(hash_type)
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()


file_path = 'path to your text file'
file_hash = find_file_hash(file_path, hash_type="md5")  
print(f"The MD5 hash of the file is: {file_hash}")
