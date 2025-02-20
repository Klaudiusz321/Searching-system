import re
import difflib
from src.tokenizer import preprocess_text



def boolean_query(query, inverted_index):
    
    tokens = query.lower().split()
    result = None
    operator = None

    for token in tokens:
        if token in {"and", "or", "not"}:
            operator = token
        else:
            
            docs = set(inverted_index.get(token, {}).keys())
            if result is None:
                result = docs
            else:
                if operator == "and":
                    result = result & docs
                elif operator == "or":
                    result = result | docs
                elif operator == "not":
                    result = result - docs
            operator = None 
    return result if result is not None else set()

def phrase_query(phrase, inverted_index):
    
    words = preprocess_text(phrase)
    if not words:
        return set()
    
    common_docs = set(inverted_index.get(words[0], {}).keys())
    for word in words[1:]:
        common_docs &= set(inverted_index.get(word, {}).keys())
    
    result_docs = set()
    for doc_id in common_docs:
        positions_list = [inverted_index[word][doc_id] for word in words]
        if check_phrase_sequence(positions_list):
            result_docs.add(doc_id)
    return result_docs

def check_phrase_sequence(positions_list):
    
    for p in positions_list[0]:
        match = True
        for offset in range(1, len(positions_list)):
            if (p + offset) not in positions_list[offset]:
                match = False
                break
        if match:
            return True
    return False

def wildcard_query(pattern, inverted_index):
    regex = re.compile('^' + pattern.replace('*', '.*') + '$')
    matching_docs = set()
    for word in inverted_index.keys():
        if regex.match(word):
            matching_docs |= set(inverted_index[word].keys())
    return matching_docs

import difflib

def fuzzy_query(term, inverted_index, threshold=0.8):
    term = term.lower()
    matching_docs = set()
    words = list(inverted_index.keys())
    matches = difflib.get_close_matches(term, words, cutoff=threshold)
    for word in matches:
        matching_docs |= set(inverted_index[word].keys())
    return matching_docs
