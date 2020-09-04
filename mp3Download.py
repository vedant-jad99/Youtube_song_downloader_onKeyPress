import os
import subprocess
from urllib.request import urlopen, HTTPError as he, URLError as ue
from pytube import YouTube
import tkinter as tk
from tkinter.filedialog import askdirectory
from pyperclip import paste
import pyautogui as pya 
import re

class Downloader:
    def __init__(self):
        pya.hotkey('ctrl', 'c')
        self.valid_link = False
        self.regex = re.compile(r'.+youtube.com/.+')   
        self.link = paste()
        self.checklink()
    def checklink(self):
        validity = self.regex.match(self.link)
        if validity != None:
            try:
                urlopen(self.link)
                self.valid_link = True
            except ue:
                print(ue)
            except he:
                print(he)
        else:
            print("Not a YouTube video link")
    def download_mp3(self):
        if self.valid_link:
            yt = YouTube(self.link)
            stream = yt.streams.filter(only_audio=True)[0]
            if 'mp4' in stream.mime_type:
                root = tk.Tk()
                root.withdraw()
                file_name = stream.default_filename
                download_dir = askdirectory(initialdir='/home')
                if download_dir != ():
                    audio_file = os.path.join(download_dir, file_name.split('.')[0] + '.mp3')
                    video_file = os.path.join(download_dir, file_name)
                    stream.download(download_dir)
                    subprocess.call(['ffmpeg', '-i', video_file, audio_file])
                    os.remove(video_file)