from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
import os
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import json


queryStr = ""       #query from userinput
vocabulary = {}
vocabulary_idf = {}
freqDist = {}
document_tokens_list= []
temp_doc_tokens = []
stemmer = SnowballStemmer('english')

# opening the document_tokens_list json file
with open('./savers/document_tokens_list.json',encoding='utf8') as json_data:
        document_tokens_list = json.load(json_data)

# opening the vocabulary json file
with open('savers/vocabulary.json',encoding='utf8') as json_data:
        vocabulary = json.load(json_data)

# oepning the primeDictionary json file
with open('savers/primeDictionary.json',encoding='utf8') as json_data:
        primeDictionary = json.load(json_data)

"""
 This file help in precalculation of the normalized length of each
  documents and then store it as a json file(normaliseddenom.json)
"""
documentNormalizedDenominator={}
score = {}
 #initializing all document Normalized Denominator values to zero
for q in primeDictionary:
    innerDict=primeDictionary[q]
    for i in innerDict:
        documentNormalizedDenominator[i]=0
        score[i]=0


for q in primeDictionary:
    innerDict=primeDictionary[q]
    for i in innerDict:
        documentNormalizedDenominator[i]+=(math.pow(innerDict[i]['3'],2))


for d in documentNormalizedDenominator:

        documentNormalizedDenominator[d]=documentNormalizedDenominator[d]**0.5

with open('savers/normaliseddenom.json','w',encoding='utf8') as fp:
		json.dump(documentNormalizedDenominator,fp)

with open('savers/score.json','w',encoding='utf8') as fp:
		json.dump(score,fp)

        
