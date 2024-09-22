import streamlit as st
import mysql.connector as mc
from exceptions import CustomExceptions
import sys

class User_Login:
    if 'user' not in st.session_state:
        st.session_state['user']=""

    def __init__(self):
        pass

    def usr_state(self):
        self.user=st.session_state['user']
        return self.user

    def run(self):
        # Creating Input field
        self.usr_id=st.text_input("Enter user ID")
        self.usr_pwd=st.text_input("Enter user password", type='password')
        self.usr_exist=False

        # Login button
        self.btn=st.button("Login")
        
        if self.btn:
            try:
                self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
                self.cur=self.mydb.cursor()
                self.cur.execute('select * from credentials;')
                
                for r in self.cur:
                    if (r[0]==self.usr_id and r[1]==self.usr_pwd) and r[2].startswith('E-'):
                        st.session_state['login_employee_id']=r[2]
                        # stl.session_state['login']=True
                        self.usr_exist=True
                        st.write("Login Success!!")
                        st.session_state['user']=r[2]
                        break

                if not self.usr_exist:
                    st.write("Invalid User ID or Password")
                    
            except Exception as e:
                raise CustomExceptions(e,sys)    
        return self.usr_exist