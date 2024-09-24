import os

def rename_python_files(directory, prefix='script_', suffix='_v1'):
    """
    Renames Python files in the specified directory.

    Args:
        directory (str): The directory containing Python files.
        prefix (str): Prefix to add to the filename.
        suffix (str): Suffix to add to the filename.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"The directory {directory} does not exist.")

    files = [f for f in os.listdir(directory) if f.endswith('.py')]
    for file in files:
        old_name = os.path.join(directory, file)
        # Extract the base name and extension
        base_name, ext = os.path.splitext(file)

        # Create new filename
        new_name = f"{prefix}{base_name}{suffix}{ext}"
        new_path = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_name, new_path)
        print(f"Renamed {file} to {new_name}")

if __name__ == "__main__":
    # Set the directory path where Python files are located
    directory_path = '/home/jasvir/PycharmProjects/Imagemagic/scripts/'  # Update this path
    rename_python_files(directory_path)
