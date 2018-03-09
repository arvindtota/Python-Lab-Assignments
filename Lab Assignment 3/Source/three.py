from nltk.corpus import wordnet as wn
from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
import re, collections
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from collections import Counter
from nltk import FreqDist
import nltk
from nltk import ngrams
from operator import itemgetter


# Loading input file
with open('three.txt' , 'r') as f:
    lines = f.readlines()
print("lines",lines)
frm=''
#converting multiline to single string
for m in lines:
    frm=frm+m
print(frm)
#tokenize word
frm_word = word_tokenize(frm)
frm_sent = sent_tokenize(frm)

# Applying lemmitization
lemmatizer = WordNetLemmatizer()
frm_lemma = []
for word in frm_word:
    fr_lema = lemmatizer.lemmatize(word.lower())
    frm_lemma.append(fr_lema)

print("\n_____Lemitization Output ________  ")
print(frm_lemma)
frm_pos = pos_tag(frm_lemma)

print("_____Bigram Output_____")

n = 2
gram=[]
bigrams = ngrams(frm_lemma, n)
for grams in bigrams:
    gram.append(grams)
print(gram)
str1 = " ".join(str(x) for x,y in frm_pos)
str1_word = word_tokenize(str1)
print("______Word frequency Bigrams_______")
fdist1 = nltk.FreqDist(gram)
top_fiv = fdist1.most_common()
top_5 = fdist1.most_common(5)

top=sorted(top_fiv,key=itemgetter(0))
print(top)
print('_______Top 5 words Bigrams_______')
print(top_5)
sent1 = sent_tokenize(frm)
rep_sent1 = []


for sent in sent1:
    for word,words in gram:
        for ((c,m), l) in top_5:
            if (word,words == c,m):
                rep_sent1.append(sent)  # Creating sentences containing the most common words
print ("\n____Top 5 Bigrams sentences______")
print(max(rep_sent1,key=len))