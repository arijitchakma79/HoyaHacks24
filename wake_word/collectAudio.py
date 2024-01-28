import pyaudio
import wave
import os
import numpy as np
from pydub import AudioSegment
from pydub.utils import make_chunks


class Listener:
    '''
    https://github.com/LearnedVector/A-Hackers-AI-Voice-Assistant/tree/master
    Highly inspired by this
    '''
    def __init__(self, input_device_index):
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.channels = 1
        self.sampleRate = 8000
        self.length = 2
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT, 
                                  channels=self.channels, 
                                  rate=self.sampleRate,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=self.chunk,
                                  input_device_index=input_device_index)

    def adjust_input_gain(self, data, gain=1.0):
        return (np.frombuffer(data, dtype=np.int16) * gain).astype(np.int16).tobytes()

    def writeAudio(self, fn, frames):
        print(f"Writing file to {fn}")
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        os.makedirs(os.path.dirname(fn), exist_ok=True)

        with wave.open(fn, "wb") as waveForm:
            waveForm.setnchannels(self.channels)
            waveForm.setsampwidth(self.p.get_sample_size(self.FORMAT))
            waveForm.setframerate(self.sampleRate)
            waveForm.writeframes(b"".join(frames))

if __name__ == "__main__":
    p = pyaudio.PyAudio()
    numdevices = p.get_device_count()
    input_device_index = 1  
    l = Listener(input_device_index)
    frames = []

    for i in range(0, numdevices):
        if p.get_device_info_by_index(i).get('maxInputChannels') > 0:
            print(f"Input Device id {i} - {p.get_device_info_by_index(i).get('name')}")

    print("One class or zero class? (1/0)")
    input = input()

    if input == "1":
        folder = "one"
    else: 
        folder = "zero"

    l.stream.start_stream()  
    try:
        for i in range(5):
            for k in range(int((l.sampleRate / l.chunk) * l.length)):
                data = l.stream.read(l.chunk)
                frames.append(l.adjust_input_gain(data, gain=16))
                print(i)

    finally:
        l.stream.stop_stream()  
        l.stream.close()
        l.p.terminate()

    savePath = os.path.join(folder, "unsplit.wav")
    l.writeAudio(savePath, frames)
    print(f"{i} samples taken")

    audio = AudioSegment.from_file(savePath)
    length = l.seconds * 1000 # this is in miliseconds
    chunks = make_chunks(audio, length)
    names = []
    for i, chunk in enumerate(chunks):
        _name = savePath.split("/")[-1]
        name = "{}_{}".format(i, _name)
        wav_path = os.path.join("one", name)
        chunk.export(wav_path, format="wav")



        
    print("Done")


