import streamlit as st
import backend 
import random
import time

# Set page configuration with a dark theme
st.set_page_config(page_title="Chef Helper AI", page_icon="👩‍🍳", layout="wide")

# Custom styles for dark theme and chatbot-like UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    #f1e6e1cf {
        margin-top: -3rem;
        margin-left: 0.2rem;
    }
    .chat-message {
        padding: 0.5rem 1rem;
        margin: 0.25rem;
        border-radius: 1rem;
        background-color: #20232a;
        color: #ffffff;
    }
    .user-message {
        background-color: #007bff;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #20232a;
        color: #ffffff;
        border-radius: 1rem;
        border: 0;
    }
    .stButton > button {
        border-radius: 1.5rem;
        border: 0;
        padding: 0.25rem 1rem;
        background-color: #007bff;
        color: #ffffff;
        box-shadow: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        transition: background-color 0.3s, box-shadow 0.3s;
    }
    .stButton > button:hover {
        background-color: #0056b3;
        box-shadow: 0 0 0.5rem #ffffff;
    }
    .stButton > button:focus {
        outline: none;
        box-shadow: 0 0 0.5rem #ffffff;
    }
    .send-icon {
        font-size: 1.5rem;
        margin-left: 0.5rem;
    }
    .stSidebar > div:first-child {
        width: 300px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Placeholder for the sidebar image file
st.sidebar.empty()



# Streamed response emulator
def response_generator(temp2):
    response = temp2
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("👩‍🍳 Chef AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        temp = backend.get_llm_response(prompt)
        response = st.write_stream(response_generator(temp))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})