import streamlit as st
import mysql.connector as mc
from exceptions import CustomExceptions
import sys

class Admin_Login:

    if 'user' not in st.session_state:
        st.session_state['user']=""

    def __init__(self):
        pass


    def usr_state(self):
        self.user=st.session_state["user"]
        return self.user

    def run(self):
        
        # Creating Input field
        usr_id=st.text_input("Enter admin ID")
        usr_pwd=st.text_input("Enter admin password",type='password')

        # Login button
        btn=st.button("Login")

        usr_exist=False

        if btn:
            try:
                mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
                cur=mydb.cursor()
                cur.execute('select * from admin_creds;')

                for r in cur:
                    if (r[0]==usr_id and r[1]==usr_pwd) and r[2].startswith('Ad-'):
                        # st.session_state['login']=True
                        # st.session_state['login_admin_id']=r[2]
                        st.write("Login Success!!")
                        st.session_state['user']=r[2]
                        usr_exist=True
                        break
                
                if not usr_exist:
                    st.write("Invalid User ID or Password")

            except Exception as e:
                raise CustomExceptions(e,sys)
                
        return usr_exist