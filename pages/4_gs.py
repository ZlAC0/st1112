import streamlit as st
import pandas as pd
st.title("구글시트 연동")
gs_id = st.secrets["gs_id"]
url = f"https://docs.google.com/spreadsheets/d/{gs_id}/gviz/tq?tqx=out:csv&gid=0"


s = pd.read_csv(url)
# st.dataframe(s)

q1 = s.iloc[0,1]
st.write("문제1:", q1)
a1 = st.number_input("답1 : " : )
if a1==int(s.iloc[0,2]):
    st.success("정답입니다!")
else:
    st.write("아님!")