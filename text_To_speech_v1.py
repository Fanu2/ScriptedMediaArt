# Import libraries
from tkinter import *
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# Initialize the Tkinter window
root = Tk()
root.geometry('300x300')
root.resizable(0, 0)
root.config(bg='Cyan4')
root.title('TEXT TO SPEECH')

# Set window icon (update the path as needed)
icon_path = 'C:/Users/User/Desktop/Competitive coding/Week 7/text to speech/Text-to-speech-icon.ico'
if os.path.isfile(icon_path):
    root.iconbitmap(icon_path)

# Window heading and labels
Label(root, text='TEXT TO SPEECH', font='arial 20 bold', bg='sky blue').pack()
Label(root, text='Enter Text', font='Helvetica', bg='sky blue').place(x=20, y=60)
Label(root, text='By VISHWAJEET ANAND', font='arial 15 bold', bg='sky blue').pack(side=BOTTOM)

# String variable for entry field
Msg = StringVar()

# Entry widget for user input
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


def Text_to_speech():
    """Convert text to speech and play the audio."""
    message = entry_field.get()
    if not message.strip():
        print("No text provided.")
        return

    # Convert text to speech
    speech = gTTS(text=message, lang='en', slow=False)
    audio_path = 'vishwajeet.mp3'
    speech.save(audio_path)

    # Load and play the audio file
    audio = AudioSegment.from_mp3(audio_path)
    play(audio)


def Exit():
    """Exit the application."""
    root.destroy()


def Reset():
    """Reset the text entry field."""
    Msg.set("")


# Buttons for various actions
Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, bg='sky blue', width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='sky blue').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset, bg='sky blue').place(x=175, y=140)

# Run the Tkinter event loop
root.mainloop()
