import glob
import os
import random
from string import ascii_lowercase, digits

import cv2
import numpy as np

# Parameters
OUTPUT_SIZE = (720, 1280)  # Height, Width
SCALE_RANGE = (0.4, 0.6)  # Scale range for resizing
FILTER_TINY_SCALE = 1 / 100  # Minimum bounding box size to keep
LABEL_DIR = "/home/jasvir/Documents/Princess Jodha/labels/"
IMG_DIR = "/home/jasvir/Documents/Princess Jodha/images/"
OUTPUT_DIR = "/home/jasvir/Documents/Princess Jodha/mosaic/"
NUMBER_IMAGES = 50


def main() -> None:
    """
    Get images list and annotations list from input dir.
    Update new images and annotations.
    Save images and annotations in output dir.
    """
    print(f"Checking dataset from: LABEL_DIR={LABEL_DIR}, IMG_DIR={IMG_DIR}")

    img_paths, annos = get_dataset(LABEL_DIR, IMG_DIR)

    if not img_paths or not annos:
        print("No images or annotations found. Please check your dataset.")
        return  # Stop if no images are found

    print(f"Found {len(img_paths)} images and annotations. Starting process...")

    for index in range(NUMBER_IMAGES):
        idxs = random.sample(range(len(annos)), 4)
        new_image, new_annos, path = update_image_and_anno(
            img_paths,
            annos,
            idxs,
            OUTPUT_SIZE,
            SCALE_RANGE,
            filter_scale=FILTER_TINY_SCALE,
        )

        if new_image is None:
            print(f"Skipping generation for index {index + 1} due to missing image.")
            continue  # Skip to the next iteration if the image is missing

        if path is None:
            print(f"Skipping generation for index {index + 1} due to missing path.")
            continue

        letter_code = random_chars(32)
        file_name = path.split(os.sep)[-1].rsplit(".", 1)[0]
        file_root = f"{OUTPUT_DIR}/{file_name}_MOSAIC_{letter_code}"

        if not cv2.imwrite(f"{file_root}.jpg", new_image, [cv2.IMWRITE_JPEG_QUALITY, 85]):
            print(f"Error: Could not save image {file_root}.jpg")
            continue

        print(f"Succeeded {index + 1}/{NUMBER_IMAGES} with {file_name}")

        annos_list = []
        for anno in new_annos:
            width = anno[3] - anno[1]
            height = anno[4] - anno[2]
            x_center = anno[1] + width / 2
            y_center = anno[2] + height / 2
            obj = f"{anno[0]} {x_center} {y_center} {width} {height}"
            annos_list.append(obj)

        with open(f"{file_root}.txt", "w") as outfile:
            outfile.write("\n".join(line for line in annos_list))

    print("Processing completed.")


def get_dataset(label_dir: str, img_dir: str) -> tuple[list, list]:
    """
    Load images and annotations from the given directories.

    - label_dir <type: str>: Path to label directory containing annotation files.
    - img_dir <type: str>: Path to directory containing images.

    Returns:
        - img_paths: List of image file paths.
        - labels: List of annotations corresponding to each image.
    """
    img_paths = []
    labels = []
    print(f"Loading dataset from {label_dir} and {img_dir}...")

    for label_file in glob.glob(os.path.join(label_dir, "*.txt")):
        label_name = label_file.split(os.sep)[-1].rsplit(".", 1)[0]
        with open(label_file) as in_file:
            obj_lists = in_file.readlines()

        img_path = os.path.join(img_dir, f"{label_name}.jpg")
        if not os.path.exists(img_path):
            print(f"Warning: Image file not found at {img_path}")
            continue  # Skip if image file doesn't exist

        boxes = []
        for obj_list in obj_lists:
            obj = obj_list.rstrip("\n").split(" ")
            xmin = float(obj[1]) - float(obj[3]) / 2
            ymin = float(obj[2]) - float(obj[4]) / 2
            xmax = float(obj[1]) + float(obj[3]) / 2
            ymax = float(obj[2]) + float(obj[4]) / 2
            boxes.append([int(obj[0]), xmin, ymin, xmax, ymax])

        if not boxes:
            continue

        img_paths.append(img_path)
        labels.append(boxes)

    print(f"Loaded {len(img_paths)} image paths and annotations.")
    return img_paths, labels


