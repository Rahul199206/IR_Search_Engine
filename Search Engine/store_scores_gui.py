import os
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
class main_class(object):

    smallcorpusSize=500
    queryStr = ""       #query from userinput
    document_tokens_list= []
    temp_doc_tokens = []
    snowball_stemmer = SnowballStemmer('english')
    docFiles = [f for f in os.listdir('./json-files') if f.endswith(".json")]
    docFiles.sort()
    
    def terminal_function():
        """
        Function for inputting query and performing query based operations and finally calculating cosine scores
        """
        with open('./savers/document_tokens_list.json',encoding='utf8') as json_data:
            document_tokens_list = json.load(json_data)

        with open('savers/vocabulary.json',encoding='utf8') as json_data:
            vocabulary = json.load(json_data)

        with open('savers/primeDictionary.json',encoding='utf8') as json_data:
            primeDictionary = json.load(json_data)
        words = main_class.queryStr
        temp_doc_tokens = nltk.word_tokenize(words)
        temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
        stemmer=SnowballStemmer('english')
        temp_doc_tokens=[stemmer.stem(w) for w in temp_doc_tokens]
        queryList = temp_doc_tokens
        

        numOfWords = 0
        #print (queryList)
        queryDict={} #contains frequency till here i.e the tf
        '''calculating frequency'''
        for q in queryList:
            numOfWords = numOfWords + 1
            if q not in queryDict:
                queryDict[q]=0
            queryDict[q]+=1

        # print (queryDict)

        queryDf={}
        #Getting total Document frequency of the word
        for qkey,qvalue in queryDict.items():
            if qkey in primeDictionary:#now here we have one document , we have to sum over multiple documents
                innerDict = primeDictionary[qkey]
                total_frequency_of_documents=0
                for i in innerDict:
                    if(innerDict[i]['1']>0):
                        total_frequency_of_documents+=1
                queryDf[qkey]=total_frequency_of_documents
            else:
                queryDf[qkey]=0
       
        queryIdf={}
        
        for q in queryDf:
            if (queryDf[q]!=0):
                queryIdf[q] = math.log((main_class.smallcorpusSize/queryDf[q]))
            else:
                queryIdf[q] = 1+math.log((main_class.smallcorpusSize/(1+queryDf[q])),10)

        for q in queryDict:
            queryDict[q] = math.log(1+(queryDict[q]/float(numOfWords)))

        '''tfWeighting - multiplying tf-raw i.e. tf and Idf'''

        queryWt={}
        for q in queryIdf:
            queryWt[q]=queryIdf[q]* queryDict[q]

        queryNormalizedDenomator=0
        for q in queryWt:
            queryNormalizedDenomator+=queryWt[q]*queryWt[q]

        #print (queryNormalizedDenomator)
        queryNormalizedDenomator=(queryNormalizedDenomator)**0.5

        queryNormalized={}
        for q in queryWt:
            queryNormalized[q] = queryWt[q]/queryNormalizedDenomator

        #print (queryNormalized)

        documentNormalizedDenominator={}
        score = {}

        with open('savers/normaliseddenom.json',encoding='utf8') as json_data:
            documentNormalizedDenominator = json.load(json_data)

        with open('savers/score.json',encoding='utf8') as json_data:
            score = json.load(json_data)
        '''
        Iterate over the weight of every term, score the summation in score
        '''
        for q in queryWt:                       #for every word in query_wt
            if q in primeDictionary:
                #now parse all documents
                innerDict = primeDictionary[q]
                for i in innerDict:
                    # print(i)
                    # print(documentNormalizedDenominator[i])
                    # print(innerDict[i]['3'])
                    if(documentNormalizedDenominator[i]!=0):
                        score[i] += queryWt[q]*(innerDict[i]['3']/(documentNormalizedDenominator[i]))

        with open('savers/store.json', 'w',encoding='utf8') as fp:
            json.dump(score, fp)
    '''
    Sort the pages according tf-idf cosine similarity

    '''
    def process_function(query):
       
        main_class.queryStr = query
        main_class.terminal_function()
        

        #find max score page
        with open('savers/store.json',encoding='utf8') as json_data:
            score = json.load(json_data)

        sorted_score = sorted(score, key=score.get, reverse=True)
        # print(sorted_score)
        linkNumber_list = sorted_score[:10]
        docList = []
        newlist= []
        for f in linkNumber_list:
             f =    int( float(f)) +1
            #  print(f)
             with open("./json-files/"+ str(f) + ".json",encoding='utf8') as json_data:
                 document = json.load(json_data)
             contents = "<strong>Song: </strong>" + document["Song Name"] + " -- " + "<strong>Genre: </strong>" + document["Category"] + " -- " + "<strong>Artist: </strong>" + document["Artist"] + " -- " + "<strong>Duration: </strong>" + str(document["Duration"])+" seconds" 
             
             newlist.append(contents)
        # print(newlist)

        return newlist
