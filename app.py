'''
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="")
c = mydb.cursor()
c.execute("CREATE DATABASE bbmsystem")

'''

import streamlit as st
import mysql.connector
# from create import *
# from database import *
from create import (create_bus, create_driver, create_customer, create_schedule, create_booking, create_payment, create_user)
from database import (create_bus_table, create_driver_table, create_customer_table, create_schedule_table, create_booking_table, create_payment_table, create_user_table, edit_bus)
from delete import (delete_bus, delete_driver, delete_customer, delete_schedule, delete_booking, delete_payment, delete_user)
from read import (read_all_bus, read_all_driver, read_all_customer, read_all_schedule, read_all_booking, read_all_payment, read_all_user)
from update import ( update_bus, update_driver, update_customer, update_booking, update_schedule, update_payment, update_user)
from query import query




def main():
    title_h = 'BUS BOOKING MANAGEMENT SYSTEM'
    st.markdown(f'<h1 style="color:#6C4AB6;font-size:44px;">{title_h}</h1>', unsafe_allow_html=True)
   

    menu = ["USER","BUS","DRIVER","CUSTOMER","SCHEDULE","BOOKING","PAYMENT","QUERY BOX"]
    choice = st.sidebar.selectbox("SERVICES",menu)

    menu_user = ["ADD_USER","DELETE_USER","UPDATE_USER","VIEW_USER"]
    menu_bus = ["ADD_BUS","DELETE_BUS","UPDATE_BUS", "VIEW_BUS"]
    menu_driver = ["ADD_DRIVER","DELETE_DRIVER","UPDATE_DRIVER","VIEW_DRIVER"]
    menu_customer = ["ADD_CUSTOMER","DELETE_CUSTOMER","UPDATE_CUSTOMER","VIEW_CUSTOMER"]
    menu_schedule = ["ADD_SCHEDULE","DELETE_SCHEDULE","UPDATE_SCHEDULE","VIEW_SCHEDULE"]
    menu_booking = ["ADD_BOOKING","DELETE_BOOKING","UPDATE_BOOKING","VIEW_BOOKING"]
    menu_payment = ["ADD_PAYMENT","DELETE_PAYMENT","UPDATE_PAYMENT","VIEW_PAYMENT"]
    


    if choice == "USER":
        choice_user = st.sidebar.selectbox("MENU",menu_user)
        create_user_table()
        if choice_user == "ADD_USER":
            st.subheader("ENTER A USER DETAILS")
            create_user()

        if choice_user == "VIEW_USER":
            st.subheader("DETAILES OF ALL USER")
            read_all_user()

        if choice_user == "DELETE_USER":
            st.subheader("SELECT USER TO DELETE")
            delete_user()
        
        if choice_user == "UPDATE_USER":
            st.subheader("SELECT USER TO UPDATE")
            update_user()


    elif choice == "BUS":
        choice_bus = st.sidebar.selectbox("MENU",menu_bus)
        create_bus_table()
        if choice_bus == "ADD_BUS":
            st.subheader("ENTER A BUS DETAILS")
            create_bus()

        if choice_bus == "VIEW_BUS":
            st.subheader("DETAILES OF ALL BUS")
            read_all_bus()

        if choice_bus == "DELETE_BUS":
            st.subheader("SELECT BUS TO DELETE")
            delete_bus()
        
        if choice_bus =="UPDATE_BUS":
            st.subheader("SELECT BUS TO UPDATE")
            update_bus()


    elif choice == "DRIVER":
        choice_driver=st.sidebar.selectbox("MENU",menu_driver)
        create_driver_table()
        if choice_driver == "ADD_DRIVER":
            st.subheader("ENTER A DRIVER DETAILS")
            create_driver()

        if choice_driver == "VIEW_DRIVER":
            st.subheader("DETAILES OF ALL DRIVER")
            read_all_driver()

        if choice_driver == "DELETE_DRIVER":
            st.subheader("SELECT DRIVER TO DELETE")
            delete_driver()
        
        if choice_driver =="UPDATE_DRIVER":
            st.subheader("SELECT DRIVER TO UPDATE")
            update_driver()

        
    elif choice == "CUSTOMER":
        choice_customer=st.sidebar.selectbox("MENU",menu_customer)
        create_customer_table()
        if choice_customer == "ADD_CUSTOMER":
            st.subheader("ENTER A CUSTOMER DETAILES")
            create_customer()

        if choice_customer == "VIEW_CUSTOMER":
            st.subheader("DETAILES OF ALL CUSTOMER")
            read_all_customer()

        if choice_customer == "DELETE_CUSTOMER":
            st.subheader("SELECT CUSTOMER TO DELETE")
            delete_customer()
        
        if choice_customer =="UPDATE_CUSTOMER":
            st.subheader("SELECT CUSTOMER TO UPDATE")
            update_customer()
         

    elif choice == "SCHEDULE":
        choice_schedule=st.sidebar.selectbox("MENU",menu_schedule)
        create_schedule_table()
        if choice_schedule == "ADD_SCHEDULE":
            st.subheader("ENTER A SCHEDULE DETAILES")
            create_schedule()

        if choice_schedule == "VIEW_SCHEDULE":
            st.subheader("DETAILES OF ALL SCHEDULE")
            read_all_schedule()

        if choice_schedule == "DELETE_SCHEDULE":
            st.subheader("SELECT SCHEDULE TO DELETE")
            delete_schedule()
        
        if choice_schedule =="UPDATE_SCHEDULE":
            st.subheader("SELECT SCHEDULE TO UPDATE")
            update_schedule()
        

    elif choice == "BOOKING":
        choice_booking = st.sidebar.selectbox("MENU",menu_booking)
        create_booking_table()
        if choice_booking == "ADD_BOOKING":
            st.subheader("ENTER A BOOKING DETAILES")
            create_booking()

        if choice_booking == "VIEW_BOOKING":
            st.subheader("DETAILES OF ALL BOOKING")
            read_all_booking()

        if choice_booking == "DELETE_BOOKING":
            st.subheader("SELECT BOOKING TO DELETE")
            delete_booking()
        
        if choice_booking == "UPDATE_BOOKING":
            st.subheader("SELECT BOOKING TO UPDATE")
            update_booking()
        

    elif choice == "PAYMENT":
        choice_payment = st.sidebar.selectbox("MENU",menu_payment)
        create_payment_table()
        if choice_payment == "ADD_PAYMENT":
            st.subheader("ENTER A PAYMENT DETAILES")
            create_payment()

        if choice_payment == "VIEW_PAYMENT":
            st.subheader("DETAILES OF ALL PAYMENT")
            read_all_payment()

        if choice_payment == "DELETE_PAYMENT":
            st.subheader("SELECT PAYMENT TO DELETE")
            delete_payment()
        
        if choice_payment == "UPDATE_PAYMENT":
            st.subheader("SELECT PAYMENT TO UPDATE")
            update_payment()
        

    elif choice=="QUERY BOX":
        #st.subheader=("QUERY BOX")
        query()


if __name__=='__main__':
    main()