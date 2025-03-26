import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Authenticate with Gemini API
genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit App
st.title("🖼️ Image-to-Text with Gemini")

# Upload image
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    prompt = st.text_input("📝 Optional Prompt (or leave blank):", value="Describe the image")

    if st.button("🔍 Analyze Image"):
        with st.spinner("Generating description..."):
            try:
                response = model.generate_content(
                    [prompt, image],
                    stream=False
                )
                st.success("✅ Generated Description:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")
