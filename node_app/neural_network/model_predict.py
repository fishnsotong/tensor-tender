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

from flask import Flask
from flask import request
from flask import make_response

import serial
ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

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

def arduinoComm(resp):
    global ser
    ser.write(resp.encode('utf-8'))


#setup
nn = loadNN()

app = Flask(__name__)

@app.route("/pred", methods=['GET', 'POST'])
def pred():
    print('entered pred function')
    print(request.method)
    print (request.data)
    if request.method == 'POST':
        print("Req body: " + json.dumps(request.get_json()))
        print(np.array([request.get_json(force=True)]).shape)
        flavourProfile = np.array([request.get_json(force=True)])
        drinkMix = predictNN(nn, flavourProfile)
        resp = str(np.array(drinkMix).tolist())
        print(resp)
        arduinoComm(resp)
        return make_response(resp)
    else:
        print('GET request received isntead of POST request')
        return
