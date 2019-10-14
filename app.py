import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
app.config.from_object(Config)

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)