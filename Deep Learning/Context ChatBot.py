import pickle
import json

with open('intent.json') as json_data:
    intents = json.load(json_data)

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import random

words =[]
classes =[]
documents = []
ignore_words = ['?']


for intent in intents['intents']:
    for pattern in intents['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print(len(documents),'documents',documents)
print('###################################')
print(len(classes),'classes',classes)
print('####################################')
print(len(words),'Unique Stemmed words',words)

training = []
output = []
total_data = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

output_row = list(output_empty)
output_row[classes.index(doc[1])] = 1
total_data.append(output_row)
training.append([bag,output_row])

random.shuffle(training)
training = np.array(training)
train_x = list(training[:,0])
train_y = list(training[:,1])
