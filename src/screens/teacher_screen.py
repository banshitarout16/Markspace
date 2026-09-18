import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_home
from src.UI.base_layout import style_background_dashboard, style_base_layout
from src.database.db import check_teacher_exists, create_teacher, teacher_login


def teacher_screen():

    style_background_dashboard()
    style_base_layout()


    if "teacher_data" in st.session_state:
         teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()

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

 

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    st.header(f"""Welcome, {teacher_data["name"]}""")

def login_teacher(username, password):
    if not username or not password:
          return False

    teacher = teacher_login(username, password)

    if teacher:
         st.session_state.user_role = "teacher"
         st.session_state.teacher_data = teacher
         st.session_state.is_logged_in = True
         return True
    
    return False

     

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
        if st.button(
            "Login",
            icon=':material/passkey:', 
            shortcut='control+enter',
            width = "stretch"):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("Access granted. Welcome to MarkSpace!")
                import time
                time.sleep(1)
                st.rerun()
            else:
                 st.error("Invalid username and password combo")

        


    with btnc2:
        if st.button(
            "Register Instead",
            type="primary",
            icon=':material/passkey:', 
            width = "stretch"):
             st.session_state.teacher_login_type="register"
           


    footer_home()




def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
         return False, "All fields are required!"
    if check_teacher_exists(teacher_username):
         return False, "Username already taken!"
    if teacher_pass != teacher_pass_confirm:
         return False, "Password doesn't match"

    try:
         create_teacher(teacher_username, teacher_pass, teacher_name)
         return True, "Sucessfully Created! Login Now"
    
    except Exception as e:
         return False, "Unexpected Error!"
     

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
        if st.button(
            "Register now",
            icon=':material/passkey:', 
            shortcut='control+enter',
            width = "stretch"):
            success,message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                 st.success(message)
                 import time
                 time.sleep(2)
                 st.session_state.teacher_login_type = "login"
                 st.rerun()
            else:
                 st.error(message)
        


    with btnc2:
        if st.button(
            "Login Instead",
            type="primary",
            icon=':material/passkey:', 
            width = "stretch"):
            st.session_state.teacher_login_type="login"
           


    footer_home()