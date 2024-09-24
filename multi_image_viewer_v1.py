import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi Image Viewer")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack()

        self.prev_btn = tk.Button(self.btn_frame, text="Previous", command=self.prev_image)
        self.prev_btn.pack(side=tk.LEFT)

        self.next_btn = tk.Button(self.btn_frame, text="Next", command=self.next_image)
        self.next_btn.pack(side=tk.LEFT)

        self.open_btn = tk.Button(root, text="Open Folder", command=self.open_folder)
        self.open_btn.pack()

        self.images = []
        self.current_image_index = 0

    def open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.load_images(folder_path)

    def load_images(self, folder_path):
        self.images = []
        self.current_image_index = 0
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.images.append(os.path.join(folder_path, file))
        if self.images:
            self.display_image()

    def display_image(self):
        image_path = self.images[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((800, 600), Image.LANCZOS)  # Resize the image to fit the window
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def prev_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.display_image()

    def next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()
