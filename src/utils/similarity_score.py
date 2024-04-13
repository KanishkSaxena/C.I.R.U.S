from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import CrossEncoder
import numpy as np


model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

def calculate_similarity(question_embedding, chunk_embedding):
   
    """
    Cosine similarity between question embedding and chunk embedding.
    """
    sim = cosine_similarity(question_embedding.reshape(1, -1), chunk_embedding.reshape(1, -1))
    return sim[0][0]

def get_top_5_chunks(question, all_chunks, metadatas):
    """
    Top 5 chunks based on word embeddings similarity with the question.
    """
    question_embedding = model.encode(question)
    all_chunk_embeddings = [model.encode(str(chunk)) for chunk in all_chunks]
    similarities = [(chunk, metadata, calculate_similarity(question_embedding, chunk_embedding)) for chunk, metadata, chunk_embedding in zip(all_chunks, metadatas, all_chunk_embeddings)]
    top_5_chunks = sorted(similarities, key=lambda x: x[2], reverse=True)[:5]
    return top_5_chunks

# from sentence_transformers import CrossEncoder

# model = CrossEncoder('cross-encoder/stsb-roberta-large')

# def calculate_similarity(question, chunk):
#     similarity_score = model.predict([(question, chunk)])
#     return similarity_score[0]

# def get_top_5_chunks(question, all_chunks,metadatas):
#     similarities = [(chunk, metadata, calculate_similarity(question, str(chunk))) for chunk,metadata in zip(all_chunks,metadatas)]
#     top_5_chunks = sorted(similarities, key=lambda x: x[2], reverse=True)[:5]
#     return top_5_chunks
