from openai import OpenAI
from final import chroma_file2

# Initialize the OpenAI client to connect to your local LM Studio server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_llm_response(user_input):
    # This is a simplified example where the system's role does not change dynamically
    # system_content = "Always answer as a chef. Your answer should be 50 words max."
    
    db_input = chroma_file2.database_function(user_input)

    # Create a completion request to the LLM
    completion = client.chat.completions.create(
        model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
        messages=[
            {"role": "system", "content": "Give an answer of max 50 words. Act as a chef. Use this to answer the question" + " " + str(db_input).replace("\n", "")},
            {"role": "user", "content": user_input}
        ],
        temperature=0.2,
    )
    
    # Return the response message from the LLM
    return completion.choices[0].message.content