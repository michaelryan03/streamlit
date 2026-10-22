import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="📊",
    layout="wide"
)

st.title("Ứng dụng Streamlit")
st.write("Website đang chạy trên máy chủ cloud.")

st.success("Triển khai thành công!")

st.subheader("Kiểm tra hoạt động")

name = st.text_input("Nhập tên của bạn")

if st.button("Xác nhận"):
    if name.strip():
        st.write(f"Xin chào, {name}!")
    else:
        st.warning("Vui lòng nhập tên.")

st.caption(
    f"Thời gian hiện tại trên máy chủ: "
    f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
)
