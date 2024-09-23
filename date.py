import os
from datetime import datetime

# Specify the file path
file_path = 'file.txt'  # Replace with your file path

# Get the file creation time (ctime)
creation_time = os.path.getctime(file_path)

# Get the file modification time (mtime)
modification_time = os.path.getmtime(file_path)

# Convert both times to a human-readable format
creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
modification_date = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

# Print the creation and modification dates
print(f"Creation Date: {creation_date}")
print(f"Modification Date: {modification_date}")
