from src.indexer import build_inverted_index
from src.utils import load_documents
from src.tokenizer import preprocess_text
from src.query import boolean_query, phrase_query, wildcard_query, fuzzy_query
from src.ranking import bm25_ranking

def main():
    documents = load_documents()
    index = build_inverted_index(documents)
    
    print("Choose a search mode:")
    print("1. Basic search")
    print("2. Phrase search")
    print("3. Wildcard search")
    print("4. Fuzzy search")
    
    mode = input("Enter the mode number: ")
    query = input("Enter your query: ")

    if mode == "2":
        results = phrase_query(query, index)
    elif mode == "3":
        results = wildcard_query(query, index)
    elif mode == "4":
        results = fuzzy_query(query, index)
    else:
        # Default basic search: search by individual words.
        results = set()
        for term in preprocess_text(query):
            results |= set(index.get(term, {}).keys())
    
    if not results:
        print("No results found.")
        return
    
    # Calculate BM25 ranking for all documents.
    scores = bm25_ranking(query, documents, index)
    # Filter the BM25 scores to include only the documents returned by the chosen search mode.
    ranked_results = {doc_id: scores[doc_id] for doc_id in results}
    sorted_results = sorted(ranked_results.items(), key=lambda x: x[1], reverse=True)
    
    print("Search Results (doc_id - score):")
    for doc_id, score in sorted_results:
        print(f"{doc_id} - {score}")

if __name__ == "__main__":
    main()
