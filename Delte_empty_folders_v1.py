import os

# Define the base directory
base_dir = "/home/jasvir/Documents/Princess Jodha/"

# Define the function to delete empty folders
def delete_empty_folders(base_dir):
    for root, dirs, files in os.walk(base_dir, topdown=False):  # Walk the directory tree bottom-up
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)  # This will only remove the directory if it's empty
                print(f"Deleted empty folder: {dir_path}")
            except OSError:
                pass  # If the directory is not empty, ignore the error

# Call the function to delete empty folders
delete_empty_folders(base_dir)
