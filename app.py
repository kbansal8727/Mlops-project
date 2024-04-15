import numpy as np
import pandas as pd
import streamlit as st
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

def recommend(p):
    print(p)
    data2 = [[p[0],p[1],p[2],p[3],2023-p[4]]]
    y=model.predict(data2)
    return y
3

model = pickle.load(open('model33.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    print(float_features)
    f=float_features
    output = recommend(f)
    output = output[0]
    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)