import pandas as pd
import streamlit as st
from database import view_all_bus,get_bus,edit_bus, view_only_bus, view_all_driver,get_driver,edit_driver,view_only_driver, view_all_customer, get_customer, edit_customer,view_only_customer, view_all_schedule, get_schedule, edit_schedule,view_only_schedule, view_all_booking, get_booking, edit_booking,view_only_booking, view_all_payment, get_payment, edit_payment,view_only_payment, view_all_user, get_user, edit_user, view_only_user




#---------------------------Bus---------------------------

def update_bus():
    result = view_all_bus()
    df=pd.DataFrame(result,columns=["bus_id","bus_number","bus_plate_number","bus_type","capacity","users_id"])

    with st.expander("Current Bus"):
        st.dataframe(df)
    
    list_of_bus=[i[0] for i in view_only_bus()]

    selected_bus = st.selectbox("Bus to edit",list_of_bus)
    selected_result = get_bus(selected_bus)
    u_id =[i[0] for i in  view_only_user()]
    print(selected_result)
    if selected_result:
        bus_id = selected_result[0][0]
        bus_number =selected_result[0][1]
        bus_plate_number = selected_result[0][2]
        bus_type = selected_result[0][3]
        capacity = selected_result[0][4]
        users_id = selected_result[0][5]

        col1,col2 = st.columns(2)
        with col1:
            new_bus_id = st.text_input("Bus ID",bus_id)
            new_bus_number = st.text_input("Bus Number",bus_number)
            new_bus_plate_number = st.text_input("Bus Plate Number",bus_plate_number)
         
        with col2:
            new_bus_type = st.selectbox("Bus Type:",["AC","Non-AC","Non-AC Sleeper","AC Sleeper","General"])
            new_capacity = st.text_input("Capacity",capacity)
            # new_users_id = st.text_input("User ID",users_id)\
            new_users_id = st.selectbox("User ID",u_id)

        if st.button("Update Bus"):
            edit_bus(new_bus_id, new_bus_number, new_bus_plate_number, new_bus_type , new_capacity, new_users_id, bus_id,bus_number,bus_plate_number,bus_type,capacity,users_id)
            st.success("Successfully Updated Bus :{}".format(bus_number))

        result2 = view_all_bus()
        df2 = pd.DataFrame(result2, columns=["bus_id","bus_number","bus_plate_number","bus_type","capacity","users_id"])
        with st.expander("Updated data"):
            st.dataframe(df2)



#---------------------------Driver---------------------------


def update_driver():
    result = view_all_driver()
    df=pd.DataFrame(result,columns=["driver_id","driver_name","driver_contact","users_id"])

    with st.expander("Current Driver"):
        st.dataframe(df)
    
    list_of_driver = [i[0] for i in view_only_driver()]

    selected_driver = st.selectbox("Driver to edit",list_of_driver)
    selected_result = get_driver(selected_driver)
    u_id =[i[0] for i in  view_only_user()]

    if selected_result:
        driver_id = selected_result[0][0]
        driver_name =selected_result[0][1]
        driver_contact = selected_result[0][2]
        users_id = selected_result[0][3]


        col1,col2 = st.columns(2)
        with col1:
            new_driver_id = st.text_input("Driver ID",driver_id)
            new_driver_name = st.text_input("Driver Name",driver_name)
         
        with col2:
            new_driver_contact = st.text_input("Driver Contact",driver_contact)
            new_users_id = st.selectbox("Users ID",u_id)


        if st.button("Update Driver"):
            edit_driver(new_driver_id, new_driver_name, new_driver_contact,new_users_id,driver_id,driver_name,driver_contact,users_id)
            st.success("Successfully Updated Driver :{}".format(driver_name))

        result2 = view_all_driver()
        df2 = pd.DataFrame(result2, columns=["driver_id","driver_name","driver_contact","users_id"])
        with st.expander("Updated data"):
            st.dataframe(df2)



#---------------------------Customer---------------------------


