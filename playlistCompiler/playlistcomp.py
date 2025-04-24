import os
from glob import glob
from pydub import AudioSegment

def determine_format(audio_dir):
    #we're going to see whether to export the file as a flac, mp3, or wav, depending on which is most popular. default is mp3
    format = "mp3"

    flac_count = 0
    wav_count = 0
    mp3_count = 0

    for file in os.listdir(audio_dir):
        if file.endswith('.flac'):
            flac_count = flac_count + 1
        elif file.endswith('.wav'):
            wav_count = wav_count + 1
        else:
            mp3_count = mp3_count + 1
    
    if flac_count > wav_count and flac_count > mp3_count:
        format = "flac"
    if wav_count > flac_count and wav_count > mp3_count:
        format = "wav"

    return format

#Get current directory
audio_dir = os.path.dirname(os.path.abspath(__file__))
print(audio_dir)
exportname = str(input("What would you like to name the file? \n"))

#Compile list of eligibile audios
audiofiles = []
for file in os.listdir(audio_dir):
    #print(file)
    if file.endswith(('.flac', '.mp3', '.wav')):
        print(file)
        audiofiles.append(AudioSegment.from_file(audio_dir + '\\' + file))

if len(audiofiles) == 0:
    FileNotFoundError("There are no eligible audio files in this folder!")

#Merge all songs into one file
playlist = audiofiles.pop(0)
for song in audiofiles:
    playlist = playlist.append(song, crossfade=(2 * 1000))
    print("added to playlist!")
    print(len(playlist))

print(len(playlist))

#Export
correct_format = determine_format(audio_dir)
with open(audio_dir + '\\' + exportname + "." + correct_format, 'wb') as out_f:
    playlist.export(out_f, format=correct_format)

print("Done!")