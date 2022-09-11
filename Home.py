import streamlit as st
import wget
import os
# os.system("lshw -C video")
# import tensorflow as tf
# print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
from detection_helpers import *
from tracking_helpers import *
from bridge_wrapper import *
from PIL import Image
import tempfile
import cv2

st.set_page_config(
    page_title="web app of phat",
    page_icon="💽",
)
st.markdown("<h1 style='text-align: center; color: red;'>🎥 Web App of Phat 📀</h1>", unsafe_allow_html=True)
st.header('')
st.header('')
path = ""

# os.system("wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")


uploaded_file = st.file_uploader("Tải video lên", type=["mp4"])
if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    vf = cv2.VideoCapture(tfile.name)
    st.write(type(vf))
# click = st.button("Tiến hành Object Traking")
# detector = Detector()
# detector.load_model('./yolov7x.pt')
# tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)


# if click and (uploaded_file is None):
#     st.caption("Làm ơn tải lên Video")
# if click and uploaded_file is not None:

#     tracker.track_video(video,
#                         output="./street_input_test1.mp4", show_live=False, skip_frames=0,
#                         count_objects=True, verbose=15)


