import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
import time
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import keras
from keras import optimizers
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

seed = 155
np.random.seed(seed)

def readData(pathToFile, n_output):
# import from local directory
    dataset = pd.read_csv(pathToFile).values # not sure if I have headers, change to general data
    print(dataset.shape)
    X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, :-n_output], dataset[:, -n_output:], test_size=0.25, random_state=87)
    print(X_train.shape, Y_train.shape)
    return X_train, Y_train, X_test, Y_test

def compileNN(n_input, n_hidden, n_output):
    nn = Sequential()
    #don’t explicitly create the input layer. Instead, we specify the number of neurons (or features) that feed into the first hidden layer.
    nn.add(Dense(units=n_hidden, input_dim=n_input, activation='relu')) # hidden layer
    nn.add(Dense(units=n_output, activation='sigmoid')) # output layer

    sgd = optimizers.SGD(lr=0.1, decay=1e-5, momentum=0.9, nesterov=True)
    nn.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
    return nn

def fitNN(nn, X_train, Y_train, n_epoch):
    filepath="weights_history/nn_weights-{epoch:02d}.hdf5"
    checkpoint = keras.callbacks.ModelCheckpoint(filepath, monitor='val_acc', save_weights_only=False, save_best_only=False, mode='max')
    nn_fitted = nn.fit(X_train, Y_train, epochs=n_epoch, batch_size=X_train.shape[0], callbacks=[checkpoint], initial_epoch=0)
    print('finished fitting')

    evalNN(nn, X_test, Y_test)

    # serialize model to JSON
    nn_json = nn.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(nn_json)
    # serialize weights to HDF5
    nn.save_weights("model.h5")
    print("Saved model to disk")
    return nn_fitted

def loadNN():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    return loaded_model

def predictNN(test_input):
    nn = loadNN()
    nn.predict(test_input, batch_size=None, steps=None)

def evalNN(nn, X_test, Y_test):
    print('entered function')
    print(nn.evaluate(X_test, Y_test))

def evalNNHistory(nn_fitted, lastEpoch):
    [nn_fitted.history['loss'][0:lastEpoch],nn_fitted.history['acc'][0:lastEpoch]]

def visualNNProg(nn_fitted, X_test, Y_test):
    temp_test_model = Sequential() # create model
    temp_test_model.add(Dense(units=20, input_dim=14, activation='relu')) # hidden layer
    temp_test_model.add(Dense(units=5, activation='sigmoid')) # output layer
    temp_test_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    test_over_time = []
    for i in range(len(nn_fitted.history['acc'])):
        temp_test_model.load_weights("weights_history/nn_weights-%02d.hdf5" % i)
        scores = temp_test_model.evaluate(X_test, Y_test, verbose=0)
        # 0 is loss; 1 is accuracy
        test_over_time.append(scores)

X_train, Y_train, X_test, Y_test = readData("data/trainingData.csv", 5)
# nn = compileNN(14, 20, 5)
# nn_fitted = fitNN(nn, X_train, Y_train, 500)
test_input = np.array([0.109589, 0.0958904, 0.0958904, 0.0273973, 0.0958904, 0.0821918, 0.136986, 0.0821918, 0.0136986, 0.0684932, 0.0821918, 0.0684932, 0.0410959, 0.0136986])
test_input.shape
#predictNN(test_input)
# evalNN(nn, X_test, Y_test)
# evalNNHistory(nn_fitted, 500)
# visualNNProg(nn_fitted, X_test, Y_test)
