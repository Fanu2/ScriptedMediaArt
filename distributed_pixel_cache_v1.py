import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def apply_discrete_fourier_transform(input_path, output_path):
    # Load the image and convert to grayscale
    img = Image.open(input_path).convert('L')
    img_array = np.array(img)

    # Compute the 2D DFT of the image
    dft = np.fft.fft2(img_array)

    # Shift the zero frequency component to the center
    dft_shifted = np.fft.fftshift(dft)

    # Compute the magnitude spectrum
    magnitude_spectrum = np.abs(dft_shifted)

    # Normalize the magnitude spectrum to fit in the 8-bit range
    magnitude_spectrum = np.log(1 + magnitude_spectrum)
    magnitude_spectrum = np.uint8(255 * magnitude_spectrum / np.max(magnitude_spectrum))

    # Save the magnitude spectrum as an image
    result_img = Image.fromarray(magnitude_spectrum)
    result_img.save(output_path)

    # Display the result
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum')
    plt.axis('off')
    plt.show()


# Example usage
apply_discrete_fourier_transform('/home/jasvir/Pictures/DFT/fanu.jpg', '/home/jasvir/Pictures/DFT/output1.jpg')

