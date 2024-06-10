import streamlit as st
# importing Image from librry pillow (PIL) which comes in default with streamlit installation as a dependancy
from PIL import Image

# adding an extension button for "start Camera"
with st.expander("Start Camera"):
    # start the webcam
    camera_image = st.camera_input("Camera")

if camera_image:
    # creating a PIL instance
    img = Image.open(camera_image)

    # here "L" represents the algorithm required for converting colored pillow image to gray image.
    gray_img = img.convert("L")

    # render the greyscale image on the streamlit webpage
    st.image(gray_img)
