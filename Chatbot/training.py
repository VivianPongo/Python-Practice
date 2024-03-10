#pip --version
# pip install tensorflow


import random
import json
import pickle 
import numpy as np  #pip install  numpy
import nltk  #pip install nltk
from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
import tensorflow as tf
from keras.optimizers import SGD
 


lenmataizer = WordNetLemmatizer

path = "intents.json"  #deben tener el mismo nombre la api -- "intents1":[ del json y el nombre del archivo json
data_file= open(path).read()
intents = json.loads(data_file)




nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

words = []
classes = []
documents = []
ignore_letter = ["?", "!", "¡", ".", ",", "¿"]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])


words = [nltk.stem.WordNetLemmatizer().lemmatize(word) for word in ignore_letter]
words = sorted(set(words))

pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))

training = []
output_empty = [0]*len(classes)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [nltk.stem.WordNetLemmatizer().lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(document[1])]=1 #indice a 1
    training.append([bag, output_row])

random.shuffle(training)
#training2 = np.array(training)
#array(training2, dtype = object)

print(training)


train_x = list(training[:0])
train_y = list(training[:1])


#modelo de aprendizaje automatico
model = Sequential()
#capa dense de 128 neuronas 
model.add(Dense(128, input_shape=(len(train_x[0]))))
model.add(Dropout(0.5))
model.add(Dense(64,activation="relu" ))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))


sgd = SGD(learning_rate=0.001, weight_decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer = sgd, metrics = ['accuracy'])


train_process = model.fit(np.array(train_x), np.array(train_y), epochs=100, batch_size=5, verbose=1)
model.save("chatbot_model.h5", train_process)










