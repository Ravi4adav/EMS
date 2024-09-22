from pages.pipeline.login import LoginRoutes
from pages.pipeline.admin_events import admin_routes
from pages.pipeline.user_events import user_routes
import streamlit as st
from exceptions import CustomExceptions
import sys


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'user' not in st.session_state:
    st.session_state['user_type']=""

def login_routes():

    loginroutes=LoginRoutes()
    if not st.session_state['logged_in']:
        login_status=loginroutes.routes()
        if login_status!=None:
            st.session_state['logged_in'], st.session_state['user_type']=login_status[0], login_status[1]

        if st.session_state['logged_in']:
            st.rerun()
    
    else:
        if st.session_state['user_type']=="Employee":
            user_routes()

        elif st.session_state['user_type']=="Admin":
            admin_routes()


login_routes()