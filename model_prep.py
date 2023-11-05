import os
import subprocess
from Video_loader import *
from audio_loader import *



# Set up paths and variables for the output file
output_file_path = 'output/result_voice.mp4'

# Delete existing output file before processing, if any
if os.path.exists(output_file_path):
    os.remove(output_file_path)

pad_top =  st.slider(label='pad top', min_value=0, max_value=100, step=10)
pad_bottom =  st.slider(label='pad bottom', min_value=0, max_value=100, step=10)
pad_left =  st.slider(label='pad left', min_value=0, max_value=100, step=10)
pad_right =  st.slider(label='pad right',min_value=0, max_value=100, step=10)
rescaleFactor =  st.slider(label='rescale factor', min_value=0, max_value=100, step=1)
nosmooth = st.checkbox(label='No Smoothing of Video output', options=[True, False])

use_hd_model = st.selectbox(label='HD model', options=[True, False])
checkpoint_path = 'pretained_models/wav2lip.pth' if not use_hd_model else 'pretained_models/wav2lip_gan.pth'


cmd_1 = f'python Wav2Lip/inference.py --checkpoint_path $checkpoint_path --face "{PATH_VIDEO}" --audio "/Users/sahreenhaider/Downloads/input__audio.wav" --pads $pad_top $pad_bottom $pad_left $pad_right --resize_factor $rescaleFactor'
cmd_2 = f'Wav2lip/python inference.py --checkpoint_path $checkpoint_path --face "{PATH_VIDEO}" --audio "/Users/sahreenhaider/Downloads/input__audio.wav" --pads $pad_top $pad_bottom $pad_left $pad_right --resize_factor $rescaleFactor --nosmooth'


if nosmooth == False:
    process = subprocess.Popen(cmd_1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    st.video(output)

else:
    process = subprocess.Popen(cmd_2, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    st.write(output, error)