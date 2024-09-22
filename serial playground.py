import serial
import time
import soundfile as sf
import numpy as np
import os

ser = serial.Serial()
ser.port = "COM3"
ser.baudrate = 9600

ser.open()
ser.reset_input_buffer()

i = 6
file = "red"
extension = ".wav"

while True:
    filename = "".join((file,str(i),extension))
    translated_serial = ser.readline().decode("utf-8")
    stringlist = translated_serial.split(" ")
    intlist = [int(i) for i in stringlist]
    print(intlist)
    converted_array = np.array(intlist, "int16")
    
    # Save the audio file locally
    os.chdir("C:/Users/tikop/OneDrive/Desktop/virtual environment/gdrive/audio_samples")
    print(os.getcwd())
    sf.write(filename, converted_array, 22050, "PCM_16")
    
    print("File uploaded successfully.")
    i = i + 1