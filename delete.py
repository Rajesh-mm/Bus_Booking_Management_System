import streamlit as st
import pandas as pd
from database import view_all_bus, delete_buses, view_only_bus,view_all_driver, delete_drivers, view_only_driver, view_all_customer, delete_customers, view_only_customer, view_all_schedule, delete_schedules, view_only_schedule, view_all_booking, delete_bookings, view_only_booking, view_all_payment, delete_payments, view_only_payment, view_all_user, delete_users, view_only_user



#-------------------------BUS----------------------------------

def delete_bus():
    result = view_all_bus()
    df = pd.DataFrame(result,columns=['Bus ID', 'Bus Number', 'Plate Number', 'Type', 'Capacity','User ID'])
    with st.expander("Current_bus"):
        st.dataframe(df)

    list_of_bus = [i[0] for i in view_only_bus()]
    selected_bus = st.selectbox("Bus to edit", list_of_bus)
    st.warning("Do you want to delete '{}'?".format(selected_bus))

    if st.button("Delete bus"):
        delete_buses(selected_bus)
        st.success("Successfully deleted")

    
    result2 = view_all_bus()
    df2 = pd.DataFrame(result2, columns=['Bus ID', 'Bus Number', 'Plate Number', 'Type', 'Capacity','User ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


#----------------------------driver------------------------------

def delete_driver():
    result = view_all_driver()
    df = pd.DataFrame(result,columns=['Driver ID', 'Driver Name', 'Contact', 'User ID'])
    with st.expander("Current_driver"):
        st.dataframe(df)

    list_of_driver = [i[0] for i in view_only_driver()]
    selected_driver = st.selectbox("Driver to edit", list_of_driver)
    st.warning("Do you want to delete '{}'?".format(selected_driver))

    if st.button("Delete driver"):
        delete_drivers(selected_driver)
        st.success("Successfully deleted")

    
    result2 = view_all_driver()
    df2 = pd.DataFrame(result2, columns=['Driver ID', 'Driver Name', 'Contact', 'User ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


#-----------------------------customer-----------------------------

def delete_customer():
    result = view_all_customer()
    df = pd.DataFrame(result,columns=['Customer ID', 'Customer Name', 'Contact','Email ID', 'User Name', 'Customer Password', 'Status', 'User ID'])
    with st.expander("Current_customer"):
        st.dataframe(df)

    list_of_customer = [i[0] for i in view_only_customer()]
    selected_customer = st.selectbox("Customer to edit", list_of_customer)
    st.warning("Do you want to delete '{}'?".format(selected_customer))

    if st.button("Delete customer"):
        delete_customers(selected_customer)
        st.success("Successfully deleted")

    
    result2 = view_all_customer()
    df2 = pd.DataFrame(result2, columns=['Customer ID', 'Customer Name', 'Contact','Email ID', 'User Name', 'Customer Password', 'Status', 'User ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


#-----------------------schedule---------------------------------------

def delete_schedule():
    result = view_all_schedule()
    df = pd.DataFrame(result,columns=['Schedule ID', 'Bus ID', 'Driver ID', 'Starting Point', 'Destination', 'Schedule Date', 'Departure Time','Estimated Arrival Time', 'Arrival Time', 'Fare Amount', 'User ID'])
    with st.expander("Current_schedule"):
        st.dataframe(df)

    list_of_schedule = [i[0] for i in view_only_schedule()]
    selected_schedule = st.selectbox("Schedule to edit", list_of_schedule)
    st.warning("Do you want to delete '{}'?".format(selected_schedule))

    if st.button("Delete schedule"):
        delete_schedules(selected_schedule)
        st.success("Successfully Deleted")

    
    result2 = view_all_schedule()
    df2 = pd.DataFrame(result2, columns=['Schedule ID', 'Bus ID', 'Driver ID', 'Source', 'Destination', 'Schedule Date', 'Departure Time','Estimated Arrival Time', 'Arrival Time', 'Fare Amount', 'User ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


#-----------------------------booking-----------------------------

def delete_booking():
    result = view_all_booking()
    df = pd.DataFrame(result,columns=['Booking ID', 'Schedule ID', 'Customer ID', 'Number of Seat', 'Fare Amount','Total Amount', 'Date of Booking', 'Booking Status', 'User ID'])
    with st.expander("Current_booking"):
        st.dataframe(df)

    list_of_booking = [i[0] for i in view_only_booking()]
    selected_booking = st.selectbox("Booking to edit", list_of_booking)
    st.warning("Do you want to delete '{}'?".format(selected_booking))

    if st.button("Delete booking"):
        delete_bookings(selected_booking)
        st.success("Successfully deleted")


    
    result2 = view_all_booking()
    df2 = pd.DataFrame(result2, columns=['Booking ID', 'Schedule ID', 'Customer ID', 'Number of Seat', 'Fare Amount','Total Amount', 'Date of Booking', 'Booking Status', 'User ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


#-----------------------------payment-----------------------------
def delete_payment():
    result = view_all_payment()
    df = pd.DataFrame(result,columns=['Payment ID','Booking ID', 'Amount Paid', 'Payment Date', 'User ID'])
    with st.expander("Current_payment"):
        st.dataframe(df)

    list_of_payment = [i[0] for i in view_only_payment()]
    selected_payment = st.selectbox("Payment to edit", list_of_payment)
    st.warning("Do you want to delete '{}'?".format(selected_payment))

    if st.button("Delete payment"):
        delete_payments(selected_payment)
        st.success("Successfully deleted")


    result2 = view_all_payment()
    df2 = pd.DataFrame(result2, columns=['Payment ID','Booking ID', 'Amount Paid', 'Payment Date', 'User ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        

#-----------------------------user-----------------------------

def delete_user():
    result = view_all_user()
    df = pd.DataFrame(result,columns=['User ID', 'Full Name', 'Contact', 'Email ID', 'User Name', 'User Password', 'Category', 'Status'])
    with st.expander("Current_user"):
        st.dataframe(df)

    list_of_user = [i[0] for i in view_only_user()]
    selected_user = st.selectbox("User to edit", list_of_user)
    st.warning("Do you want to delete '{}'?".format(selected_user))

    if st.button("Delete user"):
        delete_users(selected_user)
        st.success("Successfully deleted")

    
    result2 = view_all_user()
    df2 = pd.DataFrame(result2, columns=['User ID', 'Full Name', 'Contact', 'Email ID', 'User Name', 'User Password', 'Category', 'Status'])
    with st.expander("Updated data"):
        st.dataframe(df2)