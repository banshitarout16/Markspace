import streamlit as st

# overriding home background
def style_background_home():
    st.markdown("""

        <style>
        .stApp{ 
        background: #142B6F !important; 
        }
        </style>
        
        """ 
        ,unsafe_allow_html=True)


# overriding dashboard background
def style_background_dashboard():
    st.markdown("""

        <style>
        .stApp{ 
        background: #E0E3FF !important; 
        }
        </style>

        
        """ 
        ,unsafe_allow_html=True)

# overriding base layout background
def style_base_layout():
    st.markdown("""

        <style>
        @import url('https://fonts.googleapis.com/css2?family=Teko:wght@300..700&family=Titan+One&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Teko:wght@300..700&family=Titan+One&display=swap');


        #MainMenu, Footer, Header{
            visibility: hidden;
        }
        .block-container{
            padding-top: 1.5rem !important;
        }
        h1{
            font-family: 'Titan One', cursive !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

         h2{
                    font-family: 'Titan One', cursive !important;
                    font-size:2rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                }

        h3, h4, p {
            font-family: 'Outfit', sans-serif !important;   
                    }

        button{
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding:10px 20px !important;
            border: none !important;
            transition:transform 0.25s ease-in-out !important;
        }

        button[kind ="secondary"]{
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: white !important;
            padding:10px 20px !important;
            border: none !important;
            transition:transform 0.25s ease-in-out !important;
        }
        button[kind ="tertiary"]{
            border-radius: 1.5rem !important;
            background-color: black !important;
            color: white !important;
            padding:10px 20px !important;
            border: none !important;
            transition:transform 0.25s ease-in-out !important;
        }

        button:hover{
            transform: scale(1.05) !important;
            }

        </style>
        """ 
        ,unsafe_allow_html=True)
    