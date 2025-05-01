import re
from collections import defaultdict
def gets_stats(vocab):
  pairs = defaultdict(int)
  for word,freq in vocab.items(): # for both word and its frequency
    symbols = word.split() # separated each words
    for i in range(len(symbols) - 1):
      pairs[symbols[i],symbols[i+1]] += freq # updating pairs
  return pairs

def merge_vocab(pairs,vocab):
  out = {}
  bigram = re.escape(' '.join(pairs)) # escape is used for matching the literals
  for word in vocab: # for only word this time
    wout = re.sub(bigram,''.join(pairs),word) # substituting word with join pairs and update
    out[wout] = vocab[word] # stored the frequency of the new merged word, taken from the original word's frequency
  return out

vocab = {'l o w </w>' : 5, 'l o w e r </w>' : 2,
'n e w e s t </w>':6, 'w i d e s t </w>':3}

num_merges = 10
for i in range(num_merges):
  pairs = gets_stats(vocab)
  if not pairs:
    break
  best = max(pairs, key=pairs.get)
  vocab = merge_vocab(best, vocab)
  print(best)