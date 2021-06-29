from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
import os
from nltk.stem.snowball import SnowballStemmer
from collections import OrderedDict
from collections import defaultdict
import pickle
import  json

nltk.download('punkt')
nltk.download('stopwords')
artist_name_list= []

documentFiles = [f for f in os.listdir('./json-files') if f.endswith(".json")]

for k in range(len(documentFiles)):

    documentFiles[k] = int(documentFiles[k].split(".")[0])
    
# sorting the artist name list created
documentFiles.sort()
 

def create_artist_name_list():
    """
    This file helps in getting the names of artists and bands
     from our corpus and saving it as artist_name_list.json
    """
    num=0
    for file in documentFiles :
        document =  dict()
        with open("./json-files/"+ str(file) + ".json",encoding='utf8') as json_data:
         document = json.load(json_data)

        num+=1
        artist_name_list.append(document["Artist"]) 

    # storing the artist name list as a list in artist_names and then sorting it
    artist_names = set(artist_name_list)
    artist_names=list(set(artist_names))
    artist_names.sort()
    
    # creating a new json file with all the artist and band names
    with open('savers/artist_name_list.json', 'w',encoding='utf8') as fp:
        json.dump(artist_names, fp)



create_artist_name_list()
