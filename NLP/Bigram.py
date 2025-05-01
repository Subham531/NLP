#   preprocessing the input text --------->

import re

corpus = "The sun rises in the east.The sun sets in the west.Birds fly in the sky.The sky is blue and clear.Flowers bloom in the spring"

corp = corpus.lower()

new_corp = re.sub(r'[^\w\s]', ' ', corp)

text = new_corp.split()

  # <------  tuplify it --------->
bigram = []
for i in range(len(text)-1):
    bigram.append((text[i],text[i+1]))

# <---------- dictionarfication ---------->
bigram2 = {}
for i in range(len(text)-1):
  if text[i] not in bigram2:
    bigram2[text[i]] = []
  bigram2[text[i]].append(text[i+1])

# ---------- frequency table ------------>
# x = bigram2['the'].count('sun')
freq_table = {}
for key,vals in bigram2.items():
  freq_table[key] = {}

  for val in vals:
    if val not in freq_table[key]:
      freq_table[key][val] = 1
    else:
      freq_table[key][val] += 1


# -------probablity------->

prob_table = {}
for keys in freq_table:
  total=0
  prob_table[keys] = {}
  for key,vals in freq_table[keys].items():
    total += vals
  for key,vals in freq_table[keys].items():
    prob_table[keys][key] = vals /  total

# ----  word prediction ------>
text = input() # For bigram model only one word will be needed
if text in prob_table:
  max_prob = max(prob_table[text].values())
  for key,val in prob_table[text].items():
    if val == max_prob:
      print(key)
      break

else:
  print('Word not present in corpus')