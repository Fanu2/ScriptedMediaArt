import os
import shutil

# Define the base directory
base_dir = "/home/jasvir/Documents/Princess Jodha/"


# Define the function to organize files by extension and handle duplicate names
def organize_files_by_extension(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1][1:]  # Get the file extension without the dot

            if file_extension:  # Only proceed if there is an extension
                # Create the directory for the extension if it doesn't exist
                ext_dir = os.path.join(base_dir, file_extension.upper())
                os.makedirs(ext_dir, exist_ok=True)

                # Define the new path and handle file name conflicts
                new_path = os.path.join(ext_dir, file)
                if os.path.exists(new_path):
                    base_name, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(new_path):
                        new_name = f"{base_name}_{counter}{ext}"
                        new_path = os.path.join(ext_dir, new_name)
                        counter += 1

                # Move the file to the corresponding directory
                shutil.move(file_path, new_path)


# Call the function to organize files
organize_files_by_extension(base_dir)
