from pydub import AudioSegment
sound = AudioSegment.from_mp3("input.mp3")
sound.export ("C:\\Users\\Sam\\Desktop\\School (Present)\\CST 205-01\\output\\lolwut.wav", format="wav")