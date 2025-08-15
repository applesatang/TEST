import streamlit as st

st.title("🎈 파이콘 튜토리얼")
st.info ("안녕하세요, 파이콘 튜토리얼 예제입니다.")


st.subheader("첫 번째 앱")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-LUAXUklnGhHVtTtyY8VqaIhW20t_mfhFSg&s", caption="펭귄")

st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")


st.write("https://www.naver.com")
st.link_button("네이버 바로가기","https://www.naver.com")
