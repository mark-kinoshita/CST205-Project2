"""
(this is what the code should be --- we cannot run it due to inability to install resound)
(the code to convert the directory to .wav works)

File:     recognizer.py
Abstract: Converts all songs in directory to .wav. Fingerprints all songs and stores
          fingerprints. Finally takes in an audio file and checks its fingerprint
          against the fingerprints in our storage and outputs whether it recognizes
          the song and if so, outputs what song it is.
Course:   CST205
Authors:  Kyle Butler-Fish, Jeff Gearhart, Mark Kinoshita
Date:     10/14/16
"""

from os import listdir
import resound
from scipy.io import wavfile
from os.path import isfile, join
from pydub import AudioSegment

onlyfiles = [join("C:\\Users\\Kyle\\Documents\\temp\\", f) for f in listdir("C:\\Users\\Kyle\\Documents\\temp") if
                 isfile(join("C:\\Users\\Kyle\\Documents\\temp\\", f))]

def convertDirectory():
    #Converts the entire directory of .mp3 files to .wav format and stores the new files
    for f in onlyfiles:
      if f.endswith(".mp3"):
        print(f)	## Lists the Filenames out as they are entered into converting.
        onlyfiles = AudioSegment.from_mp3(f)
        name = f.split(".")[0].split("\\")[-1] ## takes the name from the list to rename the
        print("C:\\Users\\Kyle\\Documents\\temp\\{}.wav".format(name))	## Lists the filenames out after they have been converted.
        onlyfiles.export ("C:\\Users\\Kyle\\Desktop\\wavSongs\\{}.wav".format(name), format="wav") ## outputs the files into the specified directory.

def fingerprintDirectory():
    #creates fingerprints for all .wav files in directory
    for f in onlyfiles:
        sample_rate, data = wavfile.read(f)
        hashes = list(resound.hashes(data, freq=sample_rate))

def getNewSongFingerprint():
    #fingerprints the unknown song to be identified
    sample_rate, data = wavfile.read('unknown.wav')
    return resound.hashes(data, freq=sample_rate))

def checkFingerprint(newFingerprint):
    #checks if the new song fingerprint exists in our database of fingerprints
    for fp in hashes:
        if newFingerprint == fp:
            return True

    return False

def main:
    #convertDirectory() //only convert once
    fingerprintDirectory()
    newFingerprint = getNewSongFingerprint()

    if(checkFingerprint(newFingerprint)):
        for fp in hashes:
            if newFingerprint == fp:
                print("Unkown song title: " + hashes.title)
    else:
        print("Song does not exist in database")

main()