import streamlit as st
import os
import wget

st.set_page_config(
    page_title="Get Video Random",
    page_icon="💽",
)
st.markdown("<h1 style='text-align: center; color: red;'>🎥 Get Video Random 📀</h1>", unsafe_allow_html=True)
st.header('')
st.header('')
path = ""
# os.system("wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
print("Đã chạy được Wget")
