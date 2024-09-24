import cv2
import numpy as np


def apply_convex_hull(input_path, output_path):
    # Read the image
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding
    _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an image to draw the convex hull
    hull_image = np.zeros_like(img)

    # Draw convex hull for each contour
    for contour in contours:
        hull = cv2.convexHull(contour)
        cv2.drawContours(hull_image, [hull], -1, (255, 255, 255), 2)

    # Save the convex hull image
    cv2.imwrite(output_path, hull_image)


# Example usage
input_image_path = '/home/jasvir/Pictures/ConvexHull/fanu.jpg'
output_image_path = '/home/jasvir/Pictures/ConvexHull/output.jpg'
apply_convex_hull(input_image_path, output_image_path)
