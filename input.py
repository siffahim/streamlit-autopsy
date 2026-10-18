import streamlit as st

st.title("How to take input from the users")
st.divider()


name  = st.text_input("Enter your name", placeholder="Type here...");
age = st.number_input("Enter your age", placeholder="Type here...", value=None)
password = st.text_input("Enter your password", placeholder="Type here...", type="password")

pressed = st.button("Submit Here")


selected = st.selectbox("Chose your preference", 
            ("Student","Business", "Teacher"),
            index=None,
            accept_new_options=True
        )

st.write("Your selected items", selected)


if pressed:
    st.write(f"Hello {name}, your age is {age} years old.")
    st.markdown(f":red[{password}]")