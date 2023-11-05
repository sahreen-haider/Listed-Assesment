import os
import shutil
from base64 import b64encode
from moviepy import editor as mp
import streamlit as st
import tempfile

st.title('Lip Sync Project')

temp_dir = tempfile.mkdtemp()

if st.button('Begin')

PATH_TO_YOUR_VIDEO = st.file_uploader('Please upload your Video Here: ', type=['mp4', 'avi'])

if PATH_TO_YOUR_VIDEO is not None:
    with open(os.path.join(temp_dir, PATH_TO_YOUR_VIDEO.name), 'wb') as f:
        f.write(PATH_TO_YOUR_VIDEO.getvalue())
    
    PATH_VIDEO = os.path.join(temp_dir, PATH_TO_YOUR_VIDEO.name)

st.video(PATH_VIDEO)



def get_video_resolution(video_path):
    """Function to get the resolution of a video"""
    import cv2
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(width, height)
    return (width, height)

def resize_video(video_path, new_resolution):
    """Function to resize a video"""
    import cv2
    video = cv2.VideoCapture(video_path)
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
    fps = video.get(cv2.CAP_PROP_FPS)
    width, height = new_resolution
    output_path = os.path.splitext(video_path)[0] + '_720p.mp4'
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    while True:
        success, frame = video.read()
        if not success:
            break
        resized_frame = cv2.resize(frame, new_resolution)
        writer.write(resized_frame)



video_duration = mp.VideoFileClip(PATH_VIDEO).duration
if video_duration > 600:
    print("WARNING: Video duration exceeds 600 seconds. Please upload a shorter video.")
    raise SystemExit(0)

if st.button('check resolution'):
    video_resolution = get_video_resolution(PATH_VIDEO)
    print(f"Video resolution: {video_resolution}")
    if video_resolution[0] >= 1920 or video_resolution[1] >= 1080:
        print("Resizing video to 720p...")
        os.system(f"ffmpeg -i {PATH_VIDEO} -vf scale=1280:720 /content/sample_data/input_vid.mp4")
        PATH_TO_YOUR_VIDEO = "/content/sample_data/input_vid.mp4"
        st.write("Video resized to 720p")
    else:
        st.write("No resizing needed")

