
# Basic implementation of TF-IDF

import numpy as np
docs = [
    "I love machine learning and natural language processing",
    "Machine learning is great",
    "Natural language processing makes machines understand humans"
]

def preprocess(text):
  return text.lower().split()

tokenized_docs = [preprocess(doc) for doc in docs]

# tokenized_docs

vocab = sorted(set(word for doc in tokenized_docs for word in doc))
vocab_idx = {word:i for i,word in enumerate(vocab)}


def compute_tf(doc):
  tf = np.zeros(len(vocab))
  for word in doc:
    if word in vocab:
      tf[vocab_idx[word]]+=1

    return tf/len(docs)
tf_matrix = np.array([compute_tf(doc) for doc in tokenized_docs])


def compute_idf(doc):
  N = len(docs)
  idf = np.zeros(len(vocab))

  for i,word in enumerate(vocab):
    df = sum(1 for doc in docs if word in doc)
    idf[i] = np.log((N+1)/ (df+1))

  return idf

idf_vector = compute_idf(tokenized_docs)


tfidf_matrix = tf_matrix * idf_vector
print(tfidf_matrix)


def cosine_similarity(a,b):
  dot = np.dot(a,b)
  norm_a = np.linalg.norm(a)
  norm_b = np.linalg.norm(b)

  return dot/(norm_a * norm_b)


similarity = cosine_similarity(tf_matrix,idf_vector)
print(similarity)
