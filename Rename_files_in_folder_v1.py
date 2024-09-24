import os


def rename_files(directory):
    # Get a list of all files in the directory
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

    # Loop through the files and rename them
    for i, filename in enumerate(files, start=1):
        # Create the new file name
        new_name = f"{i}.png"

        # Get the full path to the files
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_file, new_file)

    print(f"Renamed {len(files)} files successfully!")


# Set the directory path
directory_path = "/home/jasvir/Music/Jodha3/images/"

# Call the function
rename_files(directory_path)
