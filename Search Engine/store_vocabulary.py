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
import  json

vocabulary = {}
vocabulary_idf = {}
freqDist = {}
document_tokens_list= []
temp_doc_tokens = []
stemmer = SnowballStemmer('english')
documentFiles = [f for f in os.listdir('./json-files') if f.endswith(".json")]
documentFiles.sort()


def compute_vocabulary():
    """
    Function for getting the document_tokens_list for generating the vocabulary and then storing the vocabulary in a json file
    """
    with open('./savers/document_tokens_list.json',encoding='utf8') as json_data:
        document_tokens_list = json.load(json_data)

    for document_tokens in document_tokens_list:

        __build_vocabulary(document_tokens)

    with open('savers/vocabulary.json', 'w',encoding='utf8') as fp:
        json.dump(vocabulary, fp)

def __build_vocabulary(document_tokens):
        """
        Function for generating the vocabulary i.e. the dictionary which has all the unique words in the corpus
        """
        count=0
        
        vocabulary_index=len(vocabulary)-1
        # accsessing words in document tokens list
        for word in document_tokens: 
                if word not in vocabulary:
                            

                            count+=1
                            vocabulary[word] = vocabulary_index
                            vocabulary_index+= 1


compute_vocabulary()
