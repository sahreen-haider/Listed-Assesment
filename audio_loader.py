import os
import streamlit as st
import librosa
import soundfile as sf
import streamlit as st
from Video_loader import *
import tempfile

temp_dir_aud = tempfile.mkdtemp()

PATH_TO_YOUR_AUDIO = st.file_uploader('Choose an Audio File: ', type==['wav', 'mp3'])
if PATH_TO_YOUR_AUDIO is not None:
        with open(os.path.join(temp_dir_aud, PATH_TO_YOUR_AUDIO.name), 'wb') as f:
            f.write(PATH_TO_YOUR_AUDIO.getvalue())
        
        PATH_AUDIO = os.path.join(temp_dir_aud, PATH_TO_YOUR_AUDIO.name)

st.audio(PATH_TO_YOUR_AUDIO)


audio, sr = librosa.load(PATH_TO_YOUR_AUDIO, sr=None)

# Save audio with specified sampling rate

sf.write(PATH_TO_YOUR_AUDIO, audio, sr, format='wav')

Videoder()

