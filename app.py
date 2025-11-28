import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO


@st.cache_resource
def load_model():
    fac = tf.keras.models.load_model("fashion_cnn.keras")
    return fac


model = load_model()

class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

st.title("PixeLook")
st.markdown("Predicts confidence level of each fashion item after uploading an image")

uploaded_file = st.file_uploader("Upload a clothing image", type=["jpg", "jpeg", "png"])

if uploaded_file is None:
    st.info("Please upload an image,\n **Prefer black-and-white, silhouette, or line-art / icon-style images**\n **Avoid complex photos, people wearing clothes, backgrounds, shadows**")
else:
    file_bytes = uploaded_file.read()
    st.image(file_bytes, caption="Uploaded Image", use_column_width=True)

    def preprocess_image(image_bytes):
        img = Image.open(BytesIO(image_bytes))
        img = img.convert("L")
        img = img.resize((28, 28))
        img_array = np.array(img).astype("float32") / 255.0
        img_array = np.expand_dims(img_array, axis=-1)   # (28, 28, 1)
        img_array = np.expand_dims(img_array, axis=0)    # (1, 28, 28, 1)
        return img_array

    if st.button("Predict"):
        processed = preprocess_image(file_bytes)
        pred = model.predict(processed)

        index = np.argmax(pred[0])
        confidence = np.max(pred[0])
        label = class_names[index]

        st.success(f"Predicted: {label}")
        st.write(f"Confidence: {confidence * 100:.2f}%")