def update_customer():
    result = view_all_customer()
    df=pd.DataFrame(result,columns=["customer_id","customer_name","customer_contact","customer_email","username","password","account_status","users_id"])

    with st.expander("Current Customer"):
        st.dataframe(df)
    
    list_of_customer = [i[0] for i in view_only_customer()]

    selected_customer = st.selectbox("Customer to edit",list_of_customer)
    selected_result = get_customer(selected_customer)
    u_id = [i[0] for i in  view_only_user()]
    if selected_result:
        customer_id = selected_result[0][0]
        customer_name =selected_result[0][1]
        customer_contact = selected_result[0][2]
        customer_email = selected_result[0][3]
        username = selected_result[0][4]
        cust_password = selected_result[0][5]
        account_status = selected_result[0][6]
        users_id = selected_result[0][7]


        col1,col2 = st.columns(2)
        with col1:
            new_customer_id = st.text_input("Customer ID",customer_id)
            new_customer_name = st.text_input("Customer Name",customer_name)
            new_customer_contact = st.text_input("Customer Contact",customer_contact)
            new_customer_email = st.text_input("Customer Email",customer_email)
         
        with col2:
            new_username = st.text_input("User Name",username)
            new_cust_password = st.text_input("Customer Password",cust_password)
            new_account_status = st.selectbox("account status",["Done","Not Done"])
            new_users_id = st.selectbox("Users ID",u_id)


        if st.button("Update Customer"):
            edit_customer(new_customer_id, new_customer_name, new_customer_contact, new_customer_email, new_username, new_cust_password, new_account_status, new_users_id, customer_id,customer_name,customer_contact,customer_email,username,cust_password,account_status,users_id)
            st.success("Successfully Updated Customer :{}".format(customer_name))

        result2 = view_all_customer()
        df2 = pd.DataFrame(result2, columns=["customer_id","customer_name","customer_contact","customer_email","username","cust_password","account_status","users_id"])
        with st.expander("Updated data"):
            st.dataframe(df2)


#---------------------------Schedule---------------------------


def update_schedule():
    result = view_all_schedule()
    df=pd.DataFrame(result,columns=["schedule_id","bus_id","driver_id","starting_point","destination","schedule_date","departure_time","estimated_arrival_time","fare_amount","remarks","users_id"])

    with st.expander("Current Schedule"):
        st.dataframe(df)
    
    list_of_schedule = [i[0] for i in view_only_schedule()]

    selected_schedule = st.selectbox("schedule to edit",list_of_schedule)
    selected_result = get_schedule(selected_schedule)
    u_id =[i[0] for i in  view_only_user()]
    b_id =[i[0] for i in  view_only_bus()]
    d_id =[i[0] for i in  view_only_driver()]

    if selected_result:
        schedule_id = selected_result[0][0]
        bus_id = selected_result[0][1]
        driver_id = selected_result[0][2]
        starting_point = selected_result[0][3]
        destination = selected_result[0][4]
        schedule_date = selected_result[0][5]
        departure_time = selected_result[0][6]
        estimated_arrival_time = selected_result[0][7]
        fare_amount = selected_result[0][8]
        remarks = selected_result[0][9]
        users_id = selected_result[0][10]


        col1,col2 = st.columns(2)
        with col1:
            new_schedule_id = st.text_input("Schedule ID",schedule_id)
            new_bus_id = st.selectbox("Bus ID",b_id)
            new_driver_id = st.selectbox("Driver ID",d_id)
            new_starting_point = st.text_input("Starting Point",starting_point)
            new_destination = st.text_input("Destination",destination)
            new_schedule_date = st.date_input("schedule Date",schedule_date)
         
        with col2:
            new_departure_time = st.text_input("Departure Time",departure_time)
            new_estimated_arrival_time = st.text_input("Estimated Arrival time",estimated_arrival_time)
            new_fare_amount = st.text_input("Fare Amount",fare_amount)
            new_remarks = st.text_input("Remarks",remarks)
            new_users_id = st.selectbox("User ID",u_id)


        if st.button("Update Schedule"):
            edit_schedule(new_schedule_id, new_bus_id, new_driver_id, new_starting_point, new_destination, new_schedule_date, new_departure_time, new_estimated_arrival_time, new_fare_amount, new_remarks, new_users_id, schedule_id,bus_id,driver_id,starting_point,destination,schedule_date,departure_time,estimated_arrival_time,fare_amount,remarks,users_id)
            st.success("Successfully Updated schedule :{}".format(schedule_date))

        result2 = view_all_schedule()
        df2 = pd.DataFrame(result2, columns=["schedule_id","bus_id","driver_id","starting_point","destination","schedule_date","departure_time","estimated_arrival_time","fare_amount","remarks","users_id"])
        with st.expander("Updated data"):
            st.dataframe(df2)


#---------------------------Booking---------------------------


