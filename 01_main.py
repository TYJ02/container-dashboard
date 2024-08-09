import streamlit as st
import cv2 as cv
import pandas as pd

st.set_page_config(page_title="Dashboard",layout="wide")

st.title("Dashboard")
st.sidebar.success("Select a page above.")

# load our dataframe
df = pd.read_csv("container.csv")


def container_id():
    st.header("container ID")
    option = st.selectbox(label="container id", options=df.iloc[:, 2])
    time = df["timestamp"][df["id"] == option].iloc[0]
    path = df["image"][df["id"] == option].iloc[0]
    st.markdown(f" ### timestamp \n this is {time}")
    return option, path

def container_image(option, path):
    st.header("container image")
    st.write(option)
    st.image(path, width= 800)


#def rating():

def damage_count(option):
    count = df["count"][df["id"] == option].iloc[0]
    st.header("damage count")
    st.write(count)

def damage_type(option):
    damages = df[["axis","concave","dentado","perforation"]][df["id"] == option].iloc[0]
    st.header("damage type")
    st.write(damages)

    # make each damage type text clickable and then show crop image when clicked

# column
col1, col2  = st.columns(2)

with col1:
    option, path = container_id()
    damage_count(option)
    damage_type(option)
    
    

with col2:
    container_image(option, path)

if st.button("view damage"):
    img = cv.imread(f"{option}.jpg")

    image1 = img[100:500, 100:500]
    image2 = img[500:1000, 500:1000]
    image3 = img[100:1000, 100:1000]
    image_list = [image1, image2, image3]

    # set channel to BGR for opencv
    for image in image_list:
        st.image(image, channels="BGR", width=200)
st.write("hello world")

st.markdown("# Damages")


# insert image

# insert table
st.dataframe(data=df, width=10000)

# insert filter

# interactive image - click to zoom





