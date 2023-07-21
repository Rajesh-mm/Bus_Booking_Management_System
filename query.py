import streamlit as st
import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="bbmsystem")
c = mydb.cursor(dictionary=True)
def query():  # NO NEED TO CHANGE THIS 
    with st.form(key="form1"):
        str1=st.text_area("Enter the query here:")
        submit=st.form_submit_button("Submit")
        if(submit):
            try:
                c.execute(str1)
                df=pd.DataFrame(c.fetchall())
                st.table(df)
            except mysql.connector.Error as e:
                st.warning(e)