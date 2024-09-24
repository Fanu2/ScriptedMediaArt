#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import logging

import moviepy.editor as mpy

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)


def main():
    movielist = config()
    generate_movies(movielist)
    return


def config():
    # Define the path to the video files
    base_path = "/home/jasvir/Music/jodha6/"

    # List of videos with their sequence ranges
    start_clip = {"name": os.path.join(base_path, "/home/jasvir/Music/jodha6/1.mp4"), "seq": (9, 25.5)}
    seg1 = {"name": os.path.join(base_path, "/home/jasvir/Music/jodha6/2.mp4"), "seq": (0, 12)}
    seg2 = {"name": os.path.join(base_path, "/home/jasvir/Music/jodha6/3.mp4"), "seq": (7.8, 20.6)}
    det1 = {"name": os.path.join(base_path, "/home/jasvir/Music/jodha6/4.mp4"), "seq": (2, 20)}
    det2 = {"name": os.path.join(base_path, "/home/jasvir/Music/jodha6/5.mp4"), "seq": (4, None)}
    united = {"name": os.path.join(base_path, "/home/jasvir/Music/jodha6/6.mp4"), "seq": (2, 12)}

    movielist = [start_clip, seg1, seg2, det1, det2, united]

    return movielist


def generate_clip(movie):
    clip = mpy.VideoFileClip(movie['name'])
    if "seq" in movie:
        clip = clip.subclip(*movie['seq'])
    return clip


def generate_movies(movielist):
    cliplist = [generate_clip(movie) for movie in movielist]
    final_clip = mpy.concatenate_videoclips(cliplist)
    final_clip.write_videofile("/home/jasvir/Music/jodha6/MultiNet.mp4")


if __name__ == "__main__":
    main()
