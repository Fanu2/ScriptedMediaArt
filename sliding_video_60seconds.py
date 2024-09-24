from moviepy.editor import ImageClip, concatenate_videoclips

# List of image paths
image_paths = [
    "/home/jasvir/Music/jas/jass/7.jpg",
    "/home/jasvir/Music/jas/jass/2.jpg",
    "/home/jasvir/Music/jas/jass/3.jpg",
    "/home/jasvir/Music/jas/jass/4.jpg",
    "/home/jasvir/Music/jas/jass/5.jpg",
    "/home/jasvir/Music/jas/jass/6.jpg"
]

# Parameters
duration_per_image = 10  # 10 seconds per image to make 6 images in 60 seconds
slide_duration = 60 / len(image_paths)  # Each image will slide for 10 seconds

# Create individual clips with sliding effect
clips = []
for image_path in image_paths:
    clip = ImageClip(image_path).set_duration(slide_duration)


    # Slide the image from left to right
    def slide(image, t):
        x = int(clip.w * t / slide_duration)
        return image.crop(x1=x, y1=0, x2=x + clip.w, y2=clip.h)


    sliding_clip = clip.fl_time(lambda t: slide(clip.get_frame(t), t), apply_to=['mask', 'video'])
    clips.append(sliding_clip)

# Concatenate the clips into one video
video = concatenate_videoclips(clips, method="compose")

# Write the final video file
video.write_videofile("/home/jasvir/Music/jas/jass/sliding_video.mp4", fps=24)
