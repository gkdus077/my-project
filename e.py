import streamlit as st
from tkinter.tix import COLUMN

st.title("playlist🎵")

col1, col2 =st.columns([2,1])

with col1:
    st.header('재생 완료')

with col2:
    st.header("재생 전")



