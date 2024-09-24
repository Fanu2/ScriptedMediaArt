import subprocess
import base64

def encode_key(key):
    return base64.b64encode(key.encode()).decode()

def apply_encipher(input_path, output_path, key='secret'):
    # Encode the key to ensure it's correctly passed
    encoded_key = encode_key(key)
    command = [
        'convert', input_path,
        '-encipher', encoded_key,
        output_path
    ]
    subprocess.run(command, check=True)

def apply_decipher(input_path, output_path, key='secret'):
    # Encode the key to ensure it's correctly passed
    encoded_key = encode_key(key)
    command = [
        'convert', input_path,
        '-decipher', encoded_key,
        output_path
    ]
    subprocess.run(command, check=True)

# Example usage
apply_encipher('/home/jasvir/Pictures/DFT/fanu.jpg', '/home/jasvir/Pictures/DFT/encrypted_output.jpg')
apply_decipher('/home/jasvir/Pictures/DFT/encrypted_output.jpg', '/home/jasvir/Pictures/DFT/decrypted_output.jpg')
