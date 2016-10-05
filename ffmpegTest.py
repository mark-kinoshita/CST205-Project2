from pydub import AudioSegment
import os

for files in os.listdir("c:\\Users\\Kyle\\Documents\\temp"):
   for file in files:
        sound = AudioSegment.from_mp3(os.path.join("C:\\Users\\Kyle\\Documents\\temp", file))
        sound.export(os.path.join("C:\\Users\\Kyle\\Desktop\\wavSongs", file), format="wav")