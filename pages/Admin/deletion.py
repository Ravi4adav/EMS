import streamlit as st
import mysql.connector as mc
from exceptions import CustomExceptions
import sys

class Remove:
    def __init__(self):
        try:
            self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
        except Exception as e:
            raise CustomExceptions(e,sys)

    def run(self):
        self.user_id=st.text_input("Enter User-ID")
        self.dept_id=st.text_input("Enter Department-ID")
        
        self.btn=st.button("Remove Data")
        if self.btn:
            try:
                self.cur=self.mydb.cursor()

                self.cur.execute(f"delete from salary where Job_ID='{self.dept_id}'")
                self.mydb.commit()

                self.cur.execute(f"delete from projects where Employee_ID='{self.user_id}';")
                self.mydb.commit()

                self.cur.execute(f"delete from users where Employee_ID='{self.user_id}';")
                self.mydb.commit()

                self.cur.execute(f"delete from credentials where Employee_ID='{self.user_id}';")
                self.mydb.commit()

                self.cur.execute(f"delete from department where Employee_ID='{self.user_id}';")
                self.mydb.commit()

                self.cur.execute(f"delete from emp_leaves where Employee_ID='{self.user_id}';")
                self.mydb.commit()

                self.cur.execute(f"delete from employee where Employee_ID='{self.user_id}';")
                self.mydb.commit()

                st.header("Data Removed Successfully")

            except Exception as e:
                raise CustomExceptions(e,sys)
