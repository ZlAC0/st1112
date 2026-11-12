import streamlit as st

st.title("1112 실습")

with st.expander("실습 안내", expanded=False, ):
    st.write("""
    어쩌고 저쩌고 되게 긴 말을 이렇게 expander로 숨기는 에제
    """)

a, b, c =st.tabs(["문제1", "문제2", "문제3"])
with a: 
    st.subheader("1. 식 전개하기")
    st.latex(r"(x+y)^2 ")

    with st.form("form1"):
        answer1 = st.radio("선택하세요", [r"$x^2 +y^2$", r"$x^2 +y^2 +2xy$", r"$x^2+y^2+xy$"], index=None)
        st.session_state.ans1 = answer1
        submitted = st.form_submit_button("제출")

    if submitted:
        if st.session_state.ans1 is None:
            st.warning("답을 먼저 선택해주세요.")
        elif st.session_state.ans1 == r"$x^2 +y^2 +2xy$":
            st.success("정답입니다! xy와 yx를 더하면 2xy가 됩니다.")
            st.latex(r"(x+y)^2 = (x+y)(x+y) = x^2+xy+yx+y^2 = x^2+2xy+y^2")
        elif st.session_state.ans1 == r"$x^2 +y^2$":
            st.error("각 항을 제곱한 것만 더하면 빠지는 항이 있어요. x와 y를 곱해서 생기는 항도 생각해보세요.")
            st.latex(r"(x+y)(x+y) = x^2+xy+yx+y^2")
        else:
            st.error("xy는 한 번만 생길까요? 앞의 x와 뒤의 y, 앞의 y와 뒤의 x를 각각 곱해보세요.")
            st.latex(r"xy+yx = 2xy")

with b:
    st.subheader("2. 일차방정식 풀기")
    st.latex(r"3x+5=14")

    with st.form("form2"):
        answer2 = st.radio("방정식을 만족하는 x의 값을 선택하세요", [r"$x=3$", r"$x=9$", r"$x=\frac{19}{3}$"], index=None)
        submitted = st.form_submit_button("제출")

    if submitted:
        if answer2 is None:
            st.warning("답을 먼저 선택해주세요.")
        elif answer2 == r"$x=3$":
            st.success("정답입니다! 양변에서 5를 뺀 다음, 양변을 3으로 나누면 됩니다.")
            st.latex(r"3x=14-5=9 \quad\Rightarrow\quad x=3")
        elif answer2 == r"$x=9$":
            st.error("9는 3x의 값이에요. x의 값을 구하려면 양변을 3으로 나누어야 해요.")
            st.latex(r"3x=9 \quad\Rightarrow\quad x=\frac{9}{3}")
        else:
            st.error("왼쪽의 +5를 없애려면 양변에서 5를 빼야 해요. 오른쪽에 5를 더하지 않도록 주의하세요.")
            st.latex(r"3x+5-5=14-5 \quad\Rightarrow\quad 3x=9")




    st.session_state.ans2 = answer2
