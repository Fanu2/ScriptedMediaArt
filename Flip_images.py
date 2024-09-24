import glob
import os
import random
from string import ascii_lowercase, digits
import cv2

"""
Flip image and bounding box for computer vision tasks
https://paperswithcode.com/method/randomhorizontalflip
"""

# Parameters
LABEL_DIR = "/home/jasvir/Documents/Princess Jodha/labels/"  # Set this to your labels directory
IMAGE_DIR = "/home/jasvir/Documents/Princess Jodha/images/"  # Set this to your images directory
OUTPUT_DIR = "/home/jasvir/Documents/Princess Jodha/mosaic/"  # Set this to your output directory
FLIP_TYPE = 1  # 0 is vertical, 1 is horizontal


def main() -> None:
    """
    Load images and annotations, process them by flipping, and save the results.
    """
    img_paths, annos = get_dataset(LABEL_DIR, IMAGE_DIR)
    print("Processing...")
    new_images, new_annos, paths = update_image_and_anno(img_paths, annos, FLIP_TYPE)

    for index, image in enumerate(new_images):
        # Generate random string code
        letter_code = random_chars(32)
        file_name = os.path.basename(paths[index]).rsplit(".", 1)[0]
        file_root = os.path.join(OUTPUT_DIR, f"{file_name}_FLIP_{letter_code}")

        # Save the flipped image
        cv2.imwrite(f"{file_root}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 85])
        print(f"Success {index + 1}/{len(new_images)} with {file_name}")

        # Save the annotations
        annos_list = []
        for anno in new_annos[index]:
            obj = f"{anno[0]} {anno[1]} {anno[2]} {anno[3]} {anno[4]}"
            annos_list.append(obj)
        with open(f"{file_root}.txt", "w") as outfile:
            outfile.write("\n".join(line for line in annos_list))


def get_dataset(label_dir: str, img_dir: str) -> tuple[list, list]:
    """
    Load image paths and their corresponding annotations.

    - label_dir: Path to the directory containing annotation files
    - img_dir: Path to the directory containing image files

    Returns:
        - List of image paths
        - List of annotations for each image
    """
    img_paths = []
    labels = []
    for label_file in glob.glob(os.path.join(label_dir, "*.txt")):
        label_name = os.path.basename(label_file).rsplit(".", 1)[0]
        with open(label_file) as in_file:
            obj_lists = in_file.readlines()

        img_path = os.path.join(img_dir, f"{label_name}.jpg")
        if not os.path.exists(img_path):
            print(f"Warning: Image file not found at {img_path}")
            continue

        boxes = []
        for obj_list in obj_lists:
            obj = obj_list.rstrip("\n").split(" ")
            boxes.append([
                int(obj[0]),
                float(obj[1]),
                float(obj[2]),
                float(obj[3]),
                float(obj[4]),
            ])

        if boxes:
            img_paths.append(img_path)
            labels.append(boxes)
    return img_paths, labels


def update_image_and_anno(
        img_list: list, anno_list: list, flip_type: int = 1
) -> tuple[list, list, list]:
    """
    Flip images and update annotations.

    - img_list: List of image file paths
    - anno_list: List of annotations corresponding to each image
    - flip_type: 0 for vertical flip, 1 for horizontal flip

    Returns:
        - List of flipped images
        - List of updated annotations
        - List of image paths
    """
    new_annos_lists = []
    path_list = []
    new_imgs_list = []
    for idx in range(len(img_list)):
        new_annos = []
        path = img_list[idx]
        path_list.append(path)
        img_annos = anno_list[idx]
        img = cv2.imread(path)
        if img is None:
            print(f"Error: Image not found at {path}")
            continue

        new_img = cv2.flip(img, flip_type)
        for bbox in img_annos:
            if flip_type == 1:  # Horizontal flip
                x_center_new = 1 - bbox[1]
                new_annos.append([bbox[0], x_center_new, bbox[2], bbox[3], bbox[4]])
            elif flip_type == 0:  # Vertical flip
                y_center_new = 1 - bbox[2]
                new_annos.append([bbox[0], bbox[1], y_center_new, bbox[3], bbox[4]])

        new_annos_lists.append(new_annos)
        new_imgs_list.append(new_img)

    return new_imgs_list, new_annos_lists, path_list


def random_chars(number_char: int = 32) -> str:
    """
    Generate a random string of specified length.

    - number_char: Length of the string to generate

    Returns:
        - Randomly generated string
    """
    assert number_char > 1, "The number of characters should be greater than 1"
    letter_code = ascii_lowercase + digits
    return "".join(random.choice(letter_code) for _ in range(number_char))


if __name__ == "__main__":
    main()
    print("DONE ✅")
