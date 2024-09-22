import streamlit as st
import pandas as pd
import mysql.connector as mc
import sys
from exceptions import CustomExceptions
from pages.Admin.login import Admin_Login
import time


class CredUpdate:

    def __init__(self):
        self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
        self.usr_id=Admin_Login().usr_state()


    def run(self):
        self.current_pswd=st.text_input("Enter existing password", type='password')
        self.new_pswd=st.text_input("Enter new password",type='password')

        self.btn=st.button("Update")

        if self.btn:
            try:
                self.cred_df=pd.read_sql_query(f"""select * from admin_creds where Admin_ID='{self.usr_id}';""",self.mydb)
                
                if self.current_pswd==self.cred_df['pswd'].values[0]:
                    if len(self.new_pswd)>4:
                        self.cur=self.mydb.cursor()
                        self.cur.execute(f"""update admin_creds set pswd='{self.new_pswd}' where Admin_ID='{self.usr_id}';""")
                        self.mydb.commit()
                        self.mydb.close()
                        st.header("Password updated successfully")
                        del st.session_state['logged_in']
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.write('Password length must greater than 4')
                else:
                    st.write("Credentials not matching")
            
            except Exception as e:
                raise CustomExceptions(e,sys)