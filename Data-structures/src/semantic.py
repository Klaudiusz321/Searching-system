from gensim.models import KeyedVectors
import numpy as np
from numpy.linalg import norm
from src.tokenizer import preprocess_text


def load_embeddings():
    from gensim.downloader import load
    model = load("glove-wiki-gigaword-50")
    return model

def average_vector(text, model):
    tokens = preprocess_text(text)
    
    vectors = [model[word] for word in tokens if word in model]
    if not vectors:
        return None
    return np.mean(vectors, axis=0)

def cosine_similarity(vec1, vec2):
    if vec1 is None or vec2 is None:
        return 0
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def semantic_similarity(query, documents, model):
    
    query_vec = average_vector(query, model)
    similarities = {}
    for doc_id, text in documents.items():
        doc_vec = average_vector(text, model)
        similarities[doc_id] = cosine_similarity(query_vec, doc_vec)
    return similarities
