# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:30:54 2020

@author: gulsum.atici
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
    