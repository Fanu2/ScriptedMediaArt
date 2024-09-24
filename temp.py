import os

# Specify the directory where the files are located
directory = '/home/jasvir/PycharmProjects/Images/Imagemagic/scripts2/'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the filename starts with 'script_'
    if filename.startswith('script_'):
        # Create the new filename by removing 'script_'
        new_filename = filename.replace('script_', '', 1)
        # Create full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')

print("All applicable files have been renamed.")
