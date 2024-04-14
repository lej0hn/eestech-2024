import chromadb
from text_chunk import recipes_to_return


client = chromadb.PersistentClient(path="C:/Users/jdara/Desktop/eestec_2024/db_chroma")

collection = client.create_collection(name="Recipes")



recipes = recipes_to_return()
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

results = collection.query(
    query_texts=[" Eggs,  castor  sugar,  Marsala,  cinnamon,  lemon,  stick "],
    n_results=10
)

