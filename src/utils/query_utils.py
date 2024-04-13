from concurrent.futures import ThreadPoolExecutor


def query_vector_db(vector_db, question):
    relevant_chunks = vector_db.query(query_texts=[question], n_results=5)
    documents = relevant_chunks['documents']
    metadatas = relevant_chunks['metadatas']
    return documents, metadatas


