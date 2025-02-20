import math
from src.tokenizer import preprocess_text

def bm25_ranking(query, documents, inverted_index, k=1.5, b=0.75):
   
    query_tokens = preprocess_text(query)
    N = len(documents)
    
    avgdl = sum(len(preprocess_text(doc)) for doc in documents.values()) / N

    scores = {doc_id: 0 for doc_id in documents.keys()}

    for term in query_tokens:
        
        df = len(inverted_index.get(term, {}))
        if df == 0:
            continue
        idf = math.log((N - df + 0.5) / (df + 0.5) + 1)
        
        for doc_id, positions in inverted_index.get(term, {}).items():
            f = len(positions)
            doc_len = len(preprocess_text(documents[doc_id]))
            score = idf * ((f * (k + 1)) / (f + k * (1 - b + b * (doc_len / avgdl))))
            scores[doc_id] += score

    return scores
def personalize_scores(bm25_scores, user_profile, alpha=0.2):
    
    personalized = {}
    for doc_id, score in bm25_scores.items():
        
        preference = user_profile.get(doc_id, 0)
        personalized[doc_id] = score * (1 + alpha * preference)
    return personalized
