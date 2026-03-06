import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="EV Dashboard", layout="wide")

# ---------- Paths (GitHub friendly) ----------
BASE_DIR = Path(__file__).parent
IMG_DIR = BASE_DIR / "images"

bg_image = IMG_DIR / "tab_bck.png"
d1 = IMG_DIR / "WhatsApp Image 2026-03-05 at 2.47.05 AM.jpeg"
d2 = IMG_DIR / "WhatsApp Image 2026-03-05 at 5.01.53 AM.jpeg"
d3 = IMG_DIR / "WhatsApp Image 2026-03-05 at 7.33.42 AM.jpeg"

# ---------- Background ----------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64(bg_image)

st.markdown(
    f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: center;
background-attachment: fixed;
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- Login ----------
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid login")

else:
    st.title("Electric Vehicle Analytics")

    dashboard = st.selectbox(
        "Select Dashboard",
        ["Dashboard 1", "Dashboard 2", "Dashboard 3"]
    )

    if dashboard == "Dashboard 1":
        st.image(d1, use_container_width=True)

    elif dashboard == "Dashboard 2":
        st.image(d2, use_container_width=True)

    elif dashboard == "Dashboard 3":
        st.image(d3, use_container_width=True)

