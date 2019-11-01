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
    return render_template("addband.html", venues=mongo.db.venues.find())
    
@app.route('/insert_band', methods=['POST'])
def insert_band():
    bands = mongo.db.bands
    bands.insert_one(request.form.to_dict())
    return redirect(url_for('get_bands'))
    
@app.route('/edit_band/<band_id>')
def edit_band(band_id):
    the_band = mongo.db.bands.find_one({"_id": ObjectId(band_id)})
    all_venues = mongo.db.venues.find()
    return render_template('editband.html', band=the_band, venues=all_venues)
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

            
    
    
    