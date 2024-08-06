import streamlit as st
import cv2 as cv
import pandas as pd

st.set_page_config(page_title="Dashboard",layout="wide")

st.title("Dashboard")
st.sidebar.success("Select a page above.")

# column
col1, col2  = st.columns(2)

with col1:
    st.header("container ID")
    st.write("10101")

with col2: 
    st.header("container image")
    st.image("image.png")
    if st.button("view damage"):
        st.switch_page("pages/02_new_page.py")

st.write("hello world")

st.markdown("# Damages")

col1, col2  = st.columns(2)

with col1:
    st.header("container ID")
    # coordinates
    st.write("10101")

with col2: 
    st.header("container image")
    # coordinates
    #coor = [500:1000, 500:1000]
    img = cv.imread("image.png")
    img = img[500:1000, 500:1000]
    st.image("image.png")


# insert image
st.image("image.png")

# insert table
df = pd.read_csv("container.csv")
st.dataframe(data=df)

# insert filter

# interactive image - click to zoom

# Function to handle page navigation
def navigate():
    st.navigation(new_page)





