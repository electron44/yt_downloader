#!/bin/bash

import os 
import importlib


if not importlib.util.find_spec('pytube'):
    os.system('pip install pytube')

from pytube import YouTube, Playlist

print("(P) Download a playlist (V) Download a videos !\n")
choices = input("Faites votre choix : ")

choices = choices.lower()

if choices == "p":
    links = input("Paste the plaslist link  0w0 : ")
    playlist = Playlist(links)
    print(f"Downloading the playlist....{playlist.title} in progress!")
    for video in playlist.videos:
        video.streams.first().download('')
    print("Download finished")

else:
    links = input("Paste the links of yt videos: ")
    video = YouTube(links)
    video = video.streams.get_highest_resolution()
    print(f"Downloading the video {video.title} in progress")
    video.download('/home/devdint/Téléchargements')
    print("Download finished")
    
    


    