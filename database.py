import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="BBMSystem")
c = mydb.cursor()



#----------------------------------------DATABSE for bus--------------------------------------------------------------------------------
def create_bus_table():
     c.execute('CREATE TABLE IF NOT EXISTS `bus` (`bus_id` int(11) NOT NULL ,`bus_number` varchar(15) NOT NULL,`bus_plate_number` varchar(15) NOT NULL,`bus_type` int(1) NOT NULL,`capacity` int(3) NOT NULL,`users_id` int(11) NOT NULL)')


def add_bus(bus_id,bus_number,bus_plate_number,bus_type,capacity,users_id):
    c.execute('INSERT INTO bus(bus_id,bus_number,bus_plate_number,bus_type,capacity,users_id) VALUES (%s,%s,%s,%s,%s,%s)',
              (bus_id,bus_number,bus_plate_number,bus_type,capacity,users_id))
    mydb.commit()


def view_all_bus():
    c.execute('SELECT * FROM bus')
    data = c.fetchall()
    return data

def view_only_bus():
    c.execute('SELECT bus_id from bus')
    data = c.fetchall()
    return data


def get_bus(bus_id):
    c.execute('SELECT * FROM bus WHERE bus_id="{}"'.format(bus_id))
    data = c.fetchall()
    return data


def edit_bus(new_bus_id, new_bus_number, new_bus_plate_number, new_bus_type , new_capacity, new_users_id, bus_id,bus_number,bus_plate_number,bus_type,capacity,users_id):
    c.execute("UPDATE bus SET bus_id=%s,bus_number=%s,bus_plate_number=%s,bus_type=%s,capacity=%s,users_id=%s where bus_id=%s and bus_number=%s and bus_plate_number=%s and bus_type=%s and capacity=%s and users_id=%s",
               (new_bus_id, new_bus_number, new_bus_plate_number, new_bus_type , new_capacity, new_users_id, bus_id,bus_number,bus_plate_number,bus_type,capacity,users_id))
    mydb.commit()
    #data = c.fetchall()
    #return data


def delete_buses(bus_id):
    c.execute('DELETE FROM bus WHERE bus_id="{}"'.format(bus_id))




#------------------------------------ database for driver--------------------------------------------------

def create_driver_table():
     c.execute('CREATE TABLE IF NOT EXISTS `driver` (`driver_id` int(11) NOT NULL AUTO_INCREMENT,`driver_name` varchar(50) NOT NULL,`driver_contact` varchar(15) NOT NULL,`users_id` int(11) NOT NULL,PRIMARY KEY (`driver_id`),KEY `users_id` (`users_id`))')


def add_driver(driver_id,driver_name,driver_contact,users_id):
    c.execute('INSERT INTO driver(driver_id,driver_name,driver_contact,users_id) '
              'VALUES (%s,%s,%s,%s)',
              (driver_id,driver_name,driver_contact,users_id))
    mydb.commit()


def view_all_driver():
    c.execute('SELECT * FROM driver')
    data = c.fetchall()
    return data


def view_only_driver():
    c.execute('SELECT driver_id from driver')
    data = c.fetchall()
    return data


def get_driver(driver_id):
    c.execute('SELECT * FROM driver WHERE driver_id="{}"'.format(driver_id))
    data = c.fetchall()
    return data

def edit_driver(new_driver_id, new_driver_name, new_driver_contact, new_users_id, driver_id,driver_name,driver_contact,users_id):
    c.execute("UPDATE driver SET driver_id=%s,driver_name=%s,driver_contact=%s,users_id=%s where driver_id=%s and driver_name=%s and driver_contact=%s and users_id=%s",
               (new_driver_id, new_driver_name, new_driver_contact, new_users_id, driver_id,driver_name,driver_contact,users_id))
    mydb.commit()
    #data = c.fetchall()
    #return data


def delete_drivers(driver_id):
    c.execute('DELETE FROM driver WHERE driver_id="{}"'.format(driver_id))



#-------------------------------------------------------------database for Customer------------------------------------------------------------------------

