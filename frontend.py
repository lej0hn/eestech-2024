import streamlit as st
import backend




# Streamlit interface
st.title("Welcome!")

# Text input for user query
user_input = st.text_area("Enter your message:", help="Type your message and hit 'Send'.")

# Button to send the request
if st.button("Send"):
    if user_input:
        # Fetch response from the LLM
        response = backend.get_llm_response(user_input)
        # Display the response
        st.write(response)
    else:
        st.error("Please enter your question.")
