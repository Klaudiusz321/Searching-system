from src.tokenizer import tokenize


def build_inverted_index(documents):
   
    inverted_index = {}
    for doc_id, text in documents.items():
        words = tokenize(text)
        for pos, word in enumerate(words):
            if word not in inverted_index:
                inverted_index[word] = {}
            if doc_id not in inverted_index[word]:
                inverted_index[word][doc_id] = []
            inverted_index[word][doc_id].append(pos)
    return inverted_index
