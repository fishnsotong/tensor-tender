import sys, json
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

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def readData(pathToFile, n_output):
# import from local directory
    dataset = pd.read_csv(pathToFile).values # not sure if I have headers, change to general data
    print(dataset.shape)
    X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, :-n_output], dataset[:, -n_output:], test_size=0.25, random_state=87)
    print(X_train.shape, Y_train.shape)
    return X_train, Y_train, X_test, Y_test

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

def predictNN(nn, test_input):
    drinkMix = nn.predict(test_input, batch_size=None, steps=None)
    return drinkMix

def main():
    #get our data as an array from read_in()
    lines = read_in()

    if lines:
        flavour_input = np.array(lines)
        drinkMix = predictNN(nn, flavour_input)
        print drinkMix

#setup
nn = loadNN()

#start process
if __name__ == '__main__':
    main()
