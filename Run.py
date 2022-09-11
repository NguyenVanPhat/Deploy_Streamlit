import os
import wget
import imageio
import streamlit as st
import cv2
import tempfile

# os.system("streamlit run home.py")
# wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
# phat_test()
uploaded_file = st.file_uploader("Tải video lên", type=["mp4"])
if uploaded_file is not None:
    st.write(uploaded_file.name)
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    vf = cv2.VideoCapture(tfile.name)
    fps = vf.get(cv2.CAP_PROP_FPS)
    st.write(int(fps))
