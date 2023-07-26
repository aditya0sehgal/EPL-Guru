from flask import Flask, render_template, request
import pandas as pd
import random, numpy, csv, io, os, json
import time

app = Flask(__name__)

# Home landing page
@app.route("/" , methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/players')
def about():
    return render_template('player_info.html')

@app.route('/aboutnew/')
def aboutnew():
    return '<h3>This is a new Flask web application.</h3>'
        
if __name__ == '__main__':
    app.run(host='0.0.0.0')