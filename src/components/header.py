import base64
import streamlit as st

# def header_home():
#     with open("docs/logo.png", "rb") as image_file:
#         encoded_image = base64.b64encode(image_file.read()).decode()

#     st.markdown(f"""
# <div style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:15px; margin-top:10px;">
# <img src="data:image/png;base64,{encoded_image}" width="140" style="display:block; object-fit:contain; margin-bottom:-10px;">
# <h1 style="font-size:2.2rem !important; margin-top:5px; margin-bottom:0; background:linear-gradient(90deg, #FFFFFF, #C7D2FE); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">MarkSpace</h1>
# <p style="color:#D8DCFB; font-family:'Outfit', sans-serif; font-size:14px; margin-top:2px;">Smart attendance. Simple tracking. Better learning.</p>
# </div>
# """, unsafe_allow_html=True)

def header_home():
    with open("docs/logo.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
<style>
@keyframes ms-shimmer {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}
@keyframes ms-fadein {{
    from {{ opacity: 0; transform: translateY(6px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
.ms-logo-wrap {{
    position: relative;
    display: inline-block;
}}
.ms-logo-glow {{
    position: absolute;
    inset: -18px;
    background: radial-gradient(circle, rgba(255,255,255,0.35), transparent 70%);
    filter: blur(12px);
    z-index: 0;
}}
.ms-logo-img {{
    position: relative;
    z-index: 1;
}}
.ms-title {{
    font-size: 3.9rem !important;
    margin-top: 8px;
    margin-bottom: 0;
    background: linear-gradient(90deg, #FFFFFF, #FFD98A, #FFFFFF);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: ms-shimmer 4s ease-in-out infinite;
}}
.ms-tagline {{
    color: #E8EAFB;
    font-family: 'Outfit', sans-serif;
    font-size: 13px;
    letter-spacing: 1.3px;
    text-transform: uppercase;
    font-weight: 500;
    margin-top: 5px;
    opacity: 0.85;
    animation: ms-fadein 0.8s ease-out;
}}
</style>
<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; margin-bottom:15px; margin-top:10px;">
<div class="ms-logo-wrap">
<div class="ms-logo-glow"></div>
<img class="ms-logo-img" src="data:image/png;base64,{encoded_image}" width="150" style="display:block; object-fit:contain;">
</div>
<h1 class="ms-title">MarkSpace</h1>
<p class="ms-tagline">Smart attendance. Simple tracking. Better learning.</p>
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