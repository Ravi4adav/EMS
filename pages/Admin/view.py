import streamlit as st
import mysql.connector as mc
import pandas as pd
from exceptions import CustomExceptions
import sys

class Details:
    def __init__(self):
        # Dictionary to map options of selectbox with table names in database
        self.features={"View Employs Data":"employee", "Employee Department":"department", "Salary Details":"salary",
             "Employee Projects":"projects", "Employee Leaves":"emp_leaves", "Employee Credentials":"credentials"}
        # providing options for selectbox
        self.options=(None,"View Employs Data", "Employee Department", "Salary Details", "Employee Projects", "Employee Leaves", "Employee Credentials")
        


    def run(self):
        self.data_genre=st.selectbox("Select query",self.options)
        try:
            if self.data_genre!=None:
                self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
                self.data=pd.read_sql_query(f"select * from {self.features[self.data_genre]}",self.mydb)
                st.dataframe(self.data)
                self.mydb.close()
        except Exception as e:
            raise CustomExceptions(e,sys)