import streamlit as st
from database import add_bus,add_driver,add_customer,add_schedule,add_booking,add_payment,add_user
from database import view_only_bus, view_only_driver, view_only_customer, view_only_schedule, view_only_booking, view_only_payment, view_only_user


#---------------------------Bus--------------------------

def create_bus():
    u_id =[i[0] for i in  view_only_user()]

    col1, col2 = st.columns(2)
    with col1:
        bus_id = st.number_input("Bus ID:")
        bus_number = st.text_input("Bus Number:")
        bus_plate_number = st.text_input("Bus Plate Number:")
    with col2:
        bus_type = st.selectbox("Bus Type:",["AC","Non-AC","Non-AC Sleeper","AC Sleeper","General"])
        capacity = st.number_input("Capacity:")
        users_id = st.selectbox("User ID:",u_id)


    if st.button("Add this Bus"):
        add_bus(bus_id,bus_number,bus_plate_number,bus_type,capacity,users_id)
        st.success("Successfully added Bus {}".format(bus_number))



#--------------------------------driver data-----------------------------------

def create_driver():
    u_id =[i[0] for i in  view_only_user()]

    col1, col2 = st.columns(2)
    with col1:
        driver_id = st.number_input("Driver ID:")
        driver_name = st.text_input("Driver Name:")
    with col2:
        driver_contact = st.text_input("Driver Contact:")
        users_id = st.selectbox("User ID:",u_id)
        

    if st.button("Add Driver"):
        add_driver(driver_id,driver_name,driver_contact,users_id)
        st.success("Successfully added Driver {}".format(driver_name))


#----------------------------------Customer data---------------------------------

def create_customer():
    u_id =[i[0] for i in  view_only_user()]

    col1, col2 = st.columns(2)
    with col1:
        customer_id = st.number_input("Custoemr ID:")
        customer_name=st.text_input("Customer Name:")
        customer_contact = st.text_input("Customer Contact:")
        customer_email = st.text_input("Customer Email ID:")
    with col2:
        username = st.text_input("User Name:")
        cust_password = st.text_input("Password:")
        account_status = st.selectbox("Account Status:",["Done","Not Done"])
        users_id = st.selectbox("User ID:",u_id)

    if st.button("Add Customer"):
        add_customer(customer_id,customer_name,customer_contact,customer_email,username,cust_password,account_status,users_id)
        st.success("Successfully added Customer: {}".format(customer_id))


#--------------------------------Schedule--------------------------- 

def create_schedule():
    u_id =[i[0] for i in  view_only_user()]
    b_id =[i[0] for i in  view_only_bus()]
    d_id =[i[0] for i in  view_only_driver()]

    col1, col2 = st.columns(2)
    with col1:
        schedule_id = st.number_input("Schedule ID:")
        bus_id = st.selectbox("Bus ID:",b_id)
        driver_id = st.selectbox("Driver ID:",d_id)
        starting_point = st.text_input("Starting Point:")
        destination = st.text_input("Destination:")
        schedule_date = st.date_input("Schedule Date:")

    with col2:
        departure_time = st.time_input("Departure Time:")
        estimated_arrival_time = st.time_input("Estimated Arrival Time:")
        fare_amount = st.number_input("Fare Amount:")
        remarks = st.text_input("Remarks:")
        users_id = st.selectbox("User ID:",u_id)


    if st.button("Add This Travel Schedule"):
        add_schedule(schedule_id,bus_id,driver_id,starting_point,destination,schedule_date,departure_time,estimated_arrival_time,fare_amount,remarks,users_id)
        st.success("Successfully added.... Have a nice journey")


#----------------------booking---------------------------------------

def create_booking():
    u_id =[i[0] for i in  view_only_user()]
    s_id =[i[0] for i in  view_only_schedule()]
    c_id =[i[0] for i in  view_only_customer()]

    col1, col2 = st.columns(2)
    with col1:
        booking_id = st.number_input("Booking ID")
        schedule_id = st.selectbox("Schedule ID:",s_id)
        customer_id = st.selectbox("Customer ID:",c_id)
        number_of_seats = st.number_input("Number Of Seat:")
        fare_amount = st.number_input("Fare Amount:")
    with col2:
        total_amount = st.number_input("Total Amount:")
        date_of_booking = st.date_input("Date of Booking:")
        booking_status = st.selectbox("booking_status:",["Confirmed","Not Confirmed"])
        users_id = st.selectbox("User ID:",u_id)

    if st.button("Book Now"):
        add_booking(booking_id,schedule_id,customer_id,number_of_seats,fare_amount,total_amount,date_of_booking,booking_status,users_id)
        st.success("Successfully Booked {}".format(date_of_booking))


#-------------------------------payment----------------------
 
def create_payment():
    u_id =[i[0] for i in  view_only_user()]
    b_id =[i[0] for i in  view_only_booking()]

    col1, col2 = st.columns(2)
    with col1:
        payment_id = st.number_input("Payment ID:")
        booking_id = st.selectbox("Booking ID:",b_id)
        amount_paid = st.number_input("Amount Paid:")
    with col2:
        payment_date = st.date_input("Payment Date:")
        users_id = st.selectbox("User ID:",u_id)
    
    if st.button("Make this Payment {} ".format(amount_paid)):
        add_payment(payment_id,booking_id,amount_paid,payment_date,users_id)
        st.success("Successfully paid {}".format(amount_paid))


#----------------------user------------------------------

def create_user():
    col1, col2 = st.columns(2)
    with col1:
        users_id = st.number_input("User ID:")
        full_name = st.text_input("Full Name:")
        contact_no = st.text_input("Contact Number:")
        email_address = st.text_input("Email Address:")
    with col2:
        username = st.text_input("User Name:")
        userpassword = st.text_input("User Password:")
        account_category = st.text_input("Account Category:")
        account_status = st.selectbox("Account Status:",["Active","Deactive"])

    if st.button("Add User {} ".format(username)):
        add_user(users_id,full_name,contact_no,email_address,username,userpassword,account_category,account_status)
        st.success("Successfully added user {}".format(username))


