import streamlit as st
from openai import OpenAI

api_key= st.text_input("OpenAI API Key", type="password")
client = OpenAI(api_key=api_key)

st.title("OpenAI GPT model")

prompt = st.text_area("User prompt")

if st.button("Ask!", disabled=(len(prompt)==0)):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    st.write(response.output_text)
import streamlit as st
import openai
import os

# Streamlit 앱 제목
st.title("💬 GPT-4.1-mini 챗봇")

# OpenAI API 키 입력받기
api_key = st.text_input("🔑 OpenAI API Key를 입력하세요", type="password")

# API 키가 입력되었을 때만 실행
if api_key:
    openai.api_key = api_key

    # 사용자로부터 프롬프트 입력받기
    prompt = st.text_area("✍️ 질문을 입력하세요")

    # '질문하기' 버튼 클릭 시 응답 생성
    if st.button("질문하기") and prompt:
        try:
            # GPT-4.1-mini 모델을 사용하여 응답 생성
            response = openai.ChatCompletion.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            # 응답 출력
            st.markdown("### 🤖 GPT-4.1-mini의 응답:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
else:
    st.warning("먼저 OpenAI API 키를 입력해주세요.")

streamlit
openai

streamlit run app.py
