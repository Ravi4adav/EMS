import streamlit as st
import pandas as pd
import mysql.connector as mc
from exceptions import CustomExceptions
import sys


class Update_Data:
    def __init__(self):
        self.options=(None,"Employs Detail", "Employee Department", "Salary Details", "Employee Projects", "Employee Leaves")
        self.features={"Employs Detail":"employee", "Employee Department":"department", "Salary Details":"salary",
            "Employee Projects":"projects", "Employee Leaves":"emp_leaves"}

        self.table=st.selectbox("Select table for making updation",self.options)


    def run(self):
        try:
            if self.table!=None:
                self.mydb=mc.connect(host='localhost',username='root',password='12345678',database='employee')
                self.data=pd.read_sql_query(f"select * from {self.features[self.table]}",self.mydb)
                st.dataframe(self.data)

                # ~~~~~~~~~~~~~~ Code for Updation of data in departments table. ~~~~~~~~~~~~~~~~~~~~
            if self.table=="Employee Department":
                # Getting primary_key value to target attributes in database
                self.primary_key=st.text_input(f"Enter unique ID of attribute (e.g. E-00X or Ad-XXX, should not empty)")
                self.immutable_col=['Job_ID']
                # Generating Fields to get value for each feature in database.
                for col in self.data.columns:
                    if self.data[col].dtypes=='object' and (col not in self.immutable_col):
                        self.value=st.text_input(f"Enter {col} value")
                        if self.value!="":
                            self.data.loc[self.data['Job_ID']==self.primary_key,col]=self.value
                        else:
                            pass


                # Button for executing updation procedure of data in table.
                self.update_btn=st.button("Update")

                if self.update_btn:
                    if self.primary_key!="":
                        # Accessing the dataframe of target attribute from whole dataset.
                        self.update_val=self.data.loc[self.data['Job_ID']==self.primary_key]
                        # Getting the table name
                        self.table_name=self.features[self.table]
                        
                        # Creating cursor for executing commands
                        self.cur=self.mydb.cursor()

                        # SQL command for updation of values
                        self.command=f"""update {self.table_name} set Job_dept='{self.update_val['Job_dept'].values[0]}', 
                        Job_description='{self.update_val['Job_description'].values[0]}',
                        Job_name='{self.update_val['Job_name'].values[0]}', Salary_range='{self.update_val['Salary_range'].values[0]}', 
                        Employee_ID='{self.update_val['Employee_ID'].values[0]}'
                        where Job_ID='{self.primary_key}'"""

                        # Executing SQL command
                        self.cur.execute(self.command)

                        # Commiting data over database.
                        self.mydb.commit()
                        # closing connection from database
                        self.mydb.close()

                        st.header("Data updated Successfully")
                    
                    else:
                        st.write("Please check Unique ID field")



            # ~~~~~~~~~~~~~~~ Code for Updation of data in employee table. ~~~~~~~~~~~~~~~~~~
            elif self.table=="Employs Detail":
                # Getting primary_key value to target attributes in database
                self.primary_key=st.text_input(f"Enter unique ID of attribute (e.g. E-00X or Ad-XXX, should not empty)")
                self.immutable_col=['Employee_ID']
                # Generating Fields to get value for each feature in database.
                for col in self.data.columns:
                    if self.data[col].dtypes=='object' and (col not in self.immutable_col):
                        self.value=st.text_input(f"Enter {col} value")
                        if self.value!="":
                            self.data.loc[self.data['Employee_ID']==self.primary_key,col]=self.value
                        else:
                            pass


                # Button for executing updation procedure of data in table.
                self.update_btn=st.button("Update")
                
                if self.update_btn:
                    if self.primary_key!="":
                        # Accessing the dataframe of target attribute from whole dataset.
                        self.update_val=self.data.loc[self.data['Employee_ID']==self.primary_key]
                        # Getting the table name
                        self.table_name=self.features[self.table]
                        
                        # Creating cursor for executing commands
                        self.cur=self.mydb.cursor()

                        # SQL command for updation of values
                        self.command=f"""update {self.table_name} set Fname='{self.update_val['Fname'].values[0]}', Lname='{self.update_val['Lname'].values[0]}',
                        Gender='{self.update_val['Gender'].values[0]}', Age='{self.update_val['Age'].values[0]}', 
                        Contact_address='{self.update_val['Contact_address'].values[0]}', Mail='{self.update_val['Mail'].values[0]}',
                        Phone='{self.update_val['Phone'].values[0]}'
                        where Employee_ID='{self.primary_key}'"""

                        # Executing SQL command
                        self.cur.execute(self.command)

                        # Commiting data over database.
                        self.mydb.commit()
                        # closing connection from database
                        self.mydb.close()

                        st.header("Data updated Successfully")
                    
                    else:
                        st.write("Please check Unique ID field")


            # ~~~~~~~~~~~~~~~ Code for Updation of data in Salary table. ~~~~~~~~~~~~~~~~~~
            elif self.table=="Salary Details":
                # Getting primary_key value to target attributes in database
                self.primary_key=st.text_input(f"Enter unique ID of attribute (e.g. S-00X, should not empty)")
                self.immutable_col=['Salary_ID', 'Annual']
                # Generating Fields to get value for each feature in database.
                for col in self.data.columns:
                    if self.data[col].dtypes=='object' and (col not in self.immutable_col):
                        self.value=st.text_input(f"Enter {col} value")
                        if self.value!="":
                            self.data.loc[self.data['Salary_ID']==self.primary_key,col]=self.value
                        else:
                            pass
                    elif self.data[col].dtypes!='object' and (col not in self.immutable_col):
                        self.value=(st.text_input(f"Enter {col} value"))
                        if self.value!="":
                            self.data.loc[data['Salary_ID']==self.primary_key,col]=pd.to_numeric(self.value)
                        else:
                            pass


                # Button for executing updation procedure of data in table.
                self.update_btn=st.button("Update")
                
                if self.update_btn:
                    if self.primary_key!="":
                        # Accessing the dataframe of target attribute from whole dataset.
                        self.update_val=self.data.loc[self.data['Salary_ID']==self.primary_key]
                        # Getting the table name
                        self.table_name=self.features[self.table]
                        
                        # Creating cursor for executing commands
                        self.cur=self.mydb.cursor()

                        # Calculating Annual salary amount using monthly salary (Amount) attribute
                        self.annual_salary=self.data.loc[self.data['Salary_ID']==self.primary_key,'Amount'].values[0]*12
                        # SQL command for updation of values
                        self.command=f"""update {self.table_name} set Job_ID='{self.update_val['Job_ID'].values[0]}', 
                        Amount='{self.update_val['Amount'].values[0]}',
                        Annual='{self.annual_salary}'
                        where Salary_ID='{self.primary_key}'"""

                        # Executing SQL command
                        self.cur.execute(self.command)

                        # Commiting data over database.
                        self.mydb.commit()
                        # closing connection from database
                        self.mydb.close()

                        st.header("Data updated Successfully")
                    
                    else:
                        st.write("Please check Unique ID field")


            # ~~~~~~~~~~~~~~~ Code for Updation of data in projects table. ~~~~~~~~~~~~~~~~~~
            elif self.table=="Employee Projects":
                # Getting primary_key value to target attributes in database
                self.primary_key=st.text_input(f"Enter unique ID of attribute (e.g. S-00X, should not empty)")
                self.immutable_col=['Project_ID']
                # Generating Fields to get value for each feature in database.
                for col in self.data.columns:
                    if self.data[col].dtypes=='object' and (col not in self.immutable_col):
                        self.value=st.text_input(f"Enter {col} value")
                        if self.value!="":
                            self.data.loc[self.data['Project_ID']==self.primary_key,col]=self.value
                        else:
                            pass
                    elif self.data[col].dtypes!='object' and (col not in self.immutable_col):
                        self.value=int(st.text_input(f"Enter {col} value"))
                        if self.value!="":
                            self.data.loc[data['Project_ID']==self.primary_key,col]=self.value
                        else:
                            pass


                # Button for executing updation procedure of data in table.
                self.update_btn=st.button("Update")
                
                if self.update_btn:
                    if self.primary_key!="":
                        # Accessing the dataframe of target attribute from whole dataset.
                        self.update_val=self.data.loc[self.data['Project_ID']==self.primary_key]
                        # Getting the table name
                        self.table_name=self.features[self.table]
                        
                        # Creating cursor for executing commands
                        self.cur=self.mydb.cursor()

                        # SQL command for updation of values
                        self.command=f"""update {self.table_name} set Employee_ID='{self.update_val['Employee_ID'].values[0]}', 
                        Project_code='{self.update_val['Project_code'].values[0]}', Project_name='{self.update_val['Project_name'].values[0]}',
                        Location='{self.update_val['Location'].values[0]}'
                        where Project_ID='{self.primary_key}'"""

                        # Executing SQL command
                        self.cur.execute(self.command)

                        # Commiting data over database.
                        self.mydb.commit()
                        # closing connection from database
                        self.mydb.close()

                        st.header("Data updated Successfully")
                    
                    else:
                        st.write("Please check Unique ID field")
        
            # ~~~~~~~~~~~~~~~ Code for Updation of data in leaves table. ~~~~~~~~~~~~~~~~~~
            elif self.table=="Employee Leaves":
                # Getting primary_key value to target attributes in database
                self.primary_key=st.text_input(f"Enter unique ID of attribute (e.g. S-00X, should not empty)")
                self.immutable_col=['Leave_ID']
                # Generating Fields to get value for each feature in database.
                for col in self.data.columns:
                    if self.data[col].dtypes=='object' and (col not in self.immutable_col):
                        self.value=st.text_input(f"Enter {col} value")
                        if self.value!="":
                            self.data.loc[self.data['Leave_ID']==self.primary_key,col]=self.value
                        else:
                            pass
                    elif self.data[col].dtypes!='object' and (col not in self.immutable_col):
                        self.value=int(st.text_input(f"Enter {col} value"))
                        if self.value!="":
                            self.data.loc[data['Leave_ID']==self.primary_key,col]=self.value
                        else:
                            pass


                # Button for executing updation procedure of data in table.
                self.update_btn=st.button("Update")
                
                if self.update_btn:
                    if self.primary_key!="":
                        # Accessing the dataframe of target attribute from whole dataset.
                        self.update_val=self.data.loc[self.data['Leave_ID']==self.primary_key]
                        # Getting the table name
                        self.table_name=self.features[self.table]
                        
                        # Creating cursor for executing commands
                        self.cur=self.mydb.cursor()

                        # SQL command for updation of values
                        self.command=f"""update {self.table_name} set LeaveDate='{self.update_val['LeaveDate'].values[0]}', 
                        Reason='{self.update_val['Reason'].values[0]}', Employee_ID='{self.update_val['Employee_ID'].values[0]}'
                        where Leave_ID='{self.primary_key}'"""

                        # Executing SQL command
                        self.cur.execute(self.command)

                        # Commiting data over database.
                        self.mydb.commit()
                        # closing connection from database
                        self.mydb.close()

                        st.header("Data updated Successfully")
                    
                    else:
                        st.write("Please check Unique ID field")

            else:
                pass
        except Exception as e:
            raise CustomExceptions(e,sys)

# if __name__=="__main__":
#     Update_Data().run()