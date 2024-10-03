import streamlit as st
import cv2 as cv
import pandas as pd
import sqlite3
from datetime import datetime
import createpdf 

st.set_page_config(page_title="Dashboard",layout="wide")

st.title("Container Inspection Dashboard")
st.sidebar.success("Select a page above.")

# load sql database
con = sqlite3.connect('database.db')
cur = con.cursor()
res = cur.execute("SELECT * FROM Containers")
container = res.fetchall()
res = cur.execute("SELECT * FROM Damages")
damage = res.fetchall()
res = cur.execute("SELECT * FROM Inspection")
time = res.fetchall()
con.close()
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
    st.header('Container ID')
    option = st.selectbox(label="Select", options=options, index = options.index(st.session_state.selected_option))
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
    try:
        timestamp = timedf["timestamp"][timedf["container_id"] == option].iloc[0]
        path = timedf["img_path"][timedf["container_id"] == option].iloc[0]
    except IndexError:
        print('no data available')
        path = None
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
    st.header('Date - Time')
    time = st.selectbox(label="timestamp", options=options, index=None, placeholder="select datetime") # index = options.index(st.session_state.selected_option
    st.write(time)
    return time

def container_grade(option, timestamp)
    grade = timedf['grade'][(timedf['container_id']==option) & (timedf['timestamp'] == timestamp)].iloc[0]
    st.metric(label="grade", value = grade)
    #st.markdown(f" ### timestamp \n this is {timestamp}")


damage = damagedf[(damagedf['container_id']==option) & (damagedf['timestamp'] == timestamp)]
# interactive image - click to zoom
st.markdown("# History")

def history(option):
    time = timedf[['timestamp','inspect_id']][(timedf['container_id']==option)].set_index('timestamp') 
    damage = damagedf[['timestamp','damage_id','location','damage_type']][(damagedf['container_id']==option)].set_index('timestamp')  
    joint = time.join(damage, lsuffix='_inspect', rsuffix='_dmg')
    #st.dataframe(time , use_container_width=True)
    #st.dataframe(damage , use_container_width=True)
    st.dataframe(joint , use_container_width=True)

history(option)




