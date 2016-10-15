import sys
from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)

app = QApplication(sys.argv)
text, okay = QInputDialog.getText(None, 'Project' , 'Please enter the location of your song library. (Ex:C:''\\''Users''\\''Users''\\''Desktop''\\''Library)')

path = text

onlyfiles = [join(path,f) for f in listdir(path) if isfile(join(path,f)) ]
for f in onlyfiles:

  if f.endswith(".mp3" or ".m4a"):
    print(f)    ## Lists the Filenames out as they are entered into converting.
    onlyfiles = AudioSegment.from_mp3(f)
    name = f.split(".")[0].split("\\")[-1] ## takes the name from the list to rename the
    print(path + "\\{}.wav".format(name))    ## Lists the filenames out after they have been converted.
    onlyfiles.export (path + "\\Converted\\{}.wav".format(name), format="wav") ## outputs the files into the specified directory.



