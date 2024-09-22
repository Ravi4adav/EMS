import streamlit as st
from pages.Home.home import Home
from pages.User.login import User_Login
from pages.Admin.login import Admin_Login
from exceptions import CustomExceptions
from streamlit_option_menu import option_menu
import sys


class LoginRoutes:
    def __init__(self):
        pass

    def routes(self):
        try:
            with st.sidebar:
                self.user=option_menu("Login As",["Home","Employee","Admin"],menu_icon='bi bi-shield-lock',
                icons=['bi bi-house-door-fill','bi bi-person','bi bi-person-gear'])


            if self.user=="Home":
                self.home_page=Home()
                self.home_page.run()

            elif self.user=="Employee":
                # self.usr_login_page=User_Login()
                return [User_Login().run(), "Employee"]

            else:
                self.adm_login_page=Admin_Login()
                return [self.adm_login_page.run(), "Admin"]
                
        except Exception as e:
            raise CustomExceptions(e,sys)
