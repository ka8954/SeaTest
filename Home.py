from dotenv import load_dotenv
load_dotenv()
import os
import random
from supabase import create_client,Client
import streamlit as slt
import random
import pandas as pd

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url,key)

def main():
    slt.set_page_config(page_title="seaTest - Instructor Interface", page_icon="✨")
    slt.sidebar.title("")
    options = slt.sidebar.radio('Pages', options=("Entry", "Retreival"))

    def btn_click():
        print("Option Selected")

    def retreive():
        col1, col2, col3 = slt.columns([4.1, 9, 2])

        with col1:
            slt.write("")

        with col2:
            slt.image("srm.jpg", width=300)
            slt.write('Developed By Kaarthik Sai Charan Ayineni')

        with col3:
            slt.write("")
        slt.header('Student Wise Seating Arrangement')
        slt.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        doc = slt.file_uploader("Upload Your Excel Doc Here", type=["csv"])
        if doc is not None:
            df = pd.read_csv(doc)
            slt.dataframe(df)
    def entry():
        col1, col2, col3 = slt.columns([4.2, 9, 2])

        with col1:
            slt.write("")

        with col2:
            slt.image("srm.jpg", width=300)
            slt.write('Developed By Kaarthik Sai Charan Ayineni')

        with col3:
            slt.write("")

        slt.title('TEST SEATING ARRANGEMENT')
        slt.subheader('DEPT OF NETWORKING AND COMMUNICATIONS')
        slt.text(
            'This System Allocates Seating for Students belonging to Cloud Computing, Cyber Security, IT, IOT, Networking Specializations')
        slt.write('# Type Of Exam')
        radio_btr = slt.selectbox(' ',
                                  options=("Choose an One", "Internals", "University Theory"))
        slt.write('# Enter the Details')
        id = slt.text_input('USER ID', max_chars=15)
        UNAME = slt.text_input('USERNAME', max_chars=6)
        PWORD = slt.text_input('PASSWORD', max_chars=4)
        labcapacity = 50

        a = 1
        x = [i for i in range(a, labcapacity + 1)]
        random.shuffle(x)

        for i in range(0, 50):
            seat = x[i]
            if seat % 2 == 0:
                Setno = "SET-1"
            else:
                Setno = "SET-2"

        exam_date = slt.date_input("SELECT THE DATE OF EXAM")
        print(exam_date)

        if slt.button("SUBMIT"):
            d1 = supabase.table("seat").insert({"ID": id, "Username": UNAME, "Password": PWORD, "Sysno": seat, "Setno": Setno}).execute()
            assert len(d1.data) > 0
            slt.success("Data Saved")

    if options == 'Entry':
        entry()

    if options == 'Retreival':
        retreive()


if __name__ == '__main__':
    main()
