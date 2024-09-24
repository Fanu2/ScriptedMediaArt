import subprocess
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def create_video_from_image(image_path, audio_path, subtitle_path, output_path):
    # Get the duration of the audio file
    command_get_duration = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        audio_path
    ]

    try:
        result = subprocess.run(command_get_duration, check=True, text=True, capture_output=True)
        audio_duration = float(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while getting the audio duration:\n{e.stderr}")
        return

    # Generate video from image with the same duration as the audio
    intermediate_video_path = output_path.replace('.mp4', '_intermediate.mp4')
    command_image_to_video = [
        'ffmpeg',
        '-loop', '1',
        '-i', image_path,
        '-c:v', 'libx264',
        '-t', str(audio_duration),
        '-pix_fmt', 'yuv420p',
        '-vf', 'scale=1920:1080',  # Adjust resolution if needed
        '-y',  # Overwrite output file if it exists
        intermediate_video_path
    ]

    try:
        subprocess.run(command_image_to_video, check=True, text=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while creating the video from the image:\n{e.stderr}")
        return

    # Add audio and subtitles to the video
    command_add_audio_subtitles = [
        'ffmpeg',
        '-i', intermediate_video_path,
        '-i', audio_path,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-shortest',
        '-vf', f'subtitles={subtitle_path}',
        '-y',  # Overwrite output file if it exists
        output_path
    ]

    try:
        subprocess.run(command_add_audio_subtitles, check=True, text=True, capture_output=True)
        messagebox.showinfo("Success", "MP4 file created successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while adding audio and subtitles:\n{e.stderr}")
        return

    # Remove intermediate video file
    try:
        os.remove(intermediate_video_path)
    except OSError as e:
        messagebox.showerror("Error", f"Error removing intermediate video file: {e.strerror}")

def select_file(filetypes, title="Select a file"):
    return filedialog.askopenfilename(filetypes=filetypes, title=title)

def save_file(filetypes, title="Save as"):
    return filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=filetypes, title=title)

def run_gui():
    root = tk.Tk()
    root.title("Video Creator")

    def on_run():
        image_path = select_file([("Image Files", "*.jpg *.jpeg *.png")], "Select an Image")
        audio_path = select_file([("Audio Files", "*.mp3 *.wav")], "Select an Audio File")
        subtitle_path = select_file([("Subtitle Files", "*.srt")], "Select a Subtitle File")
        output_path = save_file([("MP4 Video", "*.mp4")], "Save Video As")

        if image_path and audio_path and subtitle_path and output_path:
            create_video_from_image(image_path, audio_path, subtitle_path, output_path)

    run_button = tk.Button(root, text="Create Video", command=on_run)
    run_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
