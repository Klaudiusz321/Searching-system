import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# Pobranie angielskich stop-słów
nltk.download('stopwords')
english_stopwords = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

def tokenize(text):
    
    return re.findall(r'\b\w+\b', text.lower())

def preprocess_text(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    processed = [stemmer.stem(token) for token in tokens if token not in english_stopwords]
    return processed
