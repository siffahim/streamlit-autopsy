from google import genai
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)

st.markdown(interaction.output_text)

#deprecated
#res = client.models.generate_content(
 #   model="gemini-3.8-flash",
#    contents="Give me a idea about mcp between in 100 words"
#)


#print(res.text)