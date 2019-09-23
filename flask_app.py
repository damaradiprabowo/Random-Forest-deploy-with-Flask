# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:33:35 2019

@author: damara064128
"""


# Import libraries
import numpy as np
from flask import Flask, request, jsonify
#import pickle
from sklearn.externals import joblib

app = Flask(__name__)

# Load the model
model = joblib.load(open('/home/damaradiprabowo1/mysite/model_rf.pkl','rb'))

@app.route('/')
def home():
    return 'See this apps documentation on this <a href="https://github.com/damaradiprabowo/Random-Forest-deploy-with-Flask">github link</a>'


@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)

    # Make prediction using model loaded from disk (berapapun data akan bisa ke load)
    pred=[]
    for data in datas:
        prediction = model.predict([np.array([data['LIMIT_BAL'], data['PAY_1'], data['BILL_AMT1']])])

        # Take the first value of prediction
        output = int(prediction[0])
        out = "Terlambat" if output == 1 else "Tidak Terlambat"
        pred.append(out)
        
    return jsonify(pred)