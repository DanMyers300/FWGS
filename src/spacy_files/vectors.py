import string
import spacy
from collections import defaultdict
from gensim.models.word2vec import Word2Vec
from gensim.models.phrases import Phrases, Phraser

file = 'data/corpus.txt'
def open_file(file):
    with open(file, 'r') as f:
        text = f.read()
    return text

corpus = open_file(file)
corpus = corpus.lower()
words = corpus.split()


stopwords = ['a', 'an', 'the', 'and', 'or', 'but', 'if', 'because', 'as', 'what', 'which', 'this', 'that', 'these', 'those', 'then', 'just', 'so', 'than', 'such', 'both', 'through', 'about', 'for', 'is', 'of', 'while', 'during', 'to', 'What', 'Which', 'Is', 'If', 'While', 'This']

new_corpus = []
for word in words:
    if word not in stopwords:
        new_corpus.append(word)
corpus = " ".join(new_corpus)

nlp = spacy.load("en_core_web_sm")
doc = nlp(corpus)

sentences = []
for sent in doc.sents:
    sentence = sent.text.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    sentences.append(words)

def create_wordvecs(corpus, model_name):
    print(len(corpus))

    phrases = Phrases(corpus, min_count=30, progress_per=10000)
    print("Made phrases")

    bigram = Phraser(phrases)
    print("Made bigram")

    sentences = phrases[corpus]
    print("Found sentences")
    word_freq = defaultdict(int)

    for sent in sentences:
        for i in sent:
            word_freq[i] += 1
    
    print(len(word_freq))

    print("Training model now...")

    w2v_model = Word2Vec(min_count=1,
                         window=2,
                         vector_size=10,
                         sample=6e-5,
                         alpha=0.03,
                         min_alpha=0.0007,
                         negative=20)
    w2v_model.build_vocab(sentences, progress_per=10000)
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
    w2v_model.wv.save_word2vec_format(f"data/outputs/{model_name}.txt")
create_wordvecs(sentences, "rfq_wordvecs")

