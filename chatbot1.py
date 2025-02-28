import streamlit as st
import google.generativeai as genai
API_KEY="AIzaSyB121TcLtRHJjHECYdHzG8Ze_8KzpC3BKQ"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
  
st.title("🏎️RoboDrive -  Your Autonomous Vehicle Assistant🏎️")
st.write("Welcome! Ready to navigate the world of Baja SAE and self-driving cars? Let’s chat!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("Say something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    response = st.session_state.chat.send_message(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)
