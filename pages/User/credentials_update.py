import streamlit as st
import mysql.connector as mc
from pages.User.login import User_Login
import pandas as pd
from exceptions import CustomExceptions
import sys
import time

class CredUpdate:

    def __init__(self):
        try:
            self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
            self.user_type=User_Login().usr_state()


        except Exception as e:
            raise CustomExceptions(e,sys)


    def run(self):
        self.current_pswd=st.text_input("Enter existing password",type='password')
        self.new_pswd=st.text_input("Enter new password",type='password')
        self.btn=st.button("Update")


        if self.btn:
            try:
                self.cred_df=pd.read_sql_query(f"""select * from credentials where Employee_ID='{self.user_type}';""",self.mydb)
                
                if self.current_pswd==self.cred_df['pswd'].values[0]:
                    if len(self.new_pswd)>4:
                        self.cur=self.mydb.cursor()
                        self.cur.execute(f"""update credentials set pswd='{self.new_pswd}' where Employee_id='{self.user_type}';""")
                        self.mydb.commit()
                        self.mydb.close()
                        st.header("Password updated successfully")
                        time.sleep(2)
                        del st.session_state['logged_in']
                        st.rerun()
                    

                    else:
                        st.write('Password length must greater than 4')
                else:
                    st.write("Credentials not matching")
            except Exception as e:
                raise CustomExceptions(e,sys)

# if __name__=="__main__":
#     creds=CredUpdate()
#     creds.run()