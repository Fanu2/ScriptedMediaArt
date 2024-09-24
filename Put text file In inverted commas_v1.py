input_file_path = '/home/jasvir/Music/jodha/jodha.txt'
output_file_path = '/home/jasvir/Music/jodha/new_file.txt'

# Read the content from the input file
with open(input_file_path, 'r') as file:
    content = file.read()

# Split the content into sentences (assuming sentences end with a period)
sentences = content.split('.')

# Enclose each sentence in double quotes and add a comma, then join them back together
modified_content = ', '.join([f'"{sentence.strip()}."' for sentence in sentences if sentence.strip()])

# Write the modified content to the output file
with open(output_file_path, 'w') as file:
    file.write(modified_content)

print(f"Modified content saved to {output_file_path}")
