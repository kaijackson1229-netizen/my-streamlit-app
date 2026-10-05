import streamlit as st

st.title("我的第一個 Streamlit web")

name = st.text_input("請輸入姓名")

if st.button("送出"):
    st.write("你好", name)