def create_customer_table():
     c.execute('CREATE TABLE IF NOT EXISTS `customer` (`customer_id` int(11) NOT NULL AUTO_INCREMENT,`customer_name` varchar(50) NOT NULL,`customer_contact` varchar(15) NOT NULL,`customer_email` varchar(30) NOT NULL,`username` varchar(30) NOT NULL,`cust_password` varchar(30) NOT NULL,`account_status` int(1) NOT NULL,`user_id` int(11) NOT NULL,PRIMARY KEY (`customer_id`),KEY `user_id` (`user_id`))')


def add_customer(customer_id,customer_name,customer_contact,customer_email,username,cust_password,account_status,users_id):
    c.execute('INSERT INTO customer(customer_id,customer_name,customer_contact,customer_email,username,cust_password,account_status,users_id) '
              'VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (customer_id,customer_name,customer_contact,customer_email,username,cust_password,account_status,users_id))
    mydb.commit()


def view_all_customer():
    c.execute('SELECT * FROM customer')
    data = c.fetchall()
    return data


def view_only_customer():
    c.execute('SELECT customer_id FROM customer')
    data = c.fetchall()
    return data


def get_customer(customer_id):
    c.execute('SELECT * FROM customer WHERE customer_id="{}"'.format(customer_id))
    data = c.fetchall()
    return data


def edit_customer(new_customer_id, new_customer_name, new_customer_contact, new_customer_email, new_username, new_cust_password, new_account_status, new_users_id, customer_id,customer_name,customer_contact,customer_email,username,cust_password,account_status,users_id):
    c.execute("UPDATE customer SET customer_id=%s,customer_name=%s,customer_contact=%s,customer_email=%s,username=%s,cust_password=%s,account_status=%s,users_id=%s where customer_id=%s and customer_name=%s and customer_contact=%s and customer_email=%s and username=%s and cust_password=%s and account_status=%s and users_id=%s",
               (new_customer_id, new_customer_name, new_customer_contact, new_customer_email, new_username, new_cust_password, new_account_status, new_users_id, customer_id,customer_name,customer_contact,customer_email,username,cust_password,account_status,users_id))
    mydb.commit()
    #data = c.fetchall()
    #return data


def delete_customers(customer_id):
    c.execute('DELETE FROM customer WHERE customer_id="{}"'.format(customer_id))




#------------------------------------------------------------------------- database for schedule----------------------------------------------------------------------

def create_schedule_table():
     c.execute(' CREATE TABLE IF NOT EXISTS `schedule` (`schedule_id` int(11) NOT NULL ,`bus_id` int(11) NOT NULL,`driver_id` int(11) NOT NULL,`starting_point` varchar(30) NOT NULL,`destination` varchar(30) NOT NULL,`schedule_date` date NOT NULL,`departure_time` time NOT NULL,`estimated_arrival_time` time NOT NULL,`fare_amount` float NOT NULL,`remarks` varchar(100) NOT NULL,`users_id` int(11) NOT NULL,PRIMARY KEY (`schedule_id`),KEY `bus_id` (`bus_id`,`driver_id`,`users_id`),KEY `users_id` (`users_id`),KEY `driver_id` (`driver_id`))')


def add_schedule(schedule_id,bus_id,driver_id,starting_point,destination,schedule_date,departure_time,estimated_arrival_time,fare_amount,remarks,users_id):
    c.execute('INSERT INTO schedule(schedule_id,bus_id,driver_id,starting_point,destination,schedule_date,departure_time,estimated_arrival_time,fare_amount,remarks,users_id)'
              'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (schedule_id,bus_id,driver_id,starting_point,destination,schedule_date,departure_time,estimated_arrival_time,fare_amount,remarks,users_id))
    mydb.commit()


def view_all_schedule():
    c.execute('SELECT * FROM schedule')
    data = c.fetchall()
    return data


def view_only_schedule():
    c.execute('SELECT schedule_id from schedule')
    data = c.fetchall()
    return data


def get_schedule(schedule_id):
    c.execute('SELECT * FROM schedule WHERE schedule_id="{}"'.format(schedule_id))
    data = c.fetchall()
    return data


def edit_schedule(new_schedule_id, new_bus_id, new_driver_id, new_starting_point, new_destination, new_schedule_date, new_departure_time, new_estimated_arrival_time, new_fare_amount, new_remarks, new_users_id, schedule_id,bus_id,driver_id,starting_point,destination,schedule_date,departure_time,estimated_arrival_time,fare_amount,remarks,users_id):
    c.execute("UPDATE schedule SET schedule_id=%s, bus_id=%s, driver_id=%s,starting_point=%s,destination=%s,schedule_date=%s,departure_time=%s,estimated_arrival_time=%s,fare_amount=%s,remarks=%s,users_id=%s where schedule_id=%s and bus_id=%s and driver_id=%s and starting_point=%s and destination=%s and schedule_date=%s and departure_time=%s and estimated_arrival_time=%s and fare_amount=%s and remarks=%s and users_id=%s",
            (new_schedule_id, new_bus_id, new_driver_id, new_starting_point, new_destination, new_schedule_date, new_departure_time, new_estimated_arrival_time, new_fare_amount, new_remarks, new_users_id, schedule_id,bus_id,driver_id,starting_point,destination,schedule_date,departure_time,estimated_arrival_time,fare_amount,remarks,users_id))
    mydb.commit()
    #data = c.fetchall()
    #return data


def delete_schedules(schedule_id):
    c.execute('DELETE FROM schedule WHERE schedule_id="{}"'.format(schedule_id))




#---------------------------------------------------------------- database for booking-----------------------------------------------------------------------------------------

def create_booking_table():
     c.execute('CREATE TABLE IF NOT EXISTS `booking` (`booking_id` int(11) NOT NULL AUTO_INCREMENT,`schedule_id` int(11) NOT NULL,`customer_id` int(11) NOT NULL,`number_of_seats` int(2) NOT NULL,`fare_amount` float NOT NULL,`total_amount` float NOT NULL,`date_of_booking` datetime NOT NULL,`booking_status` int(1) NOT NULL,`users_id` int(11) NOT NULL,PRIMARY KEY (`booking_id`),KEY `schedule_id` (`schedule_id`,`customer_id`,`users_id`),KEY `users_id` (`users_id`),KEY `customer_id` (`customer_id`))')


def add_booking(booking_id,schedule_id,customer_id,number_of_seats,fare_amount,total_amount,date_of_booking,booking_status,users_id):
    c.execute('INSERT INTO booking(booking_id,schedule_id,customer_id,number_of_seats,fare_amount,total_amount,date_of_booking,booking_status,users_id) '
              'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (booking_id,schedule_id,customer_id,number_of_seats,fare_amount,total_amount,date_of_booking,booking_status,users_id))
    mydb.commit()


def view_all_booking():
    c.execute('SELECT * FROM booking')
    data = c.fetchall()
    return data


def view_only_booking():
    c.execute('SELECT booking_id from booking')
    data = c.fetchall()
    return data


def get_booking(booking_id):
    c.execute('SELECT * FROM booking WHERE booking_id="{}"'.format(booking_id))
    data = c.fetchall()
    return data


def edit_booking(new_booking_id, new_schedule_id, new_customer_id, new_number_of_seats, new_fare_amount,new_total_amount, new_date_of_booking, new_booking_status, new_users_id, booking_id,schedule_id,customer_id,number_of_seats,fare_amount,total_amount,date_of_booking,booking_status,users_id):
    c.execute("UPDATE booking SET booking_id=%s,schedule_id=%s,customer_id=%s, number_of_seats=%s, fare_amount=%s, total_amount=%s,date_of_booking=%s,booking_status=%s,users_id=%s where booking_id=%s and schedule_id=%s and customer_id=%s and number_of_seats=%s and fare_amount=%s and total_amount=%s and date_of_booking=%s and booking_status=%s and users_id=%s",
            (new_booking_id, new_schedule_id, new_customer_id, new_number_of_seats, new_fare_amount,new_total_amount, new_date_of_booking, new_booking_status, new_users_id, booking_id,schedule_id,customer_id,number_of_seats,fare_amount,total_amount,date_of_booking,booking_status,users_id))
    mydb.commit()
    #data = c.fetchall()
    #return data


def delete_bookings(booking_id):
    c.execute('DELETE FROM booking WHERE booking_id="{}"'.format(booking_id))




#-------------------------------------------------------------- database for payment---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_payment_table():
     c.execute('CREATE TABLE IF NOT EXISTS `payment` (`payment_id` int(11) NOT NULL AUTO_INCREMENT,`booking_id` int(11) NOT NULL,`amount_paid` float NOT NULL,`payment_date` date NOT NULL,`users_id` int(11) NOT NULL,PRIMARY KEY (`payment_id`),KEY `booking_id` (`booking_id`,`users_id`),KEY `user_id` (`users_id`))')


def add_payment(payment_id,booking_id,amount_paid,payment_date,users_id):
    c.execute('INSERT INTO payment(payment_id,booking_id,amount_paid,payment_date,users_id) '
              'VALUES (%s,%s,%s,%s,%s)',
              (payment_id,booking_id,amount_paid,payment_date,users_id))
    mydb.commit()


def view_all_payment():
    c.execute('SELECT * FROM payment')
    data = c.fetchall()
    return data


def view_only_payment():
    c.execute('SELECT payment_id from payment')
    data = c.fetchall()
    return data


def get_payment(payment_id):
    c.execute('SELECT * FROM payment WHERE payment_id="{}"'.format(payment_id))
    data = c.fetchall()
    return data


def edit_payment(new_payment_id, new_booking_id, new_amount_paid, new_payment_date, new_users_id, payment_id,booking_id,amount_paid,payment_date,users_id):
    c.execute("UPDATE payment SET payment_id=%s, booking_id=%s, amount_paid=%s, payment_date=%s, users_id=%s where payment_id=%s and booking_id=%s and amount_paid=%s and payment_date=%s and users_id=%s",
            (new_payment_id, new_booking_id, new_amount_paid, new_payment_date, new_users_id, payment_id,booking_id,amount_paid,payment_date,users_id))
    mydb.commit()
    #data = c.fetchall()
    #return data


def delete_payments(payment_id):
    c.execute('DELETE FROM payment WHERE payment_id="{}"'.format(payment_id))



#---------------------------------------------------------------- database for user-------------------------------------------------------------------------------------------------------------------


def create_user_table():
     c.execute('CREATE TABLE IF NOT EXISTS `user` (`users_id` int(11) NOT NULL AUTO_INCREMENT,`full_name` varchar(50) NOT NULL,`contact_no` varchar(15) NOT NULL,`email_address` varchar(30) NOT NULL,`username` varchar(30) NOT NULL,`userpassword` varchar(30) NOT NULL,`account_category` int(1) NOT NULL,`account_status` int(1) NOT NULL,PRIMARY KEY (`users_id`))')


def add_user(users_id,full_name,contact_no,email_address,username,userpassword,account_category,account_status):
    c.execute('INSERT INTO user(users_id,full_name,contact_no,email_address,username,userpassword,account_category,account_status) '
              'VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (users_id,full_name,contact_no,email_address,username,userpassword,account_category,account_status))
    mydb.commit()


def view_all_user():
    c.execute('SELECT * FROM user')
    data = c.fetchall()
    return data


def view_only_user():
    c.execute('SELECT users_id from user')
    data = c.fetchall()
    return data


def get_user(users_id):
    c.execute(f'SELECT * FROM user WHERE users_id="{users_id}"')
    data = c.fetchall()
    return data


def edit_user(new_users_id, new_fullname, new_contact_no, new_email_address, new_username, new_userpassword, new_account_category, new_account_status, users_id,full_name,contact_no,email_address,username,userpassword,account_category,account_status):
    c.execute("UPDATE user SET users_id=%s, full_name=%s, contact_no=%s, email_address=%s, username=%s, userpassword=%s, account_category=%s, account_status=%s where users_id=%s and full_name=%s and contact_no=%s and email_address=%s and username=%s and userpassword=%s and account_category=%s and account_status=%s",
            (new_users_id, new_fullname, new_contact_no, new_email_address, new_username, new_userpassword, new_account_category, new_account_status, users_id,full_name,contact_no,email_address,username,userpassword,account_category,account_status))
    mydb.commit()
    #data = c.fetchall()
    #return data


def delete_users(users_id):
    c.execute('DELETE FROM user WHERE users_id="{}"'.format(users_id))


#-------------------------Query--------------------------------

def create_query_table():
     c.execute('CREATE TABLE IF NOT EXISTS query (query varchar(255) NOT NULL)')

