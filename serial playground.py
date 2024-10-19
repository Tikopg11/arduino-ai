import serial
import soundfile as sf
import numpy as np
import os

ser = serial.Serial()
ser.port = "COM6"
ser.baudrate = 9600

ser.open()
ser.reset_input_buffer()

i = 6
file = "red"
extension = ".wav"

while True:
    filename = "".join((file,str(i),extension))
    print("Filename: ", filename)
    translated_serial = ser.readline().decode("utf-8")
    print("translated serial!")
    stringlist = translated_serial.split(" ")
    stringlist[-1] = stringlist[-1].strip()
    print("Stringlist: ", len(stringlist))
    intlist = [int(i)-2**15 for i in stringlist]
    print("Intlist: ", len(intlist))
    converted_array = np.array(intlist, "int16")
    print("converted array: ", converted_array)
    print("converted array length: ", len(converted_array))

    # Save the audio file locally
    os.chdir("C:/Users/tikop/OneDrive/Desktop/microphone-data")
    print(os.getcwd())
    sf.write(filename, converted_array, 8000, "PCM_16")
    
    print("File uploaded successfully.")
    i = i + 1