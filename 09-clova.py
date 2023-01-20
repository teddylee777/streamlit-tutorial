import json
import configparser
import http.client
import streamlit as st


class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def _send_request(self, completion_request):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id
        }

        conn = http.client.HTTPSConnection(self._host)
        conn.request('POST', '/testapp/v1/completions/LK-D', json.dumps(completion_request), headers)
        response = conn.getresponse()
        result = json.loads(response.read().decode(encoding='utf-8'))
        conn.close()
        return result

    def execute(self, completion_request):
        res = self._send_request(completion_request)
        if res['status']['code'] == '20000':
            return res['result']['text']
        else:
            return 'Error'


config = configparser.ConfigParser()
config.sections()
config.read('./your_apikey.ini')

completion_executor = CompletionExecutor(
    host=config['CLOVA']['host'],
    api_key=config['CLOVA']['api_key'],
    api_key_primary_val=config['CLOVA']['api_key_primary_val'],
    request_id=config['CLOVA']['request_id']
)

st.title('나만의 챗봇')

preset_input = st.selectbox(
    '사전 문장',
    ('MBTI에 대한 지식을 기반으로, 아래의 질문에 답해보세요.', 
    '키워드를 포함하여 설날 인사말을 생성합니다.',
    '30대 남성으로 질문에 군인말투로 끝을 다,나,까로 대답한다.',
    ), 
    index=1
)

question = st.text_area(
    '질문', 
    placeholder='질문을 입력해 주세요', 
)

if preset_input and question:
    preset_text = f'{preset_input}\n\n질문:{question}'

    request_data = {
        'text': preset_text,
        'maxTokens': 100,
        'temperature': 0.5,
        'topK': 0,
        'topP': 0.8,
        'repeatPenalty': 5.0,
        'start': '\n###답:',
        'stopBefore': ['###', '질문:', '답:', '###\n'],
        'includeTokens': True,
        'includeAiFilters': True,
        'includeProbs': True
    }

    response_text = completion_executor.execute(request_data)
    # print(preset_text)
    print(response_text)
    st.markdown(response_text.split('###')[1])