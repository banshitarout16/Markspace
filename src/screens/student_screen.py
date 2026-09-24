import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_home
from src.UI.base_layout import style_background_dashboard, style_base_layout
from src.database.db import check_teacher_exists, create_teacher, teacher_login
from PIL import Image
import numpy as np 
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

def student_dashboard():
      student_data = st.session_state.student_data
      student_id = student_data['student_id']
      st.markdown(
        f"""
        <div style="text-align:center; margin-bottom:25px;">
            <h2 style="margin:0;">
                Welcome, {student_data["name"]} !
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )
      c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    
      with c1:
            header_dashboard()
      with c2:
            # st.subheader(f"""Welcome, {student_data["name"]}""")
            if st.button(
                        "Logout",
                        type="secondary",
                        key="loginbackbtn",
                        use_container_width=True,
                        shortcut="ctrl+b"
                        ):
                        st.session_state['is_logged_in'] = False
                        del st.session_state.student_data
                        st.rerun()
      st.space()

      c1, c2 =st.columns(2)
      with c1:
            st.header('Your Enrolled Subjects')
      with c2:
            if st.button('Enroll in Subject', type='primary', width='stretch'):
                  enroll_dialog()


      st.divider()


      with st.spinner('Loading your enrolled subjects..'):
            subjects = get_student_subjects(student_id)
            logs = get_student_attendance(student_id)

      stats_map = {}

      for log in logs:
            sid = log['subject_id']

            if sid not in stats_map:
                  stats_map[sid] = {"total":0, "attended": 0}

            stats_map[sid]['total'] +=1

            if log.get('is_present'):
                  stats_map[sid]['attended'] += 1


      cols = st.columns(2)
      for i, sub_node in enumerate(subjects):
            sub = sub_node['subjects']
            sid = sub['subject_id']


            stats = stats_map.get(sid,{"total":0, "attended": 0} )
            def unenroll_button(sub=sub):
                  if st.button("Unenroll from this course", type='tertiary', width='stretch', icon=':material/delete_forever:', key=f"unenroll_{sid}"):
                        unenroll_student_to_subject(student_id, sid)
                        st.toast(f'Unenrolled from {sub['name']} successfully!')
                        st.rerun()


            calendar_icon = '''<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                        <line x1="16" y1="2" x2="16" y2="6"/>
                        <line x1="8" y1="2" x2="8" y2="6"/>
                        <line x1="3" y1="10" x2="21" y2="10"/>
                        </svg>'''

            check_icon = '''<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"/>
                        <polyline points="9 12 11 14 15 10"/>
                        </svg>'''

                  
            with cols[i % 2]:

                  subject_card(
                  name = sub['name'],
                  code =sub['subject_code'],
                  section = sub['section'],



                  stats = [
                  (calendar_icon, 'Total', stats['total']),
                  (check_icon, 'Attended', stats['attended']),
                  ],
                  
                  footer_callback=unenroll_button
            )

      footer_home()


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