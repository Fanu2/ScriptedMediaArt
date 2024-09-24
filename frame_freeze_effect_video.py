from moviepy.editor import *

# Load the video and define the time for the freeze frame
video = VideoFileClip("/home/jasvir/Music/jodha4/jodha.mp4")
freeze_time = cvsecs(00.04)  # Time of the freeze at 19 minutes 21 seconds

# Create subclips: 2 seconds before and after the freeze time
clip_before = video.subclip(max(0, freeze_time - 2), freeze_time)
clip_after = video.subclip(freeze_time, min(freeze_time + 2, video.duration))

# Extract the frame at the freeze time and apply the painting effect
freeze_frame = video.to_ImageClip(freeze_time)
painting_effect = video.fx(vfx.painting, saturation=1.6, black=0.006).to_ImageClip(freeze_time)

# Create the text overlay with a font available on MX Linux
text_overlay = TextClip('Audrey', font='DejaVu-Serif', fontsize=35).set_pos((10, 180))

# Combine the painted frame with the text overlay
painting_with_text = (
    CompositeVideoClip([painting_effect, text_overlay])
    .add_mask()
    .set_duration(3)
    .crossfadein(0.5)
    .crossfadeout(0.5)
)

# Create the final composite with fade-in/fade-out effects
painting_fading = CompositeVideoClip([freeze_frame, painting_with_text])

# Concatenate the before clip, the freeze frame with effects, and the after clip
final_clip = concatenate_videoclips([
    clip_before,
    painting_fading.set_duration(3),
    clip_after
])

# Export the final video
final_clip.write_videofile('/home/jasvir/Music/jodha4/jodha.avi', fps=video.fps, codec="mpeg4", audio_bitrate="3000k")
