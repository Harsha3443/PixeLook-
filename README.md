🧠 PixeLook – Fashion Item Classifier using Deep Learning

A deep learning–powered web app built with TensorFlow and Streamlit that predicts clothing categories from images.
Users can upload an image to get the predicted class and confidence score.

🚀 Features

Upload any clothing image

Real-time prediction using trained CNN model

Displays top class + confidence

Clean, simple Streamlit UI

Model exported as .keras file for fast inference

Modular code for easy upgrade (e.g., transfer learning, real datasets)

🗂️ Project Structure
project/
│
├── app.py                 # Streamlit application
├── fashion_cnn.keras      # Trained model
├── README.md              # Project documentation
└── requirements.txt       # Dependencies

🎯 How It Works

User uploads a clothing image

Image is preprocessed (resize → grayscale/RGB → normalization)

Model predicts using a custom-trained CNN

App returns:

Predicted class (e.g., Sneaker, Dress)

Confidence percentage

🧠 Model Details

Built using TensorFlow Keras

Architecture:

Conv2D → Conv2D → MaxPool → Dropout

Flatten

Dense → Dropout → Dense(softmax)

Trained on:

Fashion-MNIST (for simple version)

OR Polyvore / real fashion dataset (for advanced version)

🛠️ Tech Stack

Python

TensorFlow / Keras

NumPy

Streamlit

Pillow (PIL)

📦 Installation
git clone <your-repo-url>
cd project-folder
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py

🧪 Sample Usage

Upload an image such as:

A sneaker

A bag

A dress

A shirt

The app shows:
Predicted: Sneaker
Confidence: 97.23%

📊 Training Notebook

The model was trained using:

CNN architecture (for MNIST)

OR MobileNetV2/EfficientNet (for real fashion images)

Add your notebook link here:

📓 Training Notebook:(https://github.com/Harsha3443/PixeLook-/)

🖼️ Screenshots (Optional but recommended)

Add screenshots of your Streamlit UI:



🤖 Future Improvements

Upgrade to EfficientNetB0 / MobileNetV2

Deploy on Streamlit Cloud or HuggingFace Spaces

Add option to capture photo using webcam



Multi-label prediction (outfit + accessories)

Recommend outfits using embeddings

🙌 Acknowledgements

TensorFlow Team

Fashion-MNIST / Polyvore dataset

Streamlit


To view live demo:

https://pixelook.streamlit.app/
