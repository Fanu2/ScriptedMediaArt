import cv2
import numpy as np


def apply_discrete_fourier_transform(input_path, output_path):
    # Read the input image
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Convert image to float32
    img_float32 = np.float32(img)

    # Apply Discrete Fourier Transform
    dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)

    # Shift the zero-frequency component to the center
    dft_shift = np.fft.fftshift(dft)

    # Compute the magnitude spectrum (log scale)
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    # Normalize magnitude spectrum to 8-bit range
    magnitude_spectrum_normalized = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)

    # Convert magnitude spectrum to uint8
    magnitude_spectrum_uint8 = np.uint8(magnitude_spectrum_normalized)

    # Save the result
    cv2.imwrite(output_path, magnitude_spectrum_uint8)


# Example usage
input_image_path = '/home/jasvir/Pictures/DFT/fanu.jpg'
output_image_path = '/home/jasvir/Pictures/DFT/output.jpg'
apply_discrete_fourier_transform(input_image_path, output_image_path)

