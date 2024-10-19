import soundfile as sf
import numpy as np
import os
os.chdir("C:/Users/tikop/OneDrive/Desktop/audio_samples")
print(os.getcwd())
array = np.random.rand(16000,1)
print(array)
sf.write('stereo_file.wav', array, 8000, 'PCM_16')