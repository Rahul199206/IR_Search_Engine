
from math import log
import sys
import math
import os
import codecs
from collections import defaultdict
import pickle
import  json

# opening the json file and storing it in doc 
with open('./music.json',encoding='utf8') as json_data:
    doc = json.load(json_data)

def jsonconverter():
    """
    This file is used to convert our corpus which is "music.json" to individual json file where each
    individual json file all the information about a single song
    """
    cnt = 0
    j = 0
    for index in doc:
        # extracting only the top 1015 datasets from the 10000 datasets available
        if cnt>=1015 :
            break
        cnt+=1

        #  creating a dictionary
        dictionary = dict()
        
        j =  j+1
        dictionary["Artist"] = index['artist.name']
        dictionary["Album Name"] =  index['release.name']

        dictionary["Category"]    = index['terms']
        dictionary["Song Name"]    = index['title']
        dictionary["Duration"]    = index['duration']

        # storing each manipulated dataset in a json file in the json-files folder

        file =  "json-files/" + str(j) + ".json"

        with open(file, 'w',encoding='utf8') as fp:
            json.dump(dictionary, fp, ensure_ascii=False)




jsonconverter()
