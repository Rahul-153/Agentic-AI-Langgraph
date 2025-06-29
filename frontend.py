import streamlit as st
import requests

st.set_page_config(
    page_title="Langraph AI Agent",
    layout="wide")

st.title("Langraph AI Agent")
st.write("This is a simple frontend for the Langraph AI Agent. You can interact with the agent by sending messages and receiving responses.")

system_prompt = st.text_area("Define the role of your Agnet: ", height= 70,placeholder="Type your system prompt here...")

MODEL_NAMES=["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "deepseek-r1-distill-llama-70b"]

model=st.selectbox("Select a model:", MODEL_NAMES)

allow_search = st.checkbox("Allow Web search")

user_query = st.text_area("Type your message here:", height= 150, placeholder="Type your message here...")   

payload = {
    "system_prompt": system_prompt,
    "messages": [user_query],
    "allow_search" : allow_search,
    "model" : model
}

url="http://127.0.0.1:8000/chat"

if st.button("Ask Agent"):
    response = "Hi, this is a fixed dummy response"
    if not user_query:
        st.error("Please enter a message.")
    elif not system_prompt:
        st.error("Please define the role of your agent.")
    else:
        user_query = user_query.strip()
        response=requests.post(url, json=payload)
        if response.status_code == 200:
            response=response.json()
            st.subheader("Response from Agent:")
            st.markdown(f"**Final Response:** {response}")