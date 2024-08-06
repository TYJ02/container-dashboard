import streamlit as st
import cv2 as cv
import pandas as pd

st.set_page_config(page_title="Dashboard",layout="wide")

st.title("Dashboard")
st.sidebar.success("Select a page above.")

# load our dataframe
df = pd.read_csv("container.csv")

# column
col1, col2  = st.columns(2)

with col1:
    st.header("container ID")
    st.write("10101")
    option = st.selectbox(label="container id", options=df.iloc[:,2])

with col2: 
    st.header("container image")
    st.write(option)
    st.image(f"{option}.jpg")
        #st.switch_page("pages/02_new_page.py")


if st.button("view damage"):
    img = cv.imread(f"{option}.jpg")

    image = img[100:1000, 100:1000]

    # set channel to BGR for opencv
    st.image(image, channels="BGR", width=500)
st.write("hello world")

st.markdown("# Damages")


# insert image

# insert table
st.dataframe(data=df, width=10000)

# insert filter

# interactive image - click to zoom





