from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello!</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

      
@app.route('/aboutnew/')
def aboutnew():
    return '<h3>This is a new Flask web application.</h3>'

        
if __name__ == '__main__':
    app.run(host='0.0.0.0')