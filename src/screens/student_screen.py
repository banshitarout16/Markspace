import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_home
from src.UI.base_layout import style_background_dashboard, style_base_layout
from src.database.db import check_teacher_exists, create_teacher, teacher_login
from PIL import Image
import numpy as np 
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student
import time

def student_dashboard():
    st.header("DASHBOARD HERE")


def student_screen():

    style_background_dashboard()
    style_base_layout()


    if "student_data" in st.session_state:
          student_dashboard()
          return

    
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
    
    show_registration = False
    photo_source = st.camera_input("Position your face in the center")
    if photo_source:
          img = np.array(Image.open(photo_source))
          with st.spinner("MarkSpace AI is Scanning.."):
                detected, all_ids, num_faces = predict_attendance(img)

                if num_faces == 0:
                      st.warning('face not found!')
                elif num_faces>1:
                      st.warning('Multiple faces found')
                else:
                      if detected:
                            student_id = list(detected.keys())[0]
                            all_students = get_all_students()

                            student = next((s for s in all_students if s['student_id']==student_id), None)

                            if student:
                                  st.session_state.is_logged_in = True
                                  st.session_state.user_role = 'student'
                                  st.session_state.student_data = student
                                  st.toast(f'Welcome Back {student['name']}!')
                                  time.sleep(1)
                                  st.rerun()


                      else:
                            st.info("Face not recognised! You might be a new Student!")
                            show_registration = True
    if show_registration:
        with st.container(border=True):
            st.header("register new Profile")
            new_name = st.text_input("Enter your name", placeholder = "Eg. Trevor jo")

            st.subheader("Optional : Voice Enrollment")
            st.info("Enroll yourself for voice only attendance")

            audio_data = None
            try:
                  audio_data = st.audio_input("Record a short phrase like I'm present, My name is Enzo.")
            except Exception:
                  st.error(" Audio Data Failed!")

            if st.button("Create Account", type="primary"):
                if new_name:
                        with st.spinner("Creating profile.."):
                              img = np.array(Image.open(photo_source))
                              encodings = get_face_embeddings(img)
                              if encodings:
                                    face_emb = encodings[0].tolist()

                                    voice_emb = None
                                    if audio_data:
                                        voice_emb = get_voice_embedding(audio_data.getvalue())

                                    response_data = create_student(new_name,face_embedding = face_emb, voice_embedding = voice_emb)

                                    if response_data:
                                        train_classifier()
                                        st.session_state.is_logged_in = True
                                        st.session_state.user_role = 'student'
                                        st.session_state.student_data = response_data[0]
                                        st.toast(f'Profile Created! Hi {new_name}!')
                                        time.sleep(1)
                                        st.rerun()  
                              else:
                                    st.error("Couldnt capture your facial features for registration")                                   

                              

                else:
                      st.warning("Please enter your name!")   


    footer_home()