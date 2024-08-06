import streamlit as st
#import cv2 as cv
import pandas as pd

st.set_page_config(page_title="Dashboard",layout="wide")

st.title("Dashboard")
st.sidebar.success("Select a page above.")

# column
#col1, col2 = st.columns(2)

#with col1:
    #st.header("container ID")
    #st.write("10101")
#
#with col2:
    #st.header("container image")
    #st.image("image.png")

st.write("hello world")
if st.button("Home"):
    st.switch_page("02_new_page.py")

st.markdown("hello **from** *python*")

st.write("hello")

# insert image

# insert table
df = pd.read_csv("container.csv")
st.dataframe(data=df)
# insert filter

# interactive image - click to zoom

# Function to handle page navigation





