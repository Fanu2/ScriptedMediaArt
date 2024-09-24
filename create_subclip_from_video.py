from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Load the video and select a subclip from 50 to 60 seconds
video_clip = VideoFileClip("/home/jasvir/Music/jas/jass/1.mp4").subclip(50, 70)

# Create a text clip with custom settings
text_clip = (
    TextClip("Love of  Jodha", fontsize=70, color='white')
    .set_position('center')
    .set_duration(20)
)

# Combine the video and text clip
final_clip = CompositeVideoClip([video_clip, text_clip])

# Write the result to a file
final_clip.write_videofile("/home/jasvir/Music/jas/jass/jass_1.mp4", fps=25)
