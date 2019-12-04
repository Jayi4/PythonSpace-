#!/usr/bash/python3

#import json to turn poems.json into pythonic date structures
import json
#randomly select a poem from our pythonic data
import random
#Open my poem database ((poems.json)

#Option(1): Calling from a text file
#with open(r"C:\Users\Student\Documents\Poems\Poems.text") as pj:

#Option 2: Calling form a local file
with open("poems.json") as pj:
    pythonpoems = json.load(pj)
#Randomly select a poem from the pythonic data
print(random.choice(list(pythonpoems.values())))

#Notes
#with Command: 