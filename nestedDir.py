import os

def create_nested_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Successfully created the directory: {path}")
    except Exception as e:
        print(f"Failed to create the directory: {e}")


nested_dir = "parent_dir/child_dir/grandchild_dir" #create this directory
create_nested_directory(nested_dir)
