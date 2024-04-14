import streamlit as st
import backend




# Streamlit interface
st.title("Talk to the LLM via LM Studio")

# Text input for user query
user_input = st.text_area("Enter your message:", help="Type your message and press enter.")

# Button to send the request
if st.button("Send"):
    if user_input:
        # Fetch response from the LLM
        response = backend.get_llm_response(user_input)
        # Display the response
        st.write("LLM Response:", response)
    else:
        st.error("Please enter some text to send to the LLM.")
