import streamlit as st



st.title("회원가입")
id= st.text_input("사용자ID")
pw= st.text_input("비밀번호",type='password')
pw_check=st.text_input("비밀번호 재확인",type='password')
name=st.text_input("이름")

st.radio('학년을 고르시오',['1학년','2학년','3학년'])

btn=st.button("회원가입")

