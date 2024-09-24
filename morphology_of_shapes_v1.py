from wand.image import Image

def apply_morphology_of_shapes(input_path, output_path):
    try:
        with Image(filename=input_path) as img:
            # Applying morphology operation: try different shapes
            try:
                img.morphology('Erode', 'Square', iterations=2)
                img.save(filename=output_path)
                print("Applied 'Erode' morphology successfully.")
            except Exception as e:
                print(f"Applying 'Erode' failed: {e}")

            try:
                img.morphology('Dilate', 'Square', iterations=2)
                img.save(filename=output_path)
                print("Applied 'Dilate' morphology successfully.")
            except Exception as e:
                print(f"Applying 'Dilate' failed: {e}")

            try:
                img.morphology('Open', 'Square', iterations=2)
                img.save(filename=output_path)
                print("Applied 'Open' morphology successfully.")
            except Exception as e:
                print(f"Applying 'Open' failed: {e}")

    except Exception as e:
        print(f"Error processing image: {e}")

# Example usage
apply_morphology_of_shapes('/home/jasvir/Pictures/DFT/fanu.jpg', '/home/jasvir/Pictures/DFT/output4.jpg')
