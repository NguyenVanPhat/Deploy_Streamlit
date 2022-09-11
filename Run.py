import os
import wget
import imageio
import streamlit as st

# os.system("streamlit run home.py")
# wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
# phat_test()
uploaded_file = st.file_uploader("Tải video lên", type=["mp4"])
# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
# video = imageio.get_reader(bytes_data, 'ffmpeg')