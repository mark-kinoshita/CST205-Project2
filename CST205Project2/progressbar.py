import sys
from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication, QLineEdit, QInputDialog, QLabel)
from PyQt5.QtCore import QBasicTimer

app = QApplication(sys.argv)
text, ok = QInputDialog.getText(None, 'Project' , 'Please enter the location of your song library. (Ex:C:''\\''Users''\\''Users''\\''Desktop''\\''Library)')

path = text

onlyfiles = [join(path,f) for f in listdir(path) if isfile(join(path,f)) ]
for f in onlyfiles:

  if f.endswith(".mp3" or ".m4a"):
    print(f)    ## Lists the Filenames out as they are entered into converting.
    onlyfiles = AudioSegment.from_mp3(f)
    name = f.split(".")[0].split("\\")[-1] ## takes the name from the list to rename the 
    print(path + "\\{}.wav".format(name))    ## Lists the filenames out after they have been converted.
    onlyfiles.export (path + "\\Converted\\{}.wav".format(name), format="wav") ## outputs the files into the specified directory.


  class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        
        
    def timerEvent(self, e):
      
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
