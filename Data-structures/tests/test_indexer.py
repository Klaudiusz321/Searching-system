import unittest
from src.indexer import build_inverted_index
from src.tokenizer import tokenize

class TestIndexer(unittest.TestCase):
    def setUp(self):
        # Example documents for testing
        self.documents = {
            1: "Python is a programming language.",
            2: "Programming in Python is simple."
        }
        # Build the inverted index based on the documents
        self.index = build_inverted_index(self.documents)
    
    def test_index_contains_words_from_doc1(self):
        
        words_doc1 = tokenize(self.documents[1])
        for word in words_doc1:
            self.assertIn(1, self.index.get(word, {}), f"Word '{word}' does not contain document 1")
    
    def test_index_positions(self):
       
        words_doc1 = tokenize(self.documents[1])
        first_word = words_doc1[0]
        # We assume that the first occurrence of the first word has index 0
        self.assertIn(0, self.index[first_word][1], f"Position 0 is not recorded for word '{first_word}' in document 1")
    
    def test_index_for_non_existing_word(self):
       
        self.assertIsNone(self.index.get("nonexistent"), "There should be no index for a non-existent word")

if __name__ == '__main__':
    unittest.main()
