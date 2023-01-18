import streamlit as st

# 타이틀 적용 예시
st.title('이것은 타이틀 입니다')

# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('스마일 :sunglasses:')

# Header 적용
st.header('헤더를 입력할 수 있어요! :sparkles:')

# Subheader 적용
st.subheader('이것은 subheader 입니다')

# 캡션 적용
st.caption('캡션을 한 번 넣어 봤습니다')

# 코드 표시
sample_code = '''
def function():
    print('hello, world')
'''
st.code(sample_code, language="python")

# 일반 텍스트
st.text('일반적인 텍스트를 입력해 보았습니다.')

# 마크다운 문법 지원
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
# 컬러코드: blue, green, orange, red, violet
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")

# LaTex 수식 지원
st.latex(r'\sqrt{x^2+y^2}=1')