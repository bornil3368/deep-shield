import streamlit as st
from PIL import Image
import io
import time
import random

# ============================================================
# 🛡️ DeepShield - Anti Deepfake Detector (Demo Version)
# ============================================================

# --- Page Configuration ---
st.set_page_config(
    page_title="DeepShield - Anti Deepfake Detector",
    page_icon="🛡️",
    layout="centered"
)

# --- Header ---
st.title("🛡️ DeepShield: Anti Deepfake Detector")
st.markdown("""
### AI-Powered Fake Media Detection  
Protecting truth in the age of digital deception.
""")

# --- Sidebar Info ---
st.sidebar.header("About DeepShield")
st.sidebar.info("""
**DeepShield** is an AI-based platform designed to detect **AI-generated or manipulated images and videos** in real time.
This demo showcases how the system identifies fake vs. real content.
""")

# --- Simulated Deepfake Detector ---
def fake_detector(image_bytes):
    verdict = random.choice(["🟩 Authentic", "🟥 Deepfake"])
    score = round(random.uniform(75, 99), 2)
    return verdict, score

# --- Upload Section ---
uploaded_files = st.file_uploader(
    "📤 Upload an image (JPG, PNG, JPEG)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded: {uploaded_file.name}", use_container_width=True)

        # Simulate AI analysis time
        with st.spinner("🔍 Analyzing image..."):
            time.sleep(2)
            verdict, score = fake_detector(uploaded_file.read())

        # Display result
        st.markdown(f"### **Result:** {verdict}")
        st.progress(score / 100)
        st.write(f"**Confidence:** {score}%")

        if verdict == "🟥 Deepfake":
            st.warning("⚠️ Potentially AI-generated or manipulated content detected.")
        else:
            st.success("✅ This image appears authentic.")

        st.divider()

# --- Footer ---
st.markdown("""
---
**DeepShield AI © 2025**  
Empowering truth. Defending authenticity.
""")
