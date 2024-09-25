import streamlit as st
import cv2 as cv
import pandas as pd
import sqlite3

st.set_page_config(page_title="Dashboard",layout="wide")

st.title("Dashboard")
st.sidebar.success("Select a page above.")

# load our dataframe
df = pd.read_csv("container.csv")
dm = pd.read_csv("damage.csv")

# load sql database
con = sqlite3.connect('database.db')
cur = con.cursor()
res = cur.execute("SELECT * FROM Containers")
container = res.fetchall()
res = cur.execute("SELECT * FROM Damages")
damage = res.fetchall()
res = cur.execute("SELECT * FROM Inspection")
time = res.fetchall()
damagedf = pd.DataFrame(damage, columns =["damage_id", "container_id", "timestamp", "damage_type", "location"])
timedf = pd.DataFrame(time, columns =["inspect_id", "container_id", "timestamp", "img_path"])

option = ''
path = ''


def container_id():
    global option
    options = [item[0] for item in container]
    print(options)
    if "selected_option" not in st.session_state:
        st.session_state.selected_option = options[0]  # Default to the first option
    option = st.selectbox(label="container id", options=options, index = options.index(st.session_state.selected_option))
    if st.button("prev"):
        current = options.index(option)
        option = options[current - 1]
        st.session_state.selected_option = option
    if st.button("next"):
        current = options.index(option)
        option = options[current + 1]
        st.session_state.selected_option = option
    #option = st.select_slider(label="container id", options=df.iloc[:, 2])
    print(option)
    timestamp = timedf["timestamp"][timedf["container_id"] == option].iloc[0]
    path = timedf["img_path"][timedf["container_id"] == option].iloc[0]
    print(path)
    return option, path


def container_image(option, path):
    st.header("container image")
    st.write(option)
    try:
        st.image(path, use_column_width=True)
    except :
        st.write("no image found")


def inspect_date(option):
    options = timedf["timestamp"][timedf["container_id"] == option].iloc[:]
    print(options)
    if "selected_option" not in st.session_state:
        st.session_state.selected_option = options[0]  # Default to the first option
    time = st.selectbox(label="timestamp", options=options, index=None, placeholder="select datetime") # index = options.index(st.session_state.selected_option
    st.write(time)
    return time
    

#def rating():

def damage_count(option):
    count = df["count"][df["id"] == option].iloc[0]
    st.header("damage count")
    st.write(count)

def damage_type(option):
    damages = df[["axis","concave","dentado","perforation"]][df["id"] == option].iloc[0]
    st.header("damage type")
    col3, col4, col5, col6 = st.columns(4)
    label = ["axis", "concave", "dentado", "perforation"]
    col3.metric(label=label[0], value = damages[0])
    col4.metric(label=label[1], value = damages[1])
    col5.metric(label=label[2], value = damages[2])
    col6.metric(label=label[3], value = damages[3])

    # make each damage type text clickable and then show crop image when clicked



# column
col1, col2  = st.columns(2)

with col1:
    option, path = container_id()
    timestamp = inspect_date(option)
    #damage_count(option)
    #damage_type(option)
    

with col2:
    container_image(option, path)
    #st.metric(label="current", value = option)
    #st.markdown(f" ### timestamp \n this is {timestamp}")




if st.button("view damage"):
    img = cv.imread(f"{option}.jpg")
    print(dm["id"] == option)
    coor = dm[["location"]][dm["id"] == option]['location']
    print(coor)
    image_list = []
    for box in coor:
        coor_list = box.split('-')
        print(f'coordinates:  {coor_list}')
        print(f'first coordinate: {coor_list[0]}')
        x = int(coor_list[0])
        y = int(coor_list[1])
        w = int(coor_list[2])
        h = int(coor_list[3])
        print(x,y,w,h)
        image = img[y-h:y+h, x-w:x+w]
        image_list.append(image)
        print(len(image_list))

    # set channel to BGR for opencv
    columns = st.columns(len(image_list))
    print(columns)
    
    for i,pic in enumerate(columns):
        with pic:
            st.image(image_list[i], channels="BGR", width=True)
st.write("hello world")

st.markdown("# Damages")
st.write(f'{option} and {timestamp}')

damage = damagedf[(damagedf['container_id']==option) & (damagedf['timestamp'] == timestamp)]

st.dataframe(damage, use_container_width=True)
# insert image

# insert table

# insert filter

# interactive image - click to zoom
st.markdown("# History")

st.dataframe(damagedf[(damagedf['container_id']==option)] , use_container_width=True)





