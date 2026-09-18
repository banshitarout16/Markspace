import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_home
from src.UI.base_layout import style_background_dashboard, style_base_layout
from src.database.db import check_teacher_exists, create_teacher, teacher_login
from PIL import Image
import numpy as np 




def student_screen():

    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
       if st.button(
                   "Go back",
                   type="secondary",
                   key="loginbackbtn",
                   use_container_width=True,
                   shortcut="ctrl+b"
                   ):
                   st.session_state['login_type']= None
                   st.rerun()

     # DIVIDER
    st.markdown("""
            <div style="
                width: 100%;
                height: 1px;
                background: linear-gradient(
                    to right,
                    transparent 0%,
                    #a8a8a8 15%,
                    #a8a8a8 85%,
                    transparent 100%
                );
                margin: 5px 0 25px 0;
            "></div>
        """, unsafe_allow_html=True)   

    
    st.header('login using FaceID', text_alignment="center")
    st.space()

    # camera on for face authentication
    
    photo_source = st.camera_input("Position your face in the center")
    if photo_source:
          np.array(Image.open(photo_source))
    footer_home()