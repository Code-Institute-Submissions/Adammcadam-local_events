import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'local_events'
app.config["MONGO_URI"] = 'mongodb+srv://root:eu4QBwmtZMzd0HU6@myfirstcluster-xm8rq.mongodb.net/local_events?retryWrites=true&w=majority'
# app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_bands')
def get_bands():
    return render_template("bands.html", bands=mongo.db.bands.find())
    
@app.route('/add_band')
def add_bands():
    venues = venues=mongo.db.venues.find()
    venue_list = [venue for venue in venues]
    return render_template("addband.html", venues = venue_list)
    
@app.route('/insert_band', methods=['POST'])
def insert_band():
    bands = mongo.db.bands
    bands.insert_one(request.form.to_dict())
    return redirect(url_for('get_bands'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

            
    
    
    