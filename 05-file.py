import streamlit as st
import pandas as pd
import time

# 파일 업로드 버튼 (업로드 기능)
file = st.file_uploader("파일 선택(csv or excel)", type=['csv', 'xls', 'xlsx'])

# 파일이 정상 업로드 된 경우
# if file is not None:
#     # 파일 읽기
#     df = pd.read_csv(file)
#     # 출력
#     st.dataframe(df)

time.sleep(3)

# Excel or CSV 확장자를 구분하여 출력하는 경우
if file is not None:
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        # 파일 읽기
        df = pd.read_csv(file)
        # 출력
        st.dataframe(df)
    elif 'xls' in ext:
        # 엑셀 로드
        df = pd.read_excel(file, engine='openpyxl')
        # 출력
        st.dataframe(df)