## CST 205 Project 2
## JEffrey Gearhart
## 

from os import listdir
from os.path import isfile, join
from pydub import AudioSegment

onlyfiles = [join("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test\\",f) for f in listdir("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test") if isfile(join("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test\\",f)) ]
for f in onlyfiles:

  if f.endswith(".mp3"):
    print(f)	## Lists the Filenames out as they are entered into converting.
    onlyfiles = AudioSegment.from_mp3(f)
    name = f.split(".")[0].split("\\")[-1] ## takes the name from the list to rename the 
    print("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test\\{}.wav".format(name))	## Lists the filenames out after they have been converted.
    onlyfiles.export ("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test\\{}.wav".format(name), format="wav") ## outputs the files into the specified directory.