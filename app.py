import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from forms import CreateBandForm, EditBandForm, ConfirmCompletion
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'local_events'
app.config["MONGO_URI"] = ''
# app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_bands')
def get_bands():
    recent_bands = mongo.db.bands.find().sort({'event_date' : -1}).limit(4)
    most_viewed = mongo.db.bands.find().sort({'views' : -1}).limit(4)
    return render_template("bands.html", recent=recent_bands, most_viewed=most_viewed)
    
@app.route('/insert_band', methods=['GET', 'POST'])
def insert_band():
    form = CreateBandForm(request.form)
    if form.validate_on_submit():
        bands_db = mongo.db.bands
        bands_db.insert_one({
            'band_name' : request.form['band_name'],
            'venue_name' : request.form['venue_name'],
            'is_headlining' : request.form['is_headlining'],
            'event_date' : request.form['event_date'],
            'views' : 0,
            'band_logo' : request.form['band_logo']
        })
        return redirect(url_for('get_bands'))
    return render_template('addband.html', form=form)
    
    
@app.route('/edit_band/<band_id>', methods=['GET', 'POST'])
def edit_band(band_id):
    band_db = mongo.db.bands.find_one({"_id": ObjectId(band_id)})
    if request.method == 'GET':
        form = EditBandForm(data=band_db)
        return render_template('editband.html', band=band_db, form=form)
    form = EditBandForm(request.form)
    if form.validate_on_submit():
        band_db = mongo.db.bands
        band_db.update_one({
            '_id' : ObjectId(band_id)
        }, {
            '$set' :  {
                'band_name' : request.form['band_name'],
                'venue_name' : request.form['venue_name'],
                'is_headlining' : request.form['is_headlining'],
                'event_date' : request.form['event_date'],
                'band_logo' : request.form['band_logo']
            }
        })
        return redirect(url_for('get_bands'))
    all_venues = mongo.db.venues.find()
    return render_template('editband.html', band=band_db, venues=all_venues, form=form)

    
@app.route('/complete_event/<band_id>', methods=['GET','POST'])
def complete_event(band_id):
    band_db = mongo.db.bands.find_one({"_id": ObjectId(band_id)})
    if request.method == 'GET':
        form = ConfirmCompletion(data=band_db)
        return render_template('complete_event.html', band=band_db, form=form)
    form = ConfirmCompletion(band_db)
    if form.validate_on_submit():
        band_db = mongo.db.bands
        band_db.update_one({
            '_id' : ObjectId(band_id)
        }, {
            '$set' : {
                'is_done' : True 
            }
        })
        return redirect(url_for('get_bands'))
    all_venues = mongo.db.venues.find()
    return render_template('complete_event.html', band=band_db, venues=all_venues, form=form)

    
@app.route('/get_venues')
def get_venues():
    return render_template("venues.html", venues=mongo.db.bands.find())
    
@app.route(404)
def handle_404(exception):
    return render_template('404.html', exception=exception)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

            
    
    
    
