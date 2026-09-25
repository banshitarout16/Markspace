import base64
import streamlit as st

def header_home():
    with open("docs/logo.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:15px; margin-top:10px;">
<img src="data:image/png;base64,{encoded_image}" width="140" style="display:block; object-fit:contain; margin-bottom:-10px;">
<h1 style="font-size:2.2rem !important; margin-top:5px; margin-bottom:0; background:linear-gradient(90deg, #FFFFFF, #C7D2FE); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">MarkSpace</h1>
<p style="color:#D8DCFB; font-family:'Outfit', sans-serif; font-size:14px; margin-top:2px;">Smart attendance. Simple tracking. Better learning.</p>
</div>
""", unsafe_allow_html=True)
    

def header_dashboard():
    with open("docs/logo.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
<div style="display:flex;align-items:center;gap:10px;">
<img src="data:image/png;base64,{encoded_image}" width="130">
<div style="font-family:'Titan One';font-size:35px;color:#3f4aba;line-height:1;">
Mark</br>Space
</div>
</div>
""", unsafe_allow_html=True)