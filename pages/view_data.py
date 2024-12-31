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


def fetch_data():
    query = text("select * from student_Data")
    try :
        with engine.connect() as conn :
            result = conn.execute(query)
            columns = result.keys ()
            data = [dict(zip(columns,row)) for row in result]
            return data
    except Exception as e :
        st.error (F"error fetching data : {e}")
        return []
    

st.title("view student data")

data = fetch_data () 
if data:
    st.table(data)
else:
    st.info("no  data found in tha database.")