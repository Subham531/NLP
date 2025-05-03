import re
corpus = "The sun rises in the east.The sun sets in the west.Birds fly in the sky.The sky is blue and clear.Flowers bloom in the spring"
text = re.sub(r'[^\w\s]',' ',corpus)
tokens = [corp.lower() for corp in text.split()]
Unigram  = {}
for i in range(len(tokens)):
    Unigram[tokens[i]] = tokens.count(tokens[i])
total = len(tokens)
for vals,key in Unigram.items():
    Unigram[vals] = key/total

