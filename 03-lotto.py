import streamlit as st
import random
import datetime

st.title(':sparkles:로또 생성기:sparkles:')


def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 46)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto

# st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
# st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

button = st.button('로또를 생성해 주세요!')

if button:
    for i in range(1, 6):
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

