import streamlit as st
import mysql.connector as mc
import pandas as pd
from exceptions import CustomExceptions
import sys

class LeavesData:
    def __init__(self):
        self.emp_id=st.text_input("Enter Employee ID")
        self.btn=st.button("View Data")

    def run(self):
        if self.btn:
            try:
                self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
                self.employ_data=pd.read_sql_query(f"""select *
                from emp_leaves
                where emp_leaves.Employee_ID='{self.emp_id}';""",self.mydb)

                st.dataframe(self.employ_data)
            except Exception as e:
                raise CustomExceptions(e,sys)