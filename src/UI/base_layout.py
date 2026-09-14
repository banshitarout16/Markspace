import streamlit as st

# overriding home background
def style_background_home():
    st.markdown("""

        <style>
        .stApp{ 
        background: #4169E1 !important; 
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
        .stApp{ 
        background: #4169E1 !important; 
        }
        </style>

        
        """ 
        ,unsafe_allow_html=True)