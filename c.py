import streamlit as st

st.title("로그인")

id=st.text_input("ID")
pw=st.text_input("비밀번호")

btn=st.button("로그인")

