import streamlit as st
import cv2 as cv

st.title("new page")
st.write("hello")
img = cv.imread("10101.jpg")

image = img[100:1000, 100:1000]

# set channel to BGR for opencv
st.image(image, channels="BGR")

# Define options for the selectbox
options = ["Option 1", "Option 2", "Option 3"]

# Initialize the session state for the selectbox if it doesn't exist
if "selected_option" not in st.session_state:
    st.session_state.selected_option = options[0]  # Default to the first option

# Function to change the selectbox state
def change_selectbox():
    st.session_state.selected_option = "Option 2"  # Change to the desired option

# Display the selectbox with the state managed by session state
selected = st.selectbox("Select an option", options, index=options.index(st.session_state.selected_option))

# Display a button that changes the selectbox state when clicked
if st.button("Change Selectbox"):
    change_selectbox()

# Show the currently selected option
st.write("You selected:", selected)

