# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = mysql.connector.connect(host='localhost',user='root',password='dbmsproject',database='new_schema')
cursor = conn.cursor()
# Perform query.
query = "SELECT * from seat"
cursor.execute(query)

results = cursor.fetchall()

# Print results.
for row in df.itertuples():
    st.write(f"{row.ID} {row.USERNAME} {row.Password} {row.Sysno} {row.Setno} {row.ExamDate}:")
conn.close()
