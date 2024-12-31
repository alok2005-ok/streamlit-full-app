import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse

DB_HOST = "127.0.0.1"  
DB_PORT = "3306"  
DB_NAME = "student_database"  
DB_USER = "root"  
DB_PASSWORD = urllib.parse.quote("123456")

db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

def update_data(student_id,field,new_value):
    query = text(f"update student_data SET {field}=:new_value WHERE id = :student_id")
    with engine.connect() as conn :
        conn.execute(query,{"new_value":new_value,"student_id":student_id})
        conn.commit()

st.title("update student data")
student_id = st.number_input("enter student id to update",min_value=1,step=1)
field = st.selectbox("field to update",["firstname","lastname","title","age","nationlity","registration_status","num_course","num_semesters"])
new_value = st.text_input("new value")

if st.button("update"):
    try:
        update_data(student_id,field,new_value)
        st.success("dta sucessfully update")
    except Exception as e:
        st.error(f"error updating data:{e}")
