import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image Capture and Upload App")

    option = st.radio("Choose an option:", ("Capture Image", "Upload Image"))

    if option == "Capture Image":
        st.sidebar.markdown("### Camera Settings")
        capture_button = st.sidebar.button("Preview Camera")

        # Create a VideoCapture object to access the camera
        cap = cv2.VideoCapture(0)

        if capture_button:
            ret, frame = cap.read()

            if ret:
                st.image(frame, caption="Camera Preview", use_column_width=True)
                st.markdown("### Capture an Image")
                if st.button("Capture"):
                    cv2.imwrite("captured_image.jpg", frame)
                    st.success("Image captured and saved as 'captured_image.jpg'")


    elif option == "Upload Image":
        uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

        if uploaded_image is not None:
            image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.markdown("### Save the Uploaded Image")
            if st.button("Save"):
                cv2.imwrite("uploaded_image.jpg", image)
                st.success("Image saved as 'uploaded_image.jpg'")

if __name__ == "__main__":
    main()
