import streamlit as st
from langchain.chains import VectorDBQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

import os
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="LLM question answering Assistant")

# From here down is all the Streamlit UI

st.header("LLM Question Answaring Assistant :robot_face:")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

with st.form(key="form"):
    user_input = st.text_input("you: ", "Hello, what do you want to know?", key="input")
    submit_button_pressed = st.form_submit_button("submit to Bot")

if submit_button_pressed:
    result ={"result": user_input[::-1]}
    output = f"Answer: {result['result']}"

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -2):
        st.message(st.session_state["generated"][i], key=str(i))
        st.message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
