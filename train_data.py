#Thank You Jesus
#Glory be to your name
#Holy Spirit the brains behind this project

import random as rd
import numpy as np
import json
import nltk
from nltk.stem import WordNetLemmatizer
import pickle

#import tensorflow as tf
#from tensorflow.keras.models import sequential
#from tensorflow.keras.layers import Dense, Activation, Dropout
#from tensorflow.keras.optimizersimport SGD

lematizer = WordNetLemmatizer()

intents = json.loads(open("intents.json").read())

words = []
classes = []
documents = []
ignore_letters = ['?','!','.',',']

for intent in intents["intents"]:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = [lematizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
print(words)

classes = sorted(set(classes))
pickle.dump(words, open('words.pkl', wb))
pickle.dump(words, open('classes.pkl', wb))


training = []
output_empty =[0]