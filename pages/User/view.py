import streamlit as st
import pandas as pd
import mysql.connector as mc
from exceptions import CustomExceptions
import sys


class UserDetails:
    def __init__(self):
        pass

    def run(self):
        self.emp_id=st.text_input("Enter Employee ID")
        self.btn=st.button("View Data")
        
        if self.btn:
            if self.emp_id!="":
                try:
                    self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
                    # fetching features of employee, projects, departments table in a merged table.
                    self.employ_data=pd.read_sql_query(f"""select 
                    employee.Employee_ID, employee.Fname, employee.Lname, employee.Age, employee.Gender, employee.Contact_address ,employee.Mail, employee.Phone,
                    department.Job_ID, department.Job_name, department.Job_dept, department.Job_description,
                    projects.Project_ID, projects.Project_code, projects.Project_name, projects.Location
                    from employee
                    inner join department
                    on employee.Employee_ID=department.Employee_ID
                    inner join projects
                    on employee.Employee_ID=projects.Employee_ID
                    where department.Employee_ID='{self.emp_id}' and
                    projects.Employee_ID='{self.emp_id}'; """,self.mydb)

                    if self.employ_data.shape[0]!=0:
                        # fetching salary table data on behalf of Job_ID assigned to Employ_ID in emloyee table
                        self.dept_id=self.employ_data.loc[0,'Job_ID']
                        self.salary_data=pd.read_sql_query(f"""select department.Job_ID, salary.Salary_ID, salary.Amount, salary.Annual from department
                        inner join salary on department.Job_ID=salary.Job_ID where salary.Job_ID='{self.dept_id}';""",self.mydb)


                        # Joining salary_data dataframe values to employ_data dataframe
                        for col in self.salary_data.columns:
                            self.employ_data[col]=self.salary_data[col]

                        # Displaying data of employee
                        st.dataframe(self.employ_data)
                    else:
                        st.write("Employee Data not Available")
                        
                except Exception as e:
                    raise CustomExceptions(e,sys)
            
            else:
                st.write("Please fill above field")

