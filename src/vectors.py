import string
import spacy
from collections import defaultdict
from gensim.models.word2vec import Word2Vec
from gensim.models.phrases import Phrases, Phraser

stopwords = ['a', 'an', 'the', 'and', 'or', 'but', 'if', 'because', 'as', 'what', 'which', 'this', 'that', 'these', 'those', 'then', 'just', 'so', 'than', 'such', 'both', 'through', 'about', 'for', 'is', 'of', 'while', 'during', 'to', 'What', 'Which', 'Is', 'If', 'While', 'This']

file = 'data/outputs/rfq_dump.txt'

def open_file(file):
    with open(file, 'r') as f:
        text = f.read()
    return text

corpus = open_file(file)

corpus = corpus.lower()
words = corpus.split()

new_corpus = []
for word in words:
    if word not in stopwords:
        new_corpus.append(word)

corpus = " ".join(new_corpus)
print(corpus)
