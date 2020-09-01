import sys
import subprocess
from mutagen.mp3 import MP3

filename = ""
silenceDuration = 4
db = -50



if(len(sys.argv) < 2):
    print("error")
else:
    filename = sys.argv[1]
    silenceDuration = float(sys.argv[2])
    db = int(sys.argv[3])
    
print("starting silence detection. this might take a few minutes for bigger audiobooks")
subprocess.check_output('ffmpeg -i "' + str(filename) + '" -af silencedetect=noise=' + str(db) + 'dB:d=' + str(silenceDuration) + ' -f null - 2> output.txt', shell=True)
print("finished writing chapter times to output.txt")

startDuration = 0
duration = 0
i = 1
f = open("output.txt", "r")
for line in f:
    if("silence_start: " in line):
        splitline = line.split("silence_start: ")
        duration = float(splitline[1]) - startDuration
        subprocess.check_output('ffmpeg -ss ' + str(startDuration) + ' -i ' + filename + ' -t ' + str(duration) + ' -c copy chap' + str(i) + '.mp3', shell=True)
        print("CREATED CHAPTER" + str(i))
        i += 1
    elif("silence_end: " in line):
        splitline = line.split("silence_end: ")
        startDuration = float(splitline[1].split(" | ")[0])

file = MP3(filename)
fileEndInSec = float(file.info.length) - 0.1

duration = fileEndInSec - startDuration
subprocess.check_output('ffmpeg -ss ' + str(startDuration) + ' -i ' + filename + ' -t ' + str(duration) + ' -c copy chap' + str(i) + '.mp3', shell=True)
print("CREATED CHAPTER" + str(i))


