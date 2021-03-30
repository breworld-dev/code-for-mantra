import streamlit as st

#text/title
st.header("streamlit")

#header/subheader
st.header("this is header")
st.subheader("this is a subheader")

#text
st.text("hello streamlit")

#markdown
st.markdown("### this is a  markdown")

#error/colourful
st.success("successful")

st.info("informtion")

st.warning("this is a warning")

st.error("this is a error danger")

#st.exception("nameerror('name three not difined')")

#get help info about python
st.help(range(10)) 

#images 
from PIL import Image
img = Image.open ("/home/linuxdom/Desktop/Dev/IMG_20210114_112238.jpgs")
st.image(img,width=300,caption="AI/ML")

# video 
vid_file = open("/home/linuxdom/Desktop/Dev/for dad's birthday.mp4","rb").read()
#vid_bytes = vid_file.read()
st.video(vid_file)

#audio
audio_file = open("/home/linuxdom/Desktop/Dev/tts for dad.mp3","rb").read()
st.audio(audio_file,format="audio/mp3")

#widget
#checkbox
if st.checkbox("show/hide"):
    st.text("hey there welcome back :D")
    
#radio
status = st.radio("what is your status",("Active","inActive"))

if status == "Active":
    st.success("Active")
else:
    st.warning("inActive, Activate it bro :D")

#selectbox 
occupation = st.selectbox("your occupation",["programmer","datescientist","doctor","businessman"])
st.write("you selected this option ",occupation)

# multiselect
location = st.multiselect("where do you work?",("london","new york","Accra","kiev","nepal"))
st.write("you selected", len(location),"locations")

#slider
level = st.slider("what is your level",1,5,)

#button
st.button("simple button")

if st.button("about"):
    st.text("streamlit is a cool")
#text input 
firstname = st.text_input ("enter your firstname","type here..")
if st.button("submit"):
    result = firstname.title()
    st.success(result)

#text area
message = st.text_area ("enter your message","type here..")
if st.button("submit now"):
    message = message.title()
    st.success(message)

#date input 
import datetime
today = st.date_input("today is", datetime.datetime.now())

#time
the_time = st.time_input("the time is", datetime.time()) 

#display json 
st.text("display json")
st.json({'name':"jesse","gender":"male"})

#display raw code
st.text("display raw code")
st.code("import numpy as np")

#display raw code
with st.echo():
    #this will also show as a comment
    import panda as pd 
    df = pd.DataFrame()

#progress bar 
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

#spinner
with st.spinner("wating.."):
    time.sleep(5)
st.success("finished!")

#ballons
if st.button("Activate Ballons"):
    st.balloons()