def update_booking():
    result = view_all_booking()
    df=pd.DataFrame(result,columns=["booking_id","schedule_id","customer_id","number_of_seats","fare_amount","total_amount","date_of_booking","booking_status","users_id"])

    with st.expander("Current Booking"):
        st.dataframe(df)
    
    list_of_booking = [i[0] for i in view_only_booking()]

    selected_booking = st.selectbox("Booking to edit",list_of_booking)
    selected_result = get_booking(selected_booking)
    u_id =[i[0] for i in  view_only_user()]
    s_id =[i[0] for i in  view_only_schedule()]
    c_id =[i[0] for i in  view_only_customer()]

    if selected_result:
        booking_id = selected_result[0][0]
        schedule_id =selected_result[0][1]
        customer_id = selected_result[0][2]
        number_of_seats = selected_result[0][3]
        fare_amount = selected_result[0][4]
        total_amount = selected_result[0][5]
        date_of_booking = selected_result[0][6]
        booking_status = selected_result[0][7]
        users_id = selected_result[0][8]


        col1,col2 = st.columns(2)
        with col1:
            new_booking_id = st.text_input("Booking ID",booking_id)
            new_schedule_id = st.selectbox("Schedule ID",s_id)
            new_customer_id = st.selectbox("Customer ID",c_id)
            new_number_of_seats = st.number_input("Number of Seat",number_of_seats)
            new_fare_amount = st.number_input("Fare Amount",fare_amount)

         
        with col2:
            new_total_amount = st.number_input("Total Amount",total_amount)
            new_date_of_booking = st.date_input("Date_of_booking",date_of_booking)
            new_booking_status = st.selectbox("booking_status",["Booked","Not Booked"])
            new_users_id = st.selectbox("Users ID",u_id)


        if st.button("Update Booking"):
            edit_booking(new_booking_id, new_schedule_id, new_customer_id, new_number_of_seats, new_fare_amount,new_total_amount, new_date_of_booking, new_booking_status, new_users_id, booking_id,schedule_id,customer_id,number_of_seats,fare_amount,total_amount,date_of_booking,booking_status,users_id)
            st.success("Successfully Updated booking :{}".format(date_of_booking))

        result2 = view_all_booking()
        df2 = pd.DataFrame(result2, columns=["booking_id","schedule_id","customer_id","number_of_seats","fare_amount","total_amount","date_of_booking","booking_status","users_id"])
        with st.expander("Updated data"):
            st.dataframe(df2)
            

#---------------------------Payment---------------------------


def update_payment():
    result = view_all_payment()
    df=pd.DataFrame(result,columns=["payment_id","booking_id","amount_paid","payment_date","users_id"])

    with st.expander("Current Payment"):
        st.dataframe(df)
    
    list_of_payment = [i[0] for i in view_only_payment()]

    selected_payment = st.selectbox("Payment to edit",list_of_payment)
    selected_result = get_payment(selected_payment)
    u_id =[i[0] for i in  view_only_user()]
    b_id =[i[0] for i in  view_only_booking()]

    if selected_result:
        payment_id = selected_result[0][0]
        booking_id =selected_result[0][1]
        amount_paid = selected_result[0][2]
        payment_date = selected_result[0][3]
        users_id = selected_result[0][4]

        col1,col2 = st.columns(2)
        with col1:
            new_payment_id = st.text_input("Payment ID",payment_id)
            new_booking_id = st.selectbox("Booking ID",b_id)
            new_amount_paid = st.number_input("Amount Paid",amount_paid)

        with col2:
            new_payment_date = st.date_input("Payment Date",payment_date)
            new_users_id = st.selectbox("User ID",u_id)


        if st.button("Update Payment"):
            edit_payment(new_payment_id, new_booking_id, new_amount_paid, new_payment_date, new_users_id, payment_id,booking_id,amount_paid,payment_date,users_id)
            st.success("Successfully Updated Payment :{}".format(amount_paid))

        result2 = view_all_payment()
        df2 = pd.DataFrame(result2, columns=["payment_id","booking_id","amount_paid","payment_date","users_id"])
        with st.expander("Updated data"):
            st.dataframe(df2)



#---------------------------User---------------------------


def update_user():
    result = view_all_user()
    df=pd.DataFrame(result,columns=["users_id","full_name","contact_no","email_address","username","userpassword","account_category","account_status"])

    with st.expander("Current User"):
        st.dataframe(df)
    
    list_of_user = [i[0] for i in view_only_user()]

    selected_user = st.selectbox("User to edit",list_of_user)
    selected_result = get_user(selected_user)
    print(selected_result)
    if selected_result:
        users_id = selected_result[0][0]
        full_name =selected_result[0][1]
        contact_no = selected_result[0][2]
        email_address = selected_result[0][3]
        username = selected_result[0][4]
        userpassword = selected_result[0][5]
        account_category = selected_result[0][6]
        account_status = selected_result[0][7]


        col1,col2 = st.columns(2)
        with col1:
            new_users_id = st.text_input("User ID",users_id)
            new_fullname = st.text_input("Full Name",full_name)
            new_contact_no = st.text_input("Contact Number",contact_no)
            new_email_address = st.text_input("Email Address",email_address)

         
        with col2:
            new_username = st.text_input("User Name",username)
            new_userpassword = st.text_input("User Password",userpassword)
            new_account_category = st.text_input("Account Category",account_category)
            new_account_status = st.selectbox("Account Status:",["Active","Deactive"])


        if st.button("Update User"):
            edit_user(new_users_id, new_fullname, new_contact_no, new_email_address, new_username, new_userpassword, new_account_category, new_account_status, users_id,full_name,contact_no,email_address,username,userpassword,account_category,account_status)
            st.success("Successfully Updated User :{}".format(username))

        result2 = view_all_user()
        df2 = pd.DataFrame(result2, columns=["users_id","full_name","contact_no","email_address","username","userpassword","account_category","account_status"])
        with st.expander("Updated data"):
            st.dataframe(df2)

