import chromadb
from final import text_chunk


client = chromadb.PersistentClient(path="C:/Users/User/OneDrive/Υπολογιστής/eestech-2024/chromadb")

collection = client.create_collection(name="Recipes")



recipes = text_chunk.recipes_to_return()
documents = []
metadatas = []
ids = []
for key, value in recipes.items():
    documents.append(value)
    metadata = {"source": key}
    metadatas.append(metadata)
    ids.append("id_" + str(len(documents)))

collection.add(
    documents = documents,
    metadatas = metadatas,
    ids = ids
)

# results = collection.query(
#     query_texts=[" Eggs,  castor  sugar,  Marsala,  cinnamon,  lemon,  stick "],
#     n_results=10
# )




