import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="EV Dashboard", layout="wide")

BASE_DIR = Path(__file__).parent
bg_image = BASE_DIR / "tab_bck.png"

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64(bg_image)

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: center;
background-attachment: fixed;
}}

h1,h2,h3,h4,h5,h6,label {{
color:white !important;
}}
</style>
""", unsafe_allow_html=True)

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.title("EV Dashboard Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid Login")

else:

    st.title("Electric Vehicle Analytics")

    page = st.selectbox(
        "Select Page",
        ["EV Charging Behavior and Infrastructure Planning Insights","EV Battery Performance and Driving Range Optimization","Comparative Analysis of Electric Vehicle Efficiency and Cost","EV Ecosystem Analysis in India"]
    )

    if page == "EV Charging Behavior and Infrastructure Planning Insights":
        url = "https://public.tableau.com/views/EV_projectD1/Dashboard2?:showVizHome=no&:embed=true"

    elif page == "EV Battery Performance and Driving Range Optimization":
        url = "https://public.tableau.com/views/EV_project_D2/Dashboard3?:showVizHome=no&:embed=true"

    elif page == "Comparative Analysis of Electric Vehicle Efficiency and Cost":
        url = "https://public.tableau.com/views/EV_project_D3/Dashboard4?:showVizHome=no&:embed=true"

    else:
        url = "https://public.tableau.com/views/EV_project_Story/EVcarsinIndia?:embed=true&:showVizHome=no"

    # ---------- Zoomed Dashboard ----------
    st.markdown(f"""
    <div style="transform: scale(1.6); transform-origin: 0 0;">
        <iframe src="{url}" width="1100" height="680"></iframe>
    </div>
    """, unsafe_allow_html=True)













