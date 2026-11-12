import streamlit as st


st.title("11/12 실습")

# 초기화
if "saved_a1" not in st.session_state:
    st.session_state.saved_a1 = ""
if "saved_a2" not in st.session_state:
    st.session_state.saved_a2 = ""

with st.form("forms1"):
    a1 = st.text_input("a1")
    s1 = st.form_submit_button("제출 1")

if s1:
    st.session_state.saved_a1 = a1

with st.form("forms2"):
    a2 = st.text_input("a2")
    s2 = st.form_submit_button("제출 2")


if s2:
    st.session_state.saved_a2 = a2  


st.divider()
st.write("기억된 a1:", st.session_state.saved_a1)
st.write("기억된 a2:", st.session_state.saved_a2)


a1 = st.session_state.saved_a1
a2 = st.session_state.saved_a2

