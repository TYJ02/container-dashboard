import streamlit as st
import cv2 as cv

st.title("new page")
st.write("hello")
img = cv.imread("image.png")

image = img[100:1000, 100:1000]

# set channel to BGR for opencv
st.image(image, channels="BGR")

