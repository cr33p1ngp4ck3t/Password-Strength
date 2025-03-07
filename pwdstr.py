import streamlit as st
from collections import Counter
import random
import string

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")
 
keywords = [".", '!', '@', '#']
numList = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

st.header("Check Your Password Strength 🔑")

pwd = st.text_input("Enter a Password to check its strength", placeholder="Enter Password", type="password", key="input_key")

charCount = Counter(pwd)
if st.button("Check", type="primary"):
    if pwd.__len__() <= 6:
        st.markdown('❌:red-background[Please Enter Longer Password (min 8)]')
    else:
        key = [keyword for keyword in keywords if keyword in pwd]
        numerics = [nums for nums in numList if nums in pwd]
        if key:
            contains = [up for up in pwd if up.isupper()]
            if contains:
                st.write("✅:green[Password should atleast contain one Capital Character]")
            else :
                st.write("❌:red[Password should atleast contain one Capital Character]")
            duplicates = {char: count for char, count in charCount.items() if count > 2}
            if duplicates:
                st.markdown("❌:red[There Should not be more than 2 Duplicates]")
            else:
                st.markdown("✅:green[There Should not be more than 2 Duplicates]")
            if numerics:
                st.markdown(f"✅:green[Password should contain numeric values (0-9)]")
            else:
                st.markdown(f"❌:red[Password should contain numeric values (0-9)]")
            st.markdown('✅:green[Password should contain: `.` | `!` | `@` | `#`]')
        else:
            st.markdown('❌:red[Password should contain: `.` | `!` | `@` | `#`]')

space = st.empty()
space.html("<br/> <br/>")

if st.checkbox("Do you Want to Be Suggested a Strong Password??"):
    st.subheader("Suggested Strong Password")
    if "password" not in st.session_state:
        st.session_state.password = ''

    len = st.number_input("What should be the Length of your Password?", value=8, step=1)
    if st.button("Suggest 💭?"):
            characters = list(string.ascii_letters + string.digits + ".!@#")
            st.session_state.password = ''.join(random.choice(characters) for _ in range(len))            

    if st.session_state.password:
        st.write(f"Suggested Password: `{st.session_state.password}`")

