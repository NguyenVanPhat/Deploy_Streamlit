import streamlit as st
import wget
import os
# os.system("apt-get update && apt-get install libgl1")
from detection_helpers import *
from tracking_helpers import *
from bridge_wrapper import *
from PIL import Image
import imageio

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
detector.load_model('./yolov7x.pt')
tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

uploaded_file = st.file_uploader("Tải video lên", type=["mp4"])
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
click = st.button("Tiến hành Object Traking")
if click and (uploaded_file is None):
    st.caption("Làm ơn tải lên Video")
if click and uploaded_file is not None:
    video = imageio.get_reader(bytes_data, 'ffmpeg')
    tracker.track_video(video,
                        output="./street_input_test1.mp4", show_live=False, skip_frames=0,
                        count_objects=True, verbose=15)

st.write("đã cài thành công")
