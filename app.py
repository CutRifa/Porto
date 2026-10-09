import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Cut Rifa Salsabil - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Menghilangkan padding & margin bawaan Streamlit
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Membaca file index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Fungsi untuk mengonversi gambar ke Base64
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            # Cek ekstensi file
            ext = image_path.split('.')[-1].lower()
            mime = "image/png" if ext == "png" else "image/jpeg"
            return f"data:{mime};base64,{encoded}"
    return ""

# Konversi foto profile.jpg jika ada
img_base64 = get_image_base64("profile.jpg") # Sesuaikan nama file foto kamu jika berbeda (misal: profile.png)

if img_base64:
    # Ganti src="profile.jpg" di HTML dengan data base64
    html_content = html_content.replace('src="profile.jpg"', f'src="{img_base64}"')

# Render HTML di Streamlit
components.html(html_content, height=1200, scrolling=True)