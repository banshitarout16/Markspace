import streamlit as st
from src.components.header import header_home
from src.UI.base_layout import style_base_layout, style_background_home

def home_screen():

    header_home()

    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2,gap="large")

    with col1:
        st.header("I'm a Student")
        st.image("docs/stu_ava.jpg", width=120)
        
        if st.button("Student Portal"):
                    st.session_state["login_type"] = "student"
                    st.rerun()


    with col2:
        st.header("I'm a Professor")
        st.image("docs/teacher_av.jpg", width=120)

        if st.button("Teacher Portal"):
            st.session_state["login_type"] = "teacher"
            st.rerun()
        