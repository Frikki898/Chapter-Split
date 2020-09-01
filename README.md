# Chapter-Split
Splits mp3 audiobooks into chapters by detecting long silent pauses in the mp3 file

## Prerequisites
mutagen must be installed using pip
```
pip install mutagen
```
Python and ffmpeg must be installed
windows users must also have these programs added to path

## Useage example
```
python chapterSplitter.py nameOfAudio.mp3 3 -50
```
In this example the program will look for 3 second gaps that have -50db or lower and split on those sections
In my experience these values do a good job finding all chapter splits but occasionally some chapters are cut into the same file. Feel free to try messing around with the parameters to find values that works for you