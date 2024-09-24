import eyeD3


def embed_image_in_mp3(image_path, mp3_path, output_path):
    # Load the MP3 file
    audio_file = eyeD3.load(mp3_path)

    # Load the image file
    with open(image_path, 'rb') as img_file:
        image_data = img_file.read()

    # Embed the image as album art in the MP3 file
    audio_file.tag.setImage(3, image_data, 'image/jpeg')  # 3 is for the front cover

    # Save the MP3 file with embedded image
    audio_file.tag.save(output_path)
    print(f"MP3 file with embedded image saved as {output_path}")


# Example usage
image_path = '/home/jasvir/Pictures/Embed_mp3/1.jpg'  # Path to your image file
mp3_path = '/home/jasvir/Pictures/Embed_mp3/jodha.mp3'  # Path to your MP3 file
output_path = '/home/jasvir/Pictures/Embed_mp3/audio_with_image.mp3'  # Path to save the output MP3 file

embed_image_in_mp3(image_path, mp3_path, output_path)
