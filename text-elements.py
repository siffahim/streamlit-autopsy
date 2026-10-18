import streamlit as st


st.title("My First Streamlit App", anchor=False)

st.divider()

st.write("Hello, welcome to my Streamlit app!");
st.text("Hey")
st.header("This is a header")

st.subheader("This sub header", divider=True)

st.caption("This is a caption")


st.markdown(":blue-background[:red[***Hello***] **World**] :balloon:")
