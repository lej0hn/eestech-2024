from transformers import AutoModelForCausalLM, AutoTokenizer

# Correct class for tokenizer
tokenizer = AutoTokenizer.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.2-GGUF")

# Correct class for model
model = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.2-GGUF")


# Function to generate an embedding for a query
def generate_embedding(query):
    # Tokenize the query
    inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True)
    # Get the model's output
    with torch.no_grad():
        outputs = model(**inputs)
    
    # You may choose to use the last hidden states or another layer
    hidden_states = outputs.last_hidden_state

    # Aggregate the hidden states to get a single vector (e.g., mean pooling)
    embeddings = hidden_states.mean(dim=1)
    return embeddings

# Example use
query = "What is the capital of France?"
query_vector = generate_embedding(query)
print(query_vector)
