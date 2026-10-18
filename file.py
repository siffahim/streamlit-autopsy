
import streamlit as st

st.title("File uploader")
st.divider()

images = st.file_uploader("Upload you file", type=['jpg','jpeg', 'png'], accept_multiple_files=True)


if images:
    col = st.columns(len(images));
    for i, img in enumerate(images):
        with col[i]:
            st.image(img)