import streamlit as st

#text/title
st.header("Mantra's website")
ff
#images 
from PIL import Image 
img = Image.open ("/home/linuxdom/Desktop/Dev/ZtyeaB.jpg")
st.image(img,width=300,)

#video
vid_file = open("/home/linuxdom/Desktop/Dev/20210129_144034.mp4","rb").read()
#vid_bytes = vid_file.read()
st.video(vid_file)

 
#audios

audio_file = open("/home/linuxdom/Desktop/Dev/Warriyo - Mortals (feat. Laura Brehm) [NCS Release].mp3","rb").read()
st.audio(audio_file,format="audio/mp3")

#ballons
if st.button("Activate Ballons"):
    st.balloons()


st.markdown("wesite made by Mantra.Mehta any question here is my gmail")

st.markdown("mantra@gmail.com")

st.markdown("pls do not do anything with the menu")

import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)