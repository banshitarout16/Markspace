import base64

import streamlit as st

def header_home():
    with open("docs/logo.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()



    st.markdown(f"""
        <div style="
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-bottom: 30px;
            margin-top: 30px;
        ">
            <img src="data:image/png;base64,{encoded_image}" width="100">
            <h1 style="
                color: #E0E3FF;
                margin-top: 10px;
                margin-bottom: 0;
            ">MarkSpace</h1>
        </div>
        """, unsafe_allow_html=True)