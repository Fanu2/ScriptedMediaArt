from tkinter import *
from tkinter import filedialog
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# Initialize the window
root = Tk()
root.geometry('300x300')
root.resizable(0, 0)
root.config(bg='Cyan4')
root.title('TEXT TO SPEECH')

# Set the icon (ensure the path is correct and the file exists)
# root.iconbitmap('/path/to/your/icon.ico')

# Heading of the window
Label(root, text='TEXT TO SPEECH', font='arial 20 bold', bg='sky blue').pack()
Label(root, text='Enter Text', font='Helvetica', bg='sky blue').place(x=20, y=60)
Label(root, text='By ', font='arial 15 bold', bg='sky blue').pack(side=BOTTOM)

# Entry widget to accept user input
Msg = StringVar()
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


# User-defined function to convert text to speech
def Text_to_speech():
    Message = entry_field.get()
    if not Message:
        return

    # Generate the audio file using gTTS
    speech = gTTS(text=Message, lang='en', slow=False)
    mp3_path = '/home/jasvir/Pictures/Embed_mp3/jodha.mp3'
    speech.save(mp3_path)

    # Load and play the audio file
    audio = AudioSegment.from_mp3(mp3_path)
    play(audio)


# Function to save the audio file
def Save_audio():
    Message = entry_field.get()
    if not Message:
        return

    # Generate the audio file using gTTS
    speech = gTTS(text=Message, lang='en', slow=False)

    # Ask the user for the save location and filename
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

    if file_path:
        speech.save(file_path)
        print(f"Audio saved as {file_path}")


# Function to exit the application
def Exit():
    root.destroy()


# Function to reset the entry field
def Reset():
    Msg.set("")


# Buttons for play, save, exit, and reset actions
Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, bg='sky blue', width=4).place(x=25, y=140)
Button(root, text="SAVE", font='arial 15 bold', command=Save_audio, bg='sky blue').place(x=100, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='sky blue').place(x=175, y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset, bg='sky blue').place(x=250, y=140)

# Infinite loop to run the program
root.mainloop()
