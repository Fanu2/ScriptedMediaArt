from moviepy.editor import *

# Manually define seven regions with their sizes and positions
regions = [
    {"size": (100, 150), "position": (10, 20)},   # Region 0
    {"size": (120, 200), "position": (130, 20)},  # Region 1
    {"size": (80, 100), "position": (260, 20)},   # Region 2
    {"size": (90, 120), "position": (10, 180)},   # Region 3
    {"size": (110, 140), "position": (110, 180)}, # Region 4
    {"size": (100, 160), "position": (230, 180)}, # Region 5
    {"size": (120, 180), "position": (360, 180)}  # Region 6
]

# Load video clips
clip_paths = [
    "/home/jasvir/Music/jodha5/1.mp4",
    "/home/jasvir/Music/jodha5/2.mp4",
    "/home/jasvir/Music/jodha5/3.mp4",
    "/home/jasvir/Music/jodha5/4.mp4",
    "/home/jasvir/Music/jodha5/5.mp4",
    "/home/jasvir/Music/jodha5/6.mp4",
    "/home/jasvir/Music/jodha5/7.mp4"
]

# Load clips and subclip them
clips = [VideoFileClip(path, audio=False).subclip(18, 22) for path in clip_paths]

# Ensure the number of clips matches the number of regions
if len(clips) != len(regions):
    raise ValueError("The number of clips does not match the number of regions.")

# Fit each clip into its corresponding region
comp_clips = [clip.resize(size).set_pos(position) for clip, (size, position) in zip(clips, [(r["size"], r["position"]) for r in regions])]

# Create a blank base image for composition (if not using a real base image)
base_image_size = (800, 600)  # Example size; adjust as needed
base_image = ColorClip(size=base_image_size, color=(0, 0, 0)).set_duration(clips[0].duration)

# Composite the clips on the base image
final_clip = CompositeVideoClip([base_image] + comp_clips)
final_clip.resize(0.6).write_videofile("/home/jasvir/Music/jodha5/complex.mp4")

print("Video processing complete.")
