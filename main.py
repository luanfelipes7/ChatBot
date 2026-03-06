import streamlit as st
from openai import OpenAI

# obtém chave segura do Streamlit secrets
api_key = st.secrets.get("openai_api_key")
if not api_key:
    st.error("Chave da OpenAI não encontrada em st.secrets. Verifique o arquivo .streamlit/secrets.toml")
    st.stop()

modelo_ia = OpenAI(api_key=api_key)
st.write("# Chatbot LFS7")

if not 'messages' in st.session_state:
    st.session_state['lista_mensagens'] = []

texto_usuario = st.chat_input("Digite sua mensagem:")

for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)

if texto_usuario:
    
    st.chat_message('user').write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state['lista_mensagens'].append(mensagem_usuario)
    
    resposta_ia = modelo_ia.chat.completions.create(messages = st.session_state['lista_mensagens'], model="gpt-4o")
    
    texto_resposta = resposta_ia.choices[0].message.content
    

    st.chat_message('assistant').write(texto_resposta)
    mensagen_ia = {"role": "assistant", "content": texto_resposta}
    st.session_state['lista_mensagens'].append(mensagen_ia)


