from transformers import BertModel, BertTokenizer
import torch

# Load the model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Function to generate an embedding for a query
def generate_embedding(query):
    # Tokenize the query
    inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True)
    # Get the model's output (you may need to specify the output you want depending on the model)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Extract embeddings, typically by averaging the last hidden states across the token dimension
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings

# Example use
query = "What is the capital of France?"
query_vector = generate_embedding(query)
print(query_vector)
