
import json
import os
import numpy as np

documentFiles = [f for f in os.listdir('./json-files') if f.endswith(".json")]
categories = []

"""
This file helps in getting the names of category or genre from our corpus and saving it as category.json
"""
for file in documentFiles:
    
    document =  dict()
    with open("./json-files/"+ file,encoding='utf8') as json_data:
        document = json.load(json_data)
    
    # appending the categories to the categories list created and then keeping the unique categories in the list
    categories.append(document["Category"])
    categories = np.unique(categories).tolist()
    # creating a new json file with all the categories
    with open('savers/category.json', 'w',encoding='utf8') as fp:
        json.dump(categories, fp)
    

