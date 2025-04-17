import re
from collections import defaultdict

def gets_stat(vocab):
    pairs = defaultdict(int)
    for word,freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    
    return pairs


def merges(vocab,pairs):
    out = {}
    bigram = re.escape(' '.join(pairs))
    for i in vocab:
        wout = re.sub(bigram,''.join(pairs),i)
        out[wout] = vocab[i]
    
    return out


num_merges = 10
vocab = {'l o w </w>':5,'l o w e s t </w>':2,'w i d e r </w>':3,'n e w e r </w>':6}
for i in range(num_merges):
    pairs = gets_stat(vocab)
    best = max(pairs,key=pairs.get)
    vocab = merges(vocab,best)
    print(best)

# print(vocab)


