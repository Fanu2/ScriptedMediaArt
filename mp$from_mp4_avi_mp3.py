#!/usr/bin/env python
# -*- coding: utf-8 -*-

import moviepy.editor as mpy
import os

def main():
    # Define file paths
    mp4_path = '/home/jasvir/Music/jodha7/1.mp4'
    avi_path = '/home/jasvir/Music/jodha7/1.avi'
    mp3_path = '/home/jasvir/Music/jodha7/1.mp3'
    output_path = '/home/jasvir/Music/jodha7/output_video.mp4'

    # Load video and audio clips
    video_mp4 = mpy.VideoFileClip(mp4_path)
    video_avi = mpy.VideoFileClip(avi_path)
    audio_mp3 = mpy.AudioFileClip(mp3_path)

    # Concatenate videos
    video_combined = mpy.concatenate_videoclips([video_mp4, video_avi])

    # Loop video to match audio duration
    video_duration = audio_mp3.duration
    video_combined = video_combined.loop(duration=video_duration)

    # Set audio to the video
    final_clip = video_combined.set_audio(audio_mp3)

    # Write the result to a file
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    main()
