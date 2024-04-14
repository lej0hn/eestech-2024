import chromadb


client = chromadb.PersistentClient(path="C:/Users/User/OneDrive/Υπολογιστής/eestech-2024/chromadb")

collection = client.get_collection(name="Recipes")

def database_function(input):
    results = collection.query(
        query_texts=input,
        n_results=1
    )
    
    print(results)
    return results['documents'][0][0]