import streamlit as st
import mysql.connector as mc
import pandas as pd
from datetime import datetime
from exceptions import CustomExceptions
import sys


class Add_Details:
    def __init__(self):
        try:
            self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
            self.options=(None, "Add Employee Details", "Add Leaves Detail", "Add Salary Details")

            self.request=st.selectbox("Select type of Data to be insert",self.options)
        except Exception as e:
            raise CustomException(e,sys)

    # def field_check(self, col):
    #     self.col=col
    #     if self.col=="":
    #         st.info("Please fill the above field")
    #     return None


    def run(self):
        try:
            if self.request=="Add Employee Details":
                self.employee_db=pd.read_sql_query("select * from employee",self.mydb)
                self.emp_department=pd.read_sql_query("select * from department",self.mydb)
                self.emp_credentials=pd.read_sql_query("select * from credentials",self.mydb)
                self.emp_user=pd.read_sql_query("select * from users",self.mydb)
                self.emp_projects=pd.read_sql_query("select * from projects",self.mydb)


                self.immutable_col=['Employee_ID','Job_ID', 'Project_ID']

                # Generating primary key for Employee_ID feature
                if self.employee_db.shape[0]<10:
                    self.emp_db_key=f"E-00{self.employee_db.shape[0]+1}"
                elif self.employee_db.shape[0]>9 and self.employee_db.shape[0]<100:
                    self.emp_db_key=f"E-0{self.employee_db.shape[0]+1}"
                else:
                    self.emp_db_key=f"E-{self.employee_db.shape[0]+1}"

                # Getting user input for employee table
                self.employee_db_user_input={}
                for col in self.employee_db.columns:
                    if col not in self.immutable_col:
                        self.val=st.text_input(f"Enter {col}")
                        self.employee_db_user_input[col]=self.val
                        

                # Generating primary key for Job_ID feature
                if self.emp_department.shape[0]<10:
                    self.emp_dpt_key=f"JD-00{self.emp_department.shape[0]+1}"
                elif self.emp_department.shape[0]>9 and self.emp_department.shape[0]<100:
                    self.emp_dpt_key=f"JD-0{self.emp_department.shape[0]+1}"
                else:
                    self.emp_dpt_key=f"JD-{self.emp_department.shape[0]+1}"
                
                # Getting user input for departments table
                self.employee_dpt_user_input={}
                for col in self.emp_department.columns:
                    if col not in self.immutable_col:
                        self.val=st.text_input(f"Enter {col}")
                        self.employee_dpt_user_input[col]=self.val

                    
                # Generating primary key for Project_ID feature
                if self.emp_projects.shape[0]<10:
                    self.emp_prj_key=f"P-00{self.emp_projects.shape[0]+1}"
                elif self.emp_projects.shape[0]>9 and self.emp_projects.shape[0]<100:
                    self.emp_prj_key=f"P-0{self.emp_projects.shape[0]+1}"
                else:
                    self.emp_prj_key=f"P-{self.emp_projects.shape[0]+1}"

                # Getting user input for projects table
                self.employee_prj_user_input={}
                for col in self.emp_projects.columns:
                    if col not in self.immutable_col:
                        self.val=st.text_input(f"Enter {col}")
                        self.employee_prj_user_input[col]=self.val


                # Getting user input for user-type
                self.employee_user_input={}
                for col in self.emp_user.columns:
                    if col not in self.immutable_col:
                        self.val=st.text_input(f"Enter {col}")
                        self.employee_user_input[col]=self.val

                # Getting user input for credentials
                self.employee_cred_user_input={}
                for col in self.emp_credentials.columns:
                    if col not in self.immutable_col:
                        if col!='user_ID':
                            self.val=st.text_input(f"Enter {col}")
                            self.employee_cred_user_input[col]=self.val
                        else:
                            self.val=st.text_input(f"Enter {col}(e.g. email or phone no )")
                            self.employee_cred_user_input[col]=self.val


                self.add_btn=st.button("Add Data")

                if self.add_btn:
                    # Executing commands to insert data to various tables
                    try:
                        self.cur=self.mydb.cursor()
                        self.cur.execute(f"""insert into employee values ('{self.emp_db_key}','{self.employee_db_user_input['Fname']}',
                        '{self.employee_db_user_input['Lname']}', '{self.employee_db_user_input['Gender']}','{self.employee_db_user_input['Age']}',
                        '{self.employee_db_user_input['Contact_address']}','{self.employee_db_user_input['Mail']}','{self.employee_db_user_input['Phone']}');""")

                        self.mydb.commit()

                        self.cur.execute(f"""insert into department values ('{self.emp_dpt_key}', '{self.employee_dpt_user_input['Job_dept']}',
                        '{self.employee_dpt_user_input['Job_description']}','{self.employee_dpt_user_input['Job_name']}',
                        '{self.employee_dpt_user_input['Salary_range']}','{self.emp_db_key}');""")
                        
                        self.mydb.commit()

                        self.cur.execute(f"""insert into projects values ('{self.emp_prj_key}', '{self.emp_db_key}',
                        '{self.employee_prj_user_input['Project_code']}', '{self.employee_prj_user_input['Project_name']}',
                        '{self.employee_prj_user_input['Location']}');""")

                        self.mydb.commit()

                        self.cur.execute(f"""insert into users values ('{self.emp_db_key}', '{self.employee_user_input['User_type']}');""")

                        self.mydb.commit()

                        self.cur.execute(f"""insert into credentials values ('{self.employee_cred_user_input['user_ID']}', 
                        '{self.employee_cred_user_input['pswd']}', '{self.emp_db_key}');""")

                        self.mydb.commit()
                        # Closing DB connection
                        self.mydb.close()

                        # Showing header message of action completion.
                        st.header(f"Data Added Successfully")
                    except:
                        st.write("Please fill above fields with correct details.")

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Adding Leaves Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            elif self.request=="Add Leaves Detail":
                self.emp_leaves=pd.read_sql_query("select * from emp_leaves",self.mydb)

                # Generating unique Leave_ID
                if self.emp_leaves.shape[0]<10:
                    self.emp_leave_key=f"L-00{self.emp_leaves.shape[0]+1}"
                elif self.emp_leaves.shape[0]>9 and self.emp_leaves.shape[0]<100:
                    self.emp_leave_key=f"L-0{self.emp_leaves.shape[0]+1}"
                else:
                    self.emp_leave_key=f"L-{self.emp_leaves.shape[0]+1}"

                # Showing fields to user for entering data on emp_leaves table
                self.immutable_col=['Leave_ID']
                self.emp_leave_user_input={}
                for col in self.emp_leaves.columns:
                    if col not in self.immutable_col:
                        if col=='LeaveDate':
                            self.current_date=datetime.now()
                            self.emp_leave_user_input[col]=self.current_date.strftime("%Y-%m-%d")
                        else:
                            self.emp_leave_user_input[col]=st.text_input(f"Enter {col}")

                # Button for adding leaves data
                self.leave_button=st.button("Add Data")
                
                if self.leave_button:
                    self.cur=self.mydb.cursor()
                    self.cur.execute(f"""insert into emp_leaves values ('{self.emp_leave_key}', '{self.emp_leave_user_input['LeaveDate']}',
                    '{self.emp_leave_user_input['Reason']}', '{self.emp_leave_user_input['Employee_ID']}');""")
                    self.mydb.commit()
                    self.mydb.close()
                    st.header("Leave Details Added Successfully")

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Adding Salary Details ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            elif self.request=="Add Salary Details":
                self.emp_salary=pd.read_sql_query("select * from salary",self.mydb)

                # Generating unique Salary_ID
                if self.emp_salary.shape[0]<10:
                    self.emp_salary_key=f"S-00{self.emp_salary.shape[0]+1}"
                elif self.emp_salary.shape[0]>9 and self.emp_salary.shape[0]<100:
                    self.emp_salary_key=f"S-0{self.emp_leaves.shape[0]+1}"
                else:
                    self.emp_salary_key=f"S-{self.emp_salary.shape[0]+1}"


                # Showing fields to user for entering data on emp_leaves table
                self.immutable_col=['Salary_ID',"Annual"]
                self.emp_salary_user_input={}
                for col in self.emp_salary.columns:
                    if col not in self.immutable_col:
                        if self.emp_salary[col].dtypes!='object':
                            self.emp_salary_user_input[col]=pd.to_numeric(st.text_input(f"Enter {col}"))
                        else:
                            self.emp_salary_user_input[col]=st.text_input(f"Enter {col}")

                self.salary_button=st.button("Add Data")
                
                # Button for adding salary data
                if self.salary_button:
                    self.cur=self.mydb.cursor()
                    self.cur.execute(f"""insert into salary values ('{self.emp_salary_key}', '{self.emp_salary_user_input['Job_ID']}',
                    '{self.emp_salary_user_input['Amount']}', '{self.emp_salary_user_input['Amount']*12}');""")
                    self.mydb.commit()
                    self.mydb.close()
                    st.header("Salary Details Added Successfully")

            else:
                pass

        except Exception as e:
            raise CustomExceptions(e,sys)