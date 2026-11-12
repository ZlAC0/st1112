
import sympy as sp
import streamlit as st

x = sp.symbols('x')
y=sp.symbols('y')

exp = x**2 + 2*x
st.write("Expression:", exp)

eq1 = sp.Eq(exp,3)
sp.solve(eq1, x)
st.write( sp.solve(eq1, x))

