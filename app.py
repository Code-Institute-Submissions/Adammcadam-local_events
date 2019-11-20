import os
import math
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from forms import CreateBandForm, EditBandForm, ConfirmCompletion, CreateVenueForm
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'local_events'
app.config["MONGO_URI"] = ''
# this solves CSRF key issues
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_bands')
def get_bands():
    recent_bands = mongo.db.bands.find().sort([("event_date", -1)]).limit(4)
    most_viewed = mongo.db.bands.find().sort([("views", -1)]).limit(4)
    return render_template("index.html", recent_bands=recent_bands, most_viewed=most_viewed)
    
@app.route('/insert_band', methods=['GET', 'POST'])
def insert_band():
    form = CreateBandForm(request.form)
    venues = mongo.db.venues.find()
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
    return render_template('addband.html', venues=venues, form=form)
    
    
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

@app.route('/bands')
def bands():
    per_page = 8
    page = int(request.args.get('page', 1))
    total = mongo.db.bands.count_documents({})
    all_bands = mongo.db.bands.find().skip((page - 1)*per_page).limit(per_page)
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    return render_template('bands.html', bands=all_bands, page=page, pages=pages, total=total)
    
@app.route('/band/<band_id>')
def band(band_id):
    mongo.db.bands.find_one_and_update(
        {'_id' : ObjectId(band_id)},
        {'$inc' : {'views' : 1} }    
    )
    band_db = mongo.db.bands.find_one_or_404({'_id' : ObjectId(band_id)})
    return render_template('band.html', band=band_db)
    
    
@app.route('/get_venues')
def get_venues():
    return render_template("venues.html", venues=mongo.db.bands.find())

@app.route('/insert_venue', methods=['GET', 'POST'])
def insert_venue():
    form = CreateVenueForm(request.form)
    if form.validate_on_submit():
        venues_db = mongo.db.venues
        venues_db.insert_one({
            
        })
        return redirect(url_for('get_venues'))
    return render_template('addvenue.html', form=form)
    
@app.errorhandler(404)
def handle_404(exception):
    return render_template('404.html', exception=exception)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

            
    
    
    
