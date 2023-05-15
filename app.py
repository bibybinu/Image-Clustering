from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.utils  import secure_filename

from datetime import datetime 

import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pandas as pd
import random

from sklearn.cluster import KMeans

import numpy as np

import calendar;
import time;

import os

cluster=100
data = pd.read_csv('finaldata.csv')
feature_data=data.iloc[:, 1:2049]
result=data.iloc[:, :1]

kmeans = KMeans(n_clusters=cluster)

# Fit the model to the data
kmeans.fit(feature_data)

# Add the cluster labels to the DataFrame
result['cluster'] = kmeans.labels_



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'test'





@app.route('/')
def index():

    return render_template('index.html')


# @app.route('/input')
# def input():    
#     return render_template('input.html')


@app.route('/predict', methods=['POST'])
def process():

    folder_path = 'test/'

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


    name2= str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)+'-'+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)
    name=name2+'.jpg'
    photo = request.files['img']
    path = os.path.join(app.config['UPLOAD_FOLDER'],name)
    photo.save(path)

    os.system("python cli.py features test test.csv")

    test = pd.read_csv('test.csv')
    test_feature=test.iloc[:, 1:2049]
    test_result=test.iloc[:, :1]
    test_res=kmeans.predict(test_feature)
    test_result['cluster']=test_res


    ress=list(test_result.loc[0])

    ccc = result[result['cluster'] == ress[1]]

    finallist= random.sample(list(ccc["ID"]), 6)

    # return(finallist)
    return render_template("result.html",img=name,images=finallist)


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404

