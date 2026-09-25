import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.UI.base_layout import style_base_layout, style_background_home

def home_screen():

    header_home()
    style_base_layout()
    style_background_home()
    

    col1, col2 = st.columns(2,gap="large")

    with col1:
        # st.header("I'm a Student")
        st.markdown("<h2>I'm a <span style='color:#4338CA;'>Student</span></h2>", unsafe_allow_html=True)
        st.image("docs/stud_av.png", width=120)
        st.markdown("<p style='color:#64748b; font-family:Outfit, sans-serif; font-size:14px; text-align:center;'>Join your classes, mark attendance, and keep track of your learning journey.</p>", unsafe_allow_html=True)
        
        if st.button("Student Portal", type="primary", icon=':material/arrow_forward:', icon_position='right'):
                    st.session_state["login_type"] = "student"
                    st.rerun()


    with col2:
        # st.header("I'm a Professor")
        st.markdown("<h2>I'm a <span style='color:#4338CA;'>Professor</span></h2>", unsafe_allow_html=True)
        st.image("docs/teacher_av.png", width=120)
        st.markdown("<p style='color:#64748b; font-family:Outfit, sans-serif; font-size:14px; text-align:center;'>Manage your subjects, track attendance, and engage with your students easily.</p>", unsafe_allow_html=True)

        if st.button("Teacher Portal", type="primary", icon=':material/arrow_forward:', icon_position='right'):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()
        