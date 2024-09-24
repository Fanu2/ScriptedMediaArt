import numpy as np
from moviepy.editor import TextClip, CompositeVideoClip, concatenate_videoclips

# Define screen size and text parameters
screensize = (720, 460)
text_content = "Love Jodha"
font_name = "Amiri-Bold"
font_size = 100

# Helper function for rotation matrix
def rotMatrix(a):
    """Return a 2D rotation matrix for angle a."""
    return np.array([[np.cos(a), np.sin(a)], [-np.sin(a), np.cos(a)]])

# Define movement functions for the letters
def vortex(screenpos, i, nletters):
    """Define vortex effect movement."""
    d = lambda t: 1.0 / (0.3 + t**8)  # damping
    a = i * np.pi / nletters  # angle of the movement
    v = rotMatrix(a).dot([-1, 0])
    if i % 2:
        v[1] = -v[1]
    return lambda t: screenpos + 400 * d(t) * rotMatrix(0.5 * d(t) * a).dot(v)

def cascade(screenpos, i, nletters):
    """Define cascade effect movement."""
    v = np.array([0, -1])
    d = lambda t: 1 if t < 0 else abs(np.sinc(t) / (1 + t**4))
    return lambda t: screenpos + v * 400 * d(t - 0.15 * i)

def arrive(screenpos, i, nletters):
    """Define arrive effect movement."""
    v = np.array([-1, 0])
    d = lambda t: max(0, 3 - 3 * t)
    return lambda t: screenpos - 400 * v * d(t - 0.2 * i)

def vortexout(screenpos, i, nletters):
    """Define vortex out effect movement."""
    d = lambda t: max(0, t)  # damping
    a = i * np.pi / nletters  # angle of the movement
    v = rotMatrix(a).dot([-1, 0])
    if i % 2:
        v[1] = -v[1]
    return lambda t: screenpos + 400 * d(t - 0.1 * i) * rotMatrix(-0.2 * d(t) * a).dot(v)

# Create individual letter clips manually
def create_letter_clips(text, screensize, font_name, font_size):
    """Create a list of TextClips for each letter in the text."""
    letter_clips = []
    x = 0
    for letter in text:
        letter_clip = TextClip(
            letter, color="white", font=font_name, kerning=5, fontsize=font_size
        )
        letter_clip = letter_clip.set_position((x, 'center')).set_duration(5)
        letter_clips.append({
            'clip': letter_clip,
            'initial_pos': np.array([x, screensize[1] // 2])
        })
        x += letter_clip.w + 10  # Move the next letter to the right
    return letter_clips

# Create letter clips
letter_clips = create_letter_clips(text_content, screensize, font_name, font_size)

def moveLetters(letter_clips, funcpos):
    """Apply the movement function to each letter clip."""
    return [
        letter_clip['clip'].set_position(
            funcpos(letter_clip['initial_pos'], i, len(letter_clips))
        )
        for i, letter_clip in enumerate(letter_clips)
    ]

# Generate clips with different text effects
clips = [
    CompositeVideoClip(moveLetters(letter_clips, funcpos), size=screensize).subclip(0, 5)
    for funcpos in [vortex, cascade, arrive, vortexout]
]

# Concatenate all clips and write to a file
final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("/home/jasvir/Music/jodha6/coolTextEffects.avi", fps=25, codec="mpeg4")

print("Video saved to ../../coolTextEffects.avi")
