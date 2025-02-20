# Searching-system

Searching-system is a modular, Python-based search engine prototype that builds an inverted index for efficient document retrieval. It supports multiple query types—basic, phrase, wildcard, and fuzzy searches—combined with BM25 ranking for improved relevance. The architecture is designed to be easily extensible, allowing for future enhancements like personalized search and semantic analysis using word embeddings.

## Features

- **Inverted Index Construction:**  
  Efficiently indexes a collection of documents by mapping tokens to document IDs and their positions.

- **Multiple Search Modes:**  
  - **Basic Search:** Retrieve documents containing individual keywords.
  - **Phrase Search:** Look for exact sequences of words.
  - **Wildcard Search:** Use wildcards (e.g., `prog*`) to match patterns.
  - **Fuzzy Search:** Handle approximate matches for misspelled or similar words.

- **Advanced Ranking with BM25:**  
  Applies the BM25 ranking algorithm to score and sort results based on relevance.

- **Modular Architecture:**  
  Clearly separated components for tokenization, indexing, querying, and ranking make the system easy to maintain and extend.

- **Unit Tested:**  
  Comprehensive tests ensure that each component functions correctly.



This project is a mini search engine implemented in Python that demonstrates core data structures and algorithms for information retrieval. It builds an inverted index to efficiently search through a collection of documents. 
The system supports various search modes including basic search, phrase search, wildcard search, and fuzzy search. It also features an advanced ranking mechanism using BM25, and the architecture is designed for further enhancements 
such as personalized ranking and semantic analysis with word embeddings. This project is ideal for learning and showcasing skills in text processing, indexing, query processing, and ranking algorithms.

