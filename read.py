import pandas as pd
import streamlit as st
from database import view_all_bus,view_all_driver,view_all_customer,view_all_schedule,view_all_booking, view_all_payment, view_all_user
#,view_all_hdata

def read_all_bus():
    result = view_all_bus()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Bus ID', 'Bus Number', 'Plate Number', 'Type', 'Capacity','User ID'])
    with st.expander("View all Bus Details"):
        st.dataframe(df)


def read_all_driver():
    result = view_all_driver()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Driver ID', 'Driver Name', 'Contact', 'User ID'])
    with st.expander("View all Drivers"):
        st.dataframe(df)
        

def read_all_customer():
    result = view_all_customer()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Customer ID', 'Customer Name', 'Contact','Email ID', 'User Name', 'Customer Password', 'Status', 'User ID'])
    with st.expander("View all Customers"):
        st.dataframe(df)

def read_all_schedule():
    result = view_all_schedule()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Schedule ID', 'Bus ID', 'Driver ID', 'Starting Point', 'Destination', 'Schedule Date', 'Departure Time', 'estimated_arrival_time', 'Fare Amount', 'Remarks', 'User ID'])
    with st.expander("View all Schedules"):
        st.dataframe(df)    

def read_all_booking():
    result = view_all_booking()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Booking ID', 'Schedule ID', 'Customer ID', 'Number of Seat', 'Fare Amount', 'Total Amount', 'Date of Booking', 'Booking Status', 'User ID'])
    with st.expander("View all Bookings"):
        st.dataframe(df)  

def read_all_payment():
    result = view_all_payment()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Payment ID','Booking ID', 'Amount Paid', 'Payment Date', 'User ID'])
    with st.expander("View all payments"):
        st.dataframe(df)   

def read_all_user():
    result = view_all_user()
    # st.write(result)
    df = pd.DataFrame(result, columns=['User ID', 'Full Name', 'Contact', 'Email ID', 'User Name', 'User Password', 'Category', 'Status'])
    with st.expander("View all Users"):
        st.dataframe(df)   
