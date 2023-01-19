import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

# 버튼 클릭
button = st.button('버튼을 눌러보세요')

if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')


# 파일 다운로드 버튼
# 샘플 데이터 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# 다운로드 버튼 연결
st.download_button(
    label='CSV로 다운로드',
    data=dataframe.to_csv(), 
    file_name='sample.csv', 
    mime='text/csv'
)

# 체크 박스
agree = st.checkbox('동의 하십니까?')

if agree:
    st.write('동의 해주셔서 감사합니다 :100:')

# 라디오 선택 버튼
mbti = st.radio(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ENFP', '선택지 없음'))

if mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ENFP', '선택지 없음'), 
    index=2
)

if mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# 다중 선택 박스
options = st.multiselect(
    '당신이 좋아하는 과일은 뭔가요?',
    ['망고', '오렌지', '사과', '바나나'],
    ['망고', '오렌지'])

st.write(f'당신의 선택은: :red[{options}] 입니다.')


# 슬라이더
values = st.slider(
    '범위의 값을 다음과 같이 지정할 수 있어요:sparkles:',
    0.0, 100.0, (25.0, 75.0))
st.write('선택 범위:', values)

start_time = st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2020, 1, 1, 0, 0), 
    max_value=dt(2020, 1, 7, 23, 0),
    value=dt(2020, 1, 3, 12, 0),
    step=datetime.timedelta(hours=1),
    format="MM/DD/YY - HH:mm")
st.write("선택한 약속 시간:", start_time)


# 텍스트 입력
title = st.text_input(
    label='가고 싶은 여행지가 있나요?', 
    placeholder='여행지를 입력해 주세요'
)
st.write(f'당신이 선택한 여행지: :violet[{title}]')

# 숫자 입력
number = st.number_input(
    label='나이를 입력해 주세요.', 
    min_value=10, 
    max_value=100, 
    value=30,
    step=5
)
st.write('당신이 입력하신 나이는:  ', number)
