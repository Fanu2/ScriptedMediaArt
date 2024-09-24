from PIL import Image, ImageDraw, ImageFont
import os  # Make sure to import the os module

# Define paths
output_dir = "/home/jasvir/Music/Jodha3/"
font_path = "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"  # Ensure this path is correct
font_size = 32
image_width = 800
image_height = 600

# Hardcoded list of sentences
sentences = [
    #Here are the lines with Hindi full stops removed, each line in inverted commas followed by a comma, and without serial numbers:

"जोधा, तुम्हारी मुस्कान से हर सुबह में नयापन आता है",
"जोधा, तुम्हारी आँखों की चमक से मेरे दिल को सुकून मिलता है",
"जोधा, तुम्हारे बिना हर रंग फीका लगता है",
"जोधा, तुम्हारी हर बात में एक खास जादू है",
"जोधा, तुम्हारी हँसी सुनकर हर दर्द गायब हो जाता है",
"जोधा, तुम मेरे जीवन की सबसे प्यारी ख्वाहिश हो",
"जोधा, तुम्हारे साथ बिताया हर पल अमूल्य है",
"जोधा, तुम मेरी ज़िंदगी की सबसे खूबसूरत कहानी हो",
"जोधा, तुम्हारी बातें मेरे दिल को गहराई से छू जाती हैं",
"जोधा, तुम्हारी आँखों की चमक से हर रात रोशन हो जाती है",
"जोधा, तुम्हारे बिना हर दिन अधूरा लगता है",
"जोधा, तुम्हारे साथ बिताए पल हमेशा याद रहेंगे",
"जोधा, तुम मेरी सुबह की पहली रौशनी हो",
"जोधा, तुम्हारी आवाज़ मेरे दिल को शांति देती है",
"जोधा, तुम्हारी हर मुस्कान मेरे जीवन को खुशियों से भर देती है",
"जोधा, तुम मेरी सबसे बड़ी खुशी हो",
"जोधा, तुम्हारे बिना इस दुनिया में कुछ भी खास नहीं लगता",
"जोधा, तुम्हारे बिना हर दिन जैसे एक लंबा सफर हो",
"जोधा, तुम्हारी आँखों में खो जाना मेरे दिल की सबसे बड़ी इच्छा है",
"जोधा, तुम्हारी बातों में वो खास बात है जो कहीं और नहीं मिलती",
"जोधा, तुम्हारे बिना मेरी ज़िंदगी अधूरी है",
"जोधा, तुम्हारी हर खुशी मेरे दिल की सबसे बड़ी चाहत है",
"जोधा, तुम्हारे साथ बिताया हर पल एक ख्वाब की तरह है",
"जोधा, तुम्हारी हर बात मेरे दिल को छू जाती है",
"जोधा, तुम मेरी ज़िंदगी का सबसे सुंदर हिस्सा हो",
"जोधा, तुम्हारे बिना मेरा दिल हमेशा खाली लगता है",
"जोधा, तुम्हारी मुस्कान हर ग़म को भुला देती है",
"जोधा, तुम्हारी हर बात मेरे दिल को शांति देती है",
"जोधा, तुम्हारे बिना मेरा जीवन अधूरा है",
"जोधा, तुम्हारी यादों में खो जाना मेरे दिल की सबसे बड़ी खुशी है"
]

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print(f"Font file not found: {font_path}")
    exit()

# Create images for each sentence
for i, sentence in enumerate(sentences):
    # Create a new image with white background
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    # Calculate text size using textbbox
    bbox = draw.textbbox((0, 0), sentence, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Print debugging information
    print(f"Processing sentence {i + 1}:")
    print(f"Text: {sentence}")
    print(f"Bounding Box: {bbox}")
    print(f"Text Width: {text_width}, Text Height: {text_height}")

    # Calculate position for centering text
    text_x = (image_width - text_width) / 2
    text_y = (image_height - text_height) / 2

    # Draw the text
    draw.text((text_x, text_y), sentence, font=font, fill='black')

    # Save image
    image_filename = os.path.join(output_dir, f"sentence_{i + 1}.png")
    image.save(image_filename)

    print(f"Image saved: {image_filename}")

print("All images created successfully!")
