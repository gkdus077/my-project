import streamlit as st
from tkinter.tix import COLUMN

st.title("playlist🎵")

col1, col2 =st.columns([2,1])

with col1:
    st.header('재생 완료')

with col2:
    st.header("재생 전")
    st.image('/Users/hyeonhayeon/Downloads/요츠바랑 - 조금만 더 기다려 주세요_ 늦어져서 정말 죄송합니다!.jpg')

    


