import streamlit as st
import wget
import os
# os.system("apt-get update && apt-get install libgl1")
from detection_helpers import *
from tracking_helpers import *
from bridge_wrapper import *
from PIL import Image

st.set_page_config(
    page_title="web app of phat",
    page_icon="💽",
)
st.markdown("<h1 style='text-align: center; color: red;'>🎥 Get Video Random 📀</h1>", unsafe_allow_html=True)
st.header('')
st.header('')
path = ""

# os.system("wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
detector = Detector()
detector.load_model('./yolov7x.pt',)
st.write("đã cài thành công")
