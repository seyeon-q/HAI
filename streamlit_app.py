import streamlit as st
import requests

class GeminiModel:
    def __init__(self):
        self.api_key = "AIzaSyDe9UFXv_alDFd5EZZSDNCm8g2hoddK890"
        self.api_url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'  # 실제 API URL로 교체

    def get_response(self, query):
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'contents': [
                {
                    'parts': [
                        {
                            'text': query
                        }
                    ]
                }
            ]
        }
        params = {
            'key': self.api_key
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload, params=params)
            response.raise_for_status()  # HTTPError 발생 시 예외 처리
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {str(e)}"

def main():
    model = GeminiModel()

    st.title("Gemini API Chat")
    st.markdown("—")

    st.subheader("Ask a question to Gemini")
    query = st.text_input('Enter your question here:')

    if query:
        with st.spinner('Fetching response…'):
            response = model.get_response(query)
        st.markdown("—")
        st.markdown("### **Response**")
        st.write(response)

if __name__ == "__main__":
    main()
