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

nltk.download('punkt')
nltk.download('stopwords')
vocabulary = {}
vocabulary_idf = {}
freqDist = {}
document_tokens_list= []
temp_doc_tokens = []
stemmer = SnowballStemmer('english')
documentFiles = [f for f in os.listdir('./json-files') if f.endswith(".json")]


for i in range(len(documentFiles)):

    documentFiles[i] = int(documentFiles[i].split(".")[0])
    

documentFiles.sort()
 

def create_document_tokens_list():
    """
    This file helps in storing the tokenized words we get from each document as lists and
     then the corresponding list is stored document_tokens_list.json
    """
    
    for file in documentFiles :
        document =  dict()
        with open("./json-files/"+ str(file) + ".json",encoding='utf8') as json_data:
         document = json.load(json_data)

        # creating a string consisting of artist name, album name, category and song name for further tokenization 
        words = str(document["Artist"] + " " + document["Album Name"] + " " +  document["Category"] + " " + document["Song Name"])
        

        # tokenizing the string created
        temp_doc_tokens = nltk.word_tokenize(words)
       
        temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
        temp_doc_tokens = [stemmer.stem(token) for token in temp_doc_tokens]
        temp_doc_tokens = [token for token in temp_doc_tokens if token not in nltk.corpus.stopwords.words('english')]
        
        document_tokens_list.append(temp_doc_tokens)


    
    with open('savers/document_tokens_list.json', 'w',encoding='utf8') as fp:
        json.dump(document_tokens_list, fp)



create_document_tokens_list()
