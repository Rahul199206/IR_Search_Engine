
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

#initialising the list and dictionary to store posting lists and Vocabulary
vocabulary = {}
vocabulary_idf = {}         #storing number of documents in which a word is appearing
freqDist = {}               #for storing frequency of each word in a document
document_tokens_list= []
temp_doc_tokens = []        
stemmer = SnowballStemmer('english')
documentFiles = [f for f in os.listdir('./json-files') if f.endswith(".json")]
documentFiles.sort()

def buildIDF():
    """
    Function for creating the Inverse Document Frequency(IDF)
    """

    for word in vocabulary:

        
        for document_tokens in document_tokens_list:
            if word in document_tokens:
                if word in vocabulary_idf:

                    vocabulary_idf[word] = vocabulary_idf[word] + 1


                else:
                    vocabulary_idf[word] = 1


def buildFreqDist(document_tokens_list):
    """
    Function for generating the Frequency Distribution
    """
    k=0

    for document_tokens in document_tokens_list:


        freqDist[k] = FreqDist(document_tokens)

        k = k + 1


def returnTermFrequency(term, document_tokens, document_tokens_index):
    """
    Function which returns the term frequency
    """
    if(float(len(document_tokens)!=0)):
        return math.log2(1+(freqDist[document_tokens_index][term]/float(len(document_tokens))))
    else:
        return 0

def returnIDFvalue(term):
    """
    Function which returns the corresponding idf
    value in the vocabulary
    """
    return math.log2(len(document_tokens_list)/vocabulary_idf[term])

"""
Funnction for computing the primary dictionary necessary for tf-idf calculations
The structure is as follows:
It has nested dictionaries
DICTIONARY1-word in vocabulary:
                DICTIONARY2-document_number:
                    DICTIONARY3- TF,IDF,TF-IDF
"""

with open('./savers/document_tokens_list.json',encoding='utf8') as json_data:
    document_tokens_list = json.load(json_data)


with open('savers/vocabulary.json',encoding='utf8') as json_data:
    vocabulary = json.load(json_data)


buildFreqDist(document_tokens_list)

buildIDF()

primaryDictionary=dict()

j=0
for vocab in vocabulary:
    j+=1
    #for keeping count of how many words of the vocabulary are done
    if vocab not in primaryDictionary:
        inner_dict=dict()
        k=0
        for document_tokens in document_tokens_list:
            inner_dict[k]=dict()
            termFreq = returnTermFrequency(vocab, document_tokens, k)
            idf = returnIDFvalue(vocab)
            # creating the dictionary which stores the term frequency, idf and termFreq*idf value
            inner_dict[k] = {1:termFreq,2:idf,3:(termFreq*idf)}
            k = k + 1
            
    primaryDictionary[vocab]=inner_dict
#IDF by searching in the vocabulary



#storing the generated prime dictionary as a json file.
with open('savers/primeDictionary.json', 'w', encoding='utf8') as fp:
    json.dump(primaryDictionary, fp)
