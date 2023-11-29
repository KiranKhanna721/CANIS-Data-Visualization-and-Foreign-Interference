import numpy as np
import streamlit as st
import pandas as pd
import hashlib
import sqlite3 
import app1
import app2
import app3


def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():
    st.title("CANIS Data Visualization and Foreign Interference")
    st.image("https://assets.everspringpartners.com/dims4/default/c65c8ef/2147483647/strip/true/crop/620x250+0+0/resize/620x250!/format/webp/quality/90/?url=http%3A%2F%2Feverspring-brightspot.s3.us-east-1.amazonaws.com%2Fe4%2F2a%2Fe9a3904c4f17a084c100bbbb5eca%2Fdata-visualization-for-accountants-620x250.jpg")
    menu = ["Login","SignUp"]
    st.write("The dataset evolved as a compass in the attempt to comprehend the global digital world, leading explorers through the stories of various entities. Individuals and organizations intentionally utilized social media channels in order to cross cultures and exchange tales. A mosaic of social media analytics, the dataset became a source of inspiration for developing effective digital campaigns. It highlighted the potential of internet storytelling in connecting with audiences across borders and languages. Each data point shed light on the influence of digital voices, arousing interest and motivating a deeper dive into the ever-changing social media world.")
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Login":
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                st.success("Logged In as {}".format(username))
                PAGES = {
                    "Social Media Followers Dashboard": app1,
                    "Social Media Followers Comparison":app2,
                    "Sum of Total Follwers VS Region Of focus":app3
                    }
                st.sidebar.title('CANIS Data Visualization and Foreign Interference')
                selection = st.sidebar.radio("Go to", list(PAGES.keys()))
                page = PAGES[selection]
                page.app()
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')
        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")



if __name__ == '__main__':
    main()