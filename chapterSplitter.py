import sys
import subprocess

filename = ""
silenceDuration = 3
db = -50
if(len(sys.argv) < 2):
    print("first parameter must be name of file to split")
    print("example 'python bookname.mp3'")
if(len(sys.argv) < 3):
    print("using default parameter values")
    print("""
silenceDuration = 3
db = -50
""")
else:
    filename = sys.argv[1]
    silenceDuration = int(sys.argv[2])
    db = int(sys.argv[3])
print("starting silence detection. this might take a few minutes for bigger audiobooks")
subprocess.check_output('ffmpeg -i "' + str(filename) + '" -af silencedetect=noise=' + str(db) + 'dB:d=' + str(silenceDuration) + ' -f null - 2> output.txt', shell=True)
print("finished writing chapter times to output.txt")

startDuration = 0
duration = 0
i = 1
f = open("output.txt", "r")
bookname = filename.split(".mp3")[0]
for line in f:
    if("silence_start: " in line):
        splitline = line.split("silence_start: ")
        duration = float(splitline[1]) - startDuration
        subprocess.check_output('ffmpeg -ss ' + str(startDuration) + ' -i hod.mp3 -t ' + str(duration) + ' -c copy ' + bookname + '_chap' + str(i) + '.mp3', shell=True)
        print("CREATED CHAPTER" + str(i))
        i += 1
    elif("silence_end: " in line):
        splitline = line.split("silence_end: ")
        startDuration = float(splitline[1].split(" | ")[0])







