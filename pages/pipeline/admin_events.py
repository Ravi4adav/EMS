from pages.Admin.view import Details
from pages.Admin.insertion import Add_Details
from pages.Admin.deletion import Remove
from pages.Admin.updation import Update_Data
from pages.Admin.credentials_update import CredUpdate
import streamlit as st
from streamlit_option_menu import option_menu
from exceptions import CustomExceptions
import sys

def admin_routes():
    try:
        with st.sidebar:
            options=("View Employs Data", "Add Data", "Remove Data", "Update Data", "Update Password")
            query=option_menu("Admin Events",options=options, menu_icon='bi bi-person-gear',
            icons=['bi bi-display','bi bi-file-earmark-plus-fill','bi bi-trash','bi bi-activity','bi bi-fingerprint'])
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

        if query=="View Employs Data":
            Details().run()

        elif query=="Add Data":
            add_data=Add_Details()
            add_data.run()
        
        elif query=="Remove Data":
            Remove().run()

        elif query=="Update Data":
            Update_Data().run()

        elif query=="Update Password":
            CredUpdate().run()

    except Exception as e:
        raise CustomExceptions(e,sys)
