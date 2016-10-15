Authors: Mark Kinoshita, Jeff Gearhart, Kyle Butler-Fish

Last updated: 10/14/16


How it works:

	Takes a directory of mp3 files, converts them to wav format, and 
	saves them in a new directory. After successful convertion, the program traverses
	through the new directory of wav files, and creates and stores fingerprints of
	each song. Then, a fingerprint is made of a new unknown wav file and this fingerprint
	is checked against the database of existing fingerprints to determine the title
	of the unknown song.


How to use:

	Install resound, scipy, and pydub.
	The entire program runs in the recognizer.py file.
	Change the path in the onlyfiles variable to the path of your existing
	mp3 directory. In the convertDirectory function, change the export path to a new
	directory where you want to store your new wav files. Lastly change the read file
	in getNewSongFingerprint funtion to the path of your unknown wav file and run.


Future work:

	Will implement functionality to take input from mic and identify the song.
	Also will add ability to print out how many times it was recently played by the local
	radio stations.


Github repository: https://github.com/mkinoshita22/CST205-Project2