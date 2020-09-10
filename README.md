# Youtube_song_downloader_onKeyPress

## Inspiration
I like listening to music. While there are lots of online apps for listening to apps, I sometimes like to download the songs that I really like and save them on my device. But it is always a pain to download the songs. Search all the websites for that songs, look for download links, etc., is too much work for lazy people like me. Wouldn't it be awesome to just press a few keys and boom!! the song you want is downloaded!

## Why YouTube?
YouTube is a platform where you get almost every video and songs in the digital media. Whatever song you want, if you know you just to search it. And viola! You can see it or hear it. That's why I am downloading songs from YouTube.

## What is the project?
So basically it consists of a python module which I have coded which consists of a Downlaoder class, which will download the YouTube video. The downloaded video is then converted to audio using ffmpeg converter, which can be downloaded from linux terminal using the command
`sudo apt install ffmpeg`
Before downloading the application asks the directory where you want to store the song. The application is run via a shell script, containing the path to the python program. The script is set in a kayboard to run when I press the keys. In my machine the shortcut is `Ctrl + Alt + S`

## Conclusion
The application testing and working is successful. My favorite songs are now downlaoded and stored in my laptop. 
