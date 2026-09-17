import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_home
from src.UI.base_layout import style_background_dashboard, style_base_layout


def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()




    # # HEADER ROW
    # c1, c2 = st.columns(
    #     [5, 2],
    #     vertical_alignment="center",
    #     gap="xlarge"
    # )

    # with c1:
    #     header_dashboard()

    # with c2:
    #     st.button(
    #         "Go back",
    #         type="secondary",
    #         key="loginbackbtn",
    #         use_container_width=True,
    #         shortcut="ctrl+b"
    #     )

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

    # # TITLE
    # st.markdown("""
    #     <div style="
    #         color: #202038;
    #         font-family: 'Titan One', cursive;
    #         font-size: 30px;
    #         line-height: 1;
    #         margin: 0;
    #         padding: 0;
    #     ">
    #         Register your teacher account
    #     </div>
    # """, unsafe_allow_html=True)



def teacher_screen_login():
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

    st.header('login using password', text_alignment="center")
    st.space()

    teacher_username = st.text_input("Enter username", placeholder ='Hardin Scott')
    teacher_pass = st.text_input("Enter password", placeholder ='Enter password', type="password")  

    st.divider()  

    btnc1, btnc2=st.columns(2)
    with btnc1:
        st.button(
            "Login",
            icon=':material/passkey:', 
            shortcut='control+enter',
            width = "stretch")
        


    with btnc2:
        if st.button(
            "Register Instead",
            type="primary",
            icon=':material/passkey:', 
            width = "stretch"):
             st.session_state.teacher_login_type="register"
           


    footer_home()






def teacher_screen_register():
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
        
    
    st.header('Register your teacher profile', text_alignment="center")
    st.space()

    teacher_username = st.text_input("Enter username", placeholder ='@HardinScott')
    teacher_name = st.text_input("Enter name", placeholder ='Hardin Scott')
    teacher_pass = st.text_input("Enter password", placeholder ='Enter password', type="password")  
    teacher_pass_confirm = st.text_input("Confirm your password", placeholder ='Confirm password', type="password")  

    st.divider()  

    btnc1, btnc2=st.columns(2)
    with btnc1:
        st.button(
            "Register now",
            icon=':material/passkey:', 
            shortcut='control+enter',
            width = "stretch")
        


    with btnc2:
        if st.button(
            "Login Instead",
            type="primary",
            icon=':material/passkey:', 
            width = "stretch"):
            st.session_state.teacher_login_type="login"
           


    footer_home()