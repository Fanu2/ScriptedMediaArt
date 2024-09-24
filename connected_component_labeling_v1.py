import cv2
import numpy as np


def apply_connected_component_labeling(input_path, output_path):
    # Read the image
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding
    _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Perform connected component labeling
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_img, connectivity=8)

    # Generate a color image to visualize labels
    label_image = np.zeros((binary_img.shape[0], binary_img.shape[1], 3), dtype=np.uint8)
    for label in range(1, num_labels):  # 0 is the background
        mask = (labels == label)
        label_image[mask] = np.random.randint(0, 255, size=3)  # Random color for each component

    # Save the labeled image
    cv2.imwrite(output_path, label_image)


# Example usage
input_image_path = '/home/jasvir/Pictures/ConnectedComponents/fanu1.jpg'
output_image_path = '/home/jasvir/Pictures/ConnectedComponents/fanuoutput1.jpg'
apply_connected_component_labeling(input_image_path, output_image_path)
