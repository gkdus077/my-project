import streamlit as st

st.title("신청방")

st.warning("19금 노래는 피해주세요🔞")
st.warning("5분 이상인 노래는 피해주세요.")

st.text_input("신청곡 제목을 입력해주세요.")
st.text_input("가수명을 입력해주세요.")

btn= st.button("신청")