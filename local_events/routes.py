import os
import math
from local_events import app, mongo
from flask import Flask, render_template, redirect, request, url_for, flash
from bson.objectid import ObjectId
from local_events.forms import CreateBandForm, CreateVenueForm

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    bands_collection = mongo.db.bands
    bands = bands_collection.find()
    recent_bands = mongo.db.bands.find().sort([("event_date", -1)]).limit(4)
    most_viewed = mongo.db.bands.find().sort([("views", -1)]).limit(4)
    return render_template('home.html', bands=bands, recent_bands=recent_bands, most_viewed=most_viewed)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/create_gig", methods=['GET', 'POST'])
def create_gig():
    venues_collection = mongo.db.venues
    venues = venues_collection.find()
    for venue in venues:
        v_id = venue['_id']
        v_name = venue['venue_name']
        print(v_name)
    #Now forming the list of tuples for SelectField
    venues_list = [(v_id, v_name) for v_name in venues]
    form = CreateBandForm()
    form.venue_name.choices = venues_list
    if request.method == 'POST' and form.validate_on_submit():
        bands_db = mongo.db.bands
        bands_db.insert({
            'band_name' : request.form['band_name'],
            'venue_name' : request.form['venue_name'],
            'event_date' : request.form['event_date'],
            'is_headlining' : request.form['is_headlining'],
            'band_logo' : request.form['band_logo'],
            'views' : 0, 
        })
        flash(f'Band created for {form.band_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('create_gig.html', title='Create Gig', form=form)
    
@app.route('/gig/<band_id>', methods=['GET', 'POST'])
def band(band_id):
    bands_collection = mongo.db.bands
    bands_collection.find_one_and_update(
        {'_id' : ObjectId(band_id)},
        {'$inc' : {'views' : 1} }    
    )
    band = bands_collection.find_one_or_404({"_id": ObjectId(band_id)})
    return render_template('band.html', title='Band', band=band)
    
@app.route('/gig/<band_id>/update', methods=['GET', 'POST'])
def update_band(band_id):
    bands_collection = mongo.db.bands
    band = bands_collection.find_one_or_404({"_id": ObjectId(band_id)})
    form = CreateBandForm()
    if request.method == 'POST' and form.validate_on_submit():
        band.update_one({
            '_id' : ObjectId(band_id)
        }, {
            '$set' :  {
                'band_name' : request.form['band_name'],
                'venue_name' : request.form['venue_name'],
                'event_date' : request.form['event_date'],
                'is_headlining' : request.form['is_headlining'],
                'band_logo' : request.form['band_logo']
            }
        })
        flash(f'Band updated for {form.band_name.data}!', 'success')
        return redirect(url_for('band', band_id=band._id))
    elif request.method == 'GET':
        form.band_name.data = band.band_name
        form.venue_name.data = band.venue_name
        form.event_date.data = band.event_date
    return render_template('create_gig.html', title='Update Gig', form=form)

@app.route('/gig/<band_id>/delete', methods=['POST'])
def delete_band(band_id):
    bands_collection = mongo.db.bands
    bands_collection.delete_one({"_id": ObjectId(band_id)})
    flash(f'Band deleted!', 'success')
    return redirect(url_for('home'))

@app.route('/bands')
def bands():
    per_page = 8
    page = int(request.args.get('page', 1))
    total = mongo.db.bands.count_documents({})
    all_bands = mongo.db.bands.find().skip((page - 1)*per_page).limit(per_page)
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    return render_template('bands.html', bands=all_bands, page=page, pages=pages, total=total)

@app.route('/venues')
def venues():
    venues_collection = mongo.db.venues
    venues = venues_collection.find()
    return render_template('venues.html', venues=venues)

@app.route('/create-venue')
def create_venue():
    form = CreateVenueForm()
    if request.method == 'POST' and form.validate_on_submit():
        venues_db = mongo.db.venues
        venues_db.insert({
            'venue_name' : request.form['venue_name'],
            'address' : request.form['address'],
            'postcode' : request.form['postcode'],
            'website' : request.form['website'],
        })
        flash(f'Venue created for {form.venue_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('create_venue.html', title='Create Venue', form=form)
    
    
@app.errorhandler(404)
def handle_404(exception):
    return render_template('404.html', exception=exception)
            

            
    
    
    
