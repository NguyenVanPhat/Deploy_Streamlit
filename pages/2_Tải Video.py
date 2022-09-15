import streamlit as st
import gc

with open("./haha.mp4", "rb") as file:
    btn = st.download_button(
        label="Download",
        data=file,
        file_name="result_video.mp4",
        mime="mp4"
    )
file.close()
file = None
for name in dir():
    # st.write("Name: ", name)
    if not name.startswith('_'):
        del globals()[name]
gc.collect()
# gc.collect(generation=1)
# gc.collect(generation=2)
