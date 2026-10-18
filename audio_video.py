import streamlit as st

st.title("Audio & Video")
st.divider()

#audio locations
st.audio("media/football.mp3", loop=True)

#audio upload
upload_audio = st.file_uploader("Upload your audio", 
                 type=["mp3","ogg", "flac"]
    )
if upload_audio:
    st.audio(upload_audio)


#video 
st.title("Video")
st.divider()

uploaded_video = st.file_uploader("Upload your video", type=["mp4","mvk"])

button = st.button("Click to upload");

if button:
    if uploaded_video:
        st.video(uploaded_video)
        st.success("Video upload successfully")
    else:
        st.error("Please chose a video file!!!!!!!")
