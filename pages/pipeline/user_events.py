from pages.User.view import UserDetails
from pages.User.Leaves import LeavesData
from pages.User.credentials_update import CredUpdate
import streamlit as st
from exceptions import CustomExceptions
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
import sys



def user_routes():
    try:
        with st.sidebar:
            options=("View Employee Data", "Leaves History", "Update Password")
            query=option_menu("Employee Events", options=options,menu_icon='bi bi-person',
            icons=['bi bi-display','bi bi-file-medical-fill','bi bi-fingerprint'])
            logout=st.button("Logout")

        st.markdown("""
        <style>
            .st-emotion-cache-lpgk4i{
                background: #f34c0400;
            }

            .st-emotion-cache-lpgk4i:hover {
                background: #ff4b4b;
                color: white;
                font-weight: 900;
            }

            .st-emotion-cache-1khr67j {
                background: #0e0c0c;
                border-radius: 5px;
                text-align: center;
            }

            .st-emotion-cache-12118b6 p:hover{
                font-weight: 900;
            }
        </style>

        """,unsafe_allow_html=True)

        if logout:
            del st.session_state['logged_in']
            st.rerun()

        if query=="Leaves History":
            LeavesData().run()

        elif query=="Update Password":
            CredUpdate().run()
        
        else:
            UserDetails().run()
            
    except Exception as e:
        raise CustomExceptions(e,sys)