def update_image_and_anno(
        all_img_list: list,
        all_annos: list,
        idxs: list[int],
        output_size: tuple[int, int],
        scale_range: tuple[float, float],
        filter_scale: float = 0.0,
) -> tuple[np.ndarray, list, str]:
    """
    Update the image and annotations to create a mosaic.

    - all_img_list <type: list>: List of image paths.
    - all_annos <type: list>: List of annotations corresponding to each image.
    - idxs <type: list[int]>: Indices of images to be used for the mosaic.
    - output_size <type: tuple[int, int]>: Size of the output mosaic image.
    - scale_range <type: tuple[float, float]>: Range for scaling the images.
    - filter_scale <type: float>: Minimum size of bounding box to keep.

    Returns:
        - output_img: Mosaic image.
        - new_anno: Updated annotations.
        - path_list[0]: Path of the first image used in the mosaic.
    """
    output_img = np.zeros([output_size[0], output_size[1], 3], dtype=np.uint8)
    scale_x = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    scale_y = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    divid_point_x = int(scale_x * output_size[1])
    divid_point_y = int(scale_y * output_size[0])

    new_anno = []
    path_list = []
    for i, index in enumerate(idxs):
        path = all_img_list[index]
        print(f"Loading image from: {path}")
        img = cv2.imread(path)
        if img is None:
            print(f"Error: Couldn't load the image from {path}")
            return None, None, None  # Return None if the image couldn't be loaded

        path_list.append(path)  # Ensure path is added to the list

        # Process the image as in the original logic
        if i == 0:  # top-left
            img = cv2.resize(img, (divid_point_x, divid_point_y))
            output_img[:divid_point_y, :divid_point_x, :] = img
            for bbox in all_annos[index]:
                xmin = bbox[1] * scale_x
                ymin = bbox[2] * scale_y
                xmax = bbox[3] * scale_x
                ymax = bbox[4] * scale_y
                new_anno.append([bbox[0], xmin, ymin, xmax, ymax])
        elif i == 1:  # top-right
            img = cv2.resize(img, (output_size[1] - divid_point_x, divid_point_y))
            output_img[:divid_point_y, divid_point_x : output_size[1], :] = img
            for bbox in all_annos[index]:
                xmin = scale_x + bbox[1] * (1 - scale_x)
                ymin = bbox[2] * scale_y
                xmax = scale_x + bbox[3] * (1 - scale_x)
                ymax = bbox[4] * scale_y
                new_anno.append([bbox[0], xmin, ymin, xmax, ymax])
        elif i == 2:  # bottom-left
            img = cv2.resize(img, (divid_point_x, output_size[0] - divid_point_y))
            output_img[divid_point_y : output_size[0], :divid_point_x, :] = img
            for bbox in all_annos[index]:
                xmin = bbox[1] * scale_x
                ymin = scale_y + bbox[2] * (1 - scale_y)
                xmax = bbox[3] * scale_x
                ymax = scale_y + bbox[4] * (1 - scale_y)
                new_anno.append([bbox[0], xmin, ymin, xmax, ymax])
        else:  # bottom-right
            img = cv2.resize(
                img, (output_size[1] - divid_point_x, output_size[0] - divid_point_y)
            )
            output_img[
                divid_point_y : output_size[0], divid_point_x : output_size[1], :
            ] = img
            for bbox in all_annos[index]:
                xmin = scale_x + bbox[1] * (1 - scale_x)
                ymin = scale_y + bbox[2] * (1 - scale_y)
                xmax = scale_x + bbox[3] * (1 - scale_x)
                ymax = scale_y + bbox[4] * (1 - scale_y)
                new_anno.append([bbox[0], xmin, ymin, xmax, ymax])

    # Remove bounding boxes smaller than filter_scale
    if filter_scale > 0:
        new_anno = [
            anno
            for anno in new_anno
            if filter_scale < (anno[3] - anno[1]) and filter_scale < (anno[4] - anno[2])
        ]

    if not path_list:
        print("Error: No paths added to path_list.")
        return None, None, None

    return output_img, new_anno, path_list[0]


def random_chars(number_char: int) -> str:
    """Generate random characters for naming files."""
    assert number_char > 1, "The number of characters should be greater than 1"
    letter_code = ascii_lowercase + digits
    return "".join(random.sample(letter_code * 4, number_char))


if __name__ == "__main__":
    main